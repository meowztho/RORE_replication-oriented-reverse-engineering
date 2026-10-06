#!/usr/bin/env python3
"""Evidence-based target requirement coverage for CoreReplica.

Standard library only.

Unlike the upstream Replica parity tool, this version deliberately does NOT read
builder-owned implementation status. It scores target requirements from
verifier-owned evidence:

    python3 parity.py corereplica/product/REQUIREMENTS.csv \
        corereplica/verification/EVIDENCE.json

Requirements CSV columns (extra columns are ignored):

    id           stable target requirement ID
    area         optional product area
    requirement  user/product outcome
    scope_status active | deferred | out_of_scope (optional; defaults active)
    priority     must | should | could (P0 | P1 | P2 also accepted for active scope)
    acceptance   optional acceptance summary
    notes        optional notes

Evidence JSON shape:

    {
      "revision": "<revision>",
      "requirements": {
        "REQ-001": {
          "status": "VERIFIED|PARTIAL|FAILED|INCONCLUSIVE|SKIP",
          "evidence": [...],
          "notes": "..."
        }
      }
    }

Active requirements are scored with weights must 3, should 2, could 1. Deferred/out_of_scope requirements are excluded before evidence scoring. VERIFIED earns full credit, PARTIAL half, FAILED/INCONCLUSIVE/missing earn zero. Evidence status SKIP remains a backwards-compatible verifier exclusion but Product Truth scope_status is preferred. A score is verification coverage, not release authority.
"""

import argparse
import csv
import json
import sys

WEIGHT = {"must": 3, "should": 2, "could": 1, "p0": 3, "p1": 2, "p2": 1}
PRIORITY_NAME = {3: "must", 2: "should", 1: "could"}
CREDIT = {
    "VERIFIED": 1.0,
    "PARTIAL": 0.5,
    "FAILED": 0.0,
    "INCONCLUSIVE": 0.0,
}
VALID_STATUS = set(CREDIT) | {"SKIP"}


class ParityError(Exception):
    pass


