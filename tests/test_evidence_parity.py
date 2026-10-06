import csv
import io
import json
import os
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr

from _load import load

parity = load("corereplica-verify", "parity")


REQS = [
    ["REQ-001", "booking", "Guest can book a slot", "must", "adopt", "REF-1", "Booking succeeds", ""],
    ["REQ-002", "booking", "Guest can reschedule", "must", "adopt", "REF-2", "Reschedule persists", ""],
    ["REQ-003", "notifications", "Host gets reminder", "should", "target-only", "", "Reminder delivered", ""],
    ["REQ-004", "sharing", "Share link can be copied", "could", "adapt", "REF-4", "Copy action exposes URL", ""],
]
HEADER = ["id", "area", "requirement", "priority", "source_decision", "reference_ids", "acceptance", "notes"]


def write_csv(path, header=HEADER, rows=REQS):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)


def write_json(path, data):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh)


class EvidenceParity(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.req = os.path.join(self.tmp.name, "requirements.csv")
        self.ev = os.path.join(self.tmp.name, "evidence.json")
        write_csv(self.req)
        write_json(self.ev, {
            "revision": "abc123",
            "requirements": {
                "REQ-001": {"status": "VERIFIED", "evidence": [{"kind": "runtime"}]},
                "REQ-002": {"status": "PARTIAL", "notes": "persistence not re-opened"},
                "REQ-003": {"status": "FAILED", "notes": "no email"},
                # REQ-004 intentionally has no evidence -> INCONCLUSIVE
            },
        })

    def tearDown(self):
        self.tmp.cleanup()

    def test_score_comes_from_verification_evidence(self):
        reqs = parity.load_requirements(self.req)
        revision, ev = parity.load_evidence(self.ev)
        result = parity.score(reqs, ev)
        # weights = 3+3+2+1 = 9; credit = 3 + 1.5 = 4.5
        self.assertEqual(revision, "abc123")
        self.assertAlmostEqual(result["verification_coverage"], 50.0)
        self.assertEqual((result["must_verified"], result["must_total"]), (1, 2))
        by_id = {x["id"]: x for x in result["unresolved"]}
        self.assertEqual(by_id["REQ-004"]["status"], "INCONCLUSIVE")

    def test_requirement_schema_rejects_builder_status_columns(self):
        bad = os.path.join(self.tmp.name, "bad.csv")
        write_csv(bad, header=["id", "requirement", "priority", "clone"],
                  rows=[["REQ-1", "Thing", "must", "yes"]])
        with self.assertRaises(parity.ParityError) as ctx:
            parity.load_requirements(bad)
        self.assertIn("mixes implementation/verification state", str(ctx.exception))

    def test_unknown_evidence_is_reported(self):
        reqs = parity.load_requirements(self.req)
        _, ev = parity.load_evidence(self.ev)
        ev["REQ-999"] = {"status": "VERIFIED"}
        result = parity.score(reqs, ev)
        self.assertTrue(any("REQ-999" in p for p in result["problems"]))

    def test_skip_is_not_scored(self):
        write_json(self.ev, {
            "revision": "abc123",
            "requirements": {
                "REQ-001": {"status": "VERIFIED"},
                "REQ-002": {"status": "SKIP"},
                "REQ-003": {"status": "VERIFIED"},
                "REQ-004": {"status": "VERIFIED"},
            },
        })
        result = parity.score(parity.load_requirements(self.req), parity.load_evidence(self.ev)[1])
        self.assertEqual(result["counted"], 3)
        self.assertEqual([x["id"] for x in result["skipped"]], ["REQ-002"])
        self.assertEqual(result["verification_coverage"], 100.0)

    def test_render_never_claims_shippable(self):
        result = parity.score(parity.load_requirements(self.req), parity.load_evidence(self.ev)[1])
        text = parity.render(result, revision="abc123")
        self.assertIn("not release authority", text.lower())
        self.assertNotIn("shippable", text.lower())

    def test_cli_fail_under_and_json(self):
        with redirect_stdout(io.StringIO()):
            self.assertEqual(parity.main([self.req, self.ev, "--fail-under", "60"]), 1)
            self.assertEqual(parity.main([self.req, self.ev, "--fail-under", "40"]), 0)
        buf = io.StringIO()
        with redirect_stdout(buf):
            self.assertEqual(parity.main([self.req, self.ev, "--json"]), 0)
        data = json.loads(buf.getvalue())
        self.assertEqual(data["revision"], "abc123")

    def test_missing_columns_exit_2(self):
        bad = os.path.join(self.tmp.name, "bad2.csv")
        with open(bad, "w") as fh:
            fh.write("id,area\nREQ-1,x\n")
        with redirect_stderr(io.StringIO()):
            self.assertEqual(parity.main([bad, self.ev]), 2)


if __name__ == "__main__":
    unittest.main()