def load_requirements(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None:
            raise ParityError("%s is empty" % path)
        fields = [f.strip().lower() for f in reader.fieldnames]
        for need in ("id", "requirement", "priority"):
            if need not in fields:
                raise ParityError(
                    "%s has no '%s' column. Required: id, requirement, priority" % (path, need)
                )
        forbidden = {"clone", "done", "verified", "implementation_status"}
        bad = sorted(forbidden.intersection(fields))
        if bad:
            raise ParityError(
                "%s mixes implementation/verification state into Product Truth: %s"
                % (path, ", ".join(bad))
            )
        rows = []
        seen = set()
        for i, raw in enumerate(reader, start=2):
            row = {(k or "").strip().lower(): (v or "").strip() for k, v in raw.items()}
            if not row.get("id") and not row.get("requirement"):
                continue
            rid = row.get("id", "")
            if not rid:
                raise ParityError("line %d: requirement has no id" % i)
            if rid in seen:
                raise ParityError("line %d: duplicate requirement id %s" % (i, rid))
            if not row.get("requirement"):
                raise ParityError("line %d: requirement text is empty" % i)
            seen.add(rid)
            row["line"] = i
            rows.append(row)
    return rows


def load_evidence(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, dict):
        raise ParityError("%s must contain a JSON object" % path)
    reqs = data.get("requirements")
    if not isinstance(reqs, dict):
        raise ParityError("%s has no object field 'requirements'" % path)
    return data.get("revision"), reqs


def score(requirements, evidence):
    counted = []
    skipped = []
    problems = []
    unknown_evidence_ids = sorted(set(evidence) - {r["id"] for r in requirements})
    for rid in unknown_evidence_ids:
        problems.append("evidence exists for unknown requirement %s" % rid)

    for row in requirements:
        scope_status = (row.get("scope_status") or "active").lower()
        if scope_status not in {"active", "deferred", "out_of_scope"}:
            problems.append(
                "line %d: scope_status '%s' is invalid; treated as active"
                % (row["line"], row.get("scope_status", ""))
            )
            scope_status = "active"
        if scope_status != "active":
            item = dict(row, weight=0, status="SKIP", evidence_note="product scope: %s" % scope_status)
            skipped.append(item)
            continue

        prio = row.get("priority", "").lower()
        if prio not in WEIGHT:
            problems.append(
                "line %d: active priority '%s' is not must/should/could; counted as could"
                % (row["line"], row.get("priority", ""))
            )
        weight = WEIGHT.get(prio, 1)
        ev = evidence.get(row["id"])
        if ev is None:
            status = "INCONCLUSIVE"
            note = "no verification evidence"
        elif not isinstance(ev, dict):
            status = "INCONCLUSIVE"
            note = "malformed evidence entry"
            problems.append("%s: evidence entry is not an object" % row["id"])
        else:
            status = str(ev.get("status", "INCONCLUSIVE")).upper()
            note = str(ev.get("notes", "") or "")
            if status not in VALID_STATUS:
                problems.append(
                    "%s: status '%s' is invalid; counted as INCONCLUSIVE"
                    % (row["id"], status)
                )
                status = "INCONCLUSIVE"

        item = dict(row, weight=weight, status=status, evidence_note=note)
        if status == "SKIP":
            skipped.append(item)
        else:
            item["credit"] = CREDIT[status]
            counted.append(item)

    total = sum(r["weight"] for r in counted)
    got = sum(r["weight"] * r["credit"] for r in counted)
    coverage = 100.0 * got / total if total else 0.0

    areas = {}
    for r in counted:
        a = r.get("area") or "(no area)"
        bucket = areas.setdefault(a, [0.0, 0.0, 0])
        bucket[0] += r["weight"] * r["credit"]
        bucket[1] += r["weight"]
        bucket[2] += 1
    by_area = sorted(
        (
            {"area": a, "score": round(100.0 * got_a / total_a, 1) if total_a else 0.0, "requirements": n}
            for a, (got_a, total_a, n) in areas.items()
        ),
        key=lambda d: (d["score"], d["area"]),
    )

    unresolved = [r for r in counted if r["status"] != "VERIFIED"]
    unresolved.sort(
        key=lambda r: (-r["weight"], -CREDIT.get(r["status"], 0.0), r.get("area", ""), r["id"])
    )

    musts = [r for r in counted if r["weight"] == 3]

    def brief(r):
        return {
            "id": r["id"],
            "requirement": r["requirement"],
            "area": r.get("area", ""),
            "priority": PRIORITY_NAME.get(r.get("weight", 1), "could"),
            "status": r.get("status", "INCONCLUSIVE"),
            "notes": r.get("evidence_note", "") or r.get("notes", ""),
        }

    return {
        "verification_coverage": round(coverage, 1),
        "counted": len(counted),
        "must_verified": sum(1 for r in musts if r["status"] == "VERIFIED"),
        "must_total": len(musts),
        "by_area": by_area,
        "unresolved": [brief(r) for r in unresolved],
        "skipped": [brief(r) for r in skipped],
        "problems": problems,
    }


def render(result, revision=None, markdown=False):
    h = "## " if markdown else ""
    out = ["%sVerification coverage: %.1f / 100" % (h, result["verification_coverage"]), ""]
    if revision:
        out.append("revision: %s" % revision)
    out.append(
        "requirements %d counted; must verified %d of %d"
        % (result["counted"], result["must_verified"], result["must_total"])
    )
    out.append("This is evidence coverage, not release authority.")
    out.append("")
    out.append("%sBy area, weakest first" % h)
    if not result["by_area"]:
        out.append("- no scored requirements")
    for a in result["by_area"]:
        out.append("- %-28s %5.1f  (%d requirements)" % (a["area"], a["score"], a["requirements"]))
    out.append("")
    out.append("%sUnresolved verification" % h)
    if not result["unresolved"]:
        out.append("- none")
    for r in result["unresolved"]:
        note = "  (%s)" % r["notes"] if r["notes"] else ""
        out.append("- [%s] %s %s: %s%s" % (r["priority"], r["id"], r["status"], r["requirement"], note))
    if result["skipped"]:
        out.append("")
        out.append("%sExcluded by Product scope or explicit verifier SKIP" % h)
        for r in result["skipped"]:
            out.append("- %s: %s" % (r["id"], r["requirement"]))
    if result["problems"]:
        out.append("")
        out.append("%sEvidence/schema problems" % h)
        for p in result["problems"]:
            out.append("- %s" % p)
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("requirements", help="target requirements CSV")
    ap.add_argument("evidence", help="verifier-owned evidence JSON")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--markdown", action="store_true")
    ap.add_argument("--fail-under", type=float, help="fail on verification coverage below threshold")
    args = ap.parse_args(argv)
    try:
        requirements = load_requirements(args.requirements)
        revision, evidence = load_evidence(args.evidence)
        result = score(requirements, evidence)
    except (ParityError, OSError, ValueError, json.JSONDecodeError) as exc:
        print("parity: %s" % exc, file=sys.stderr)
        return 2
    if args.json:
        payload = dict(result)
        payload["revision"] = revision
        print(json.dumps(payload, indent=2))
    else:
        print(render(result, revision=revision, markdown=args.markdown))
    if args.fail_under is not None and result["verification_coverage"] < args.fail_under:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
