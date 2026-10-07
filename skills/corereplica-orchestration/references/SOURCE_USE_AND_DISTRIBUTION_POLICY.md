# Reference Source, Use, Retention, and Distribution Policy

CoreReplica separates **access/analysis** from **retention**, **project/VCS sharing**, and **target-product inclusion and distribution**. Material being technically visible, inspectable, transformable, or reusable does not by itself authorize keeping, committing, shipping, or redistributing it.

## Source eligibility

A source or material may be used only within the user's actual authorization and applicable terms. Relevant inputs may include:

- public product/help/pricing/changelog/store pages and public documentation;
- publicly available walkthroughs/reviews and public API documentation;
- screenshots, recordings, files or other material supplied by the user;
- the user's own authorized account used within its permitted scope;
- user-controlled local installations, files, artifacts, source, binaries, assets or data when the user is entitled to access/use them for the task;
- open, public-domain, owned or licensed material according to its applicable terms.

## General rule

For every material input, keep these decisions separate when they differ:

```text
may access / inspect / analyze / transform for this task
!=
may retain locally after the active work
!=
may place in durable project/control workspace
!=
may share/commit through VCS or collaboration systems
!=
may include in the target product
!=
may redistribute / publish / sublicense in the release
```

1. Use only authorized sources and methods. Do not bypass authentication, paywalls, DRM/access controls, rate limits or ownership checks, and do not use another person's credentials/account without authorization.
2. Preserve provenance and any material usage, license, confidentiality, privacy, retention, sharing or redistribution constraint when it can affect later handling.
3. Local analysis, compatibility work, conversion or transformation may use authorized material without making that material durable project truth or part of the shipped product.
4. If material is `local-only`, ephemeral, confidential, privacy-sensitive or otherwise non-shareable, keep it out of version control and collaboration systems unless a separate basis permits that sharing. A path under the repository root does not grant VCS authority.
5. Include or redistribute third-party material only when there is a documented basis that covers the intended use, such as ownership, a compatible license, explicit permission or public-domain status.
6. If inclusion/distribution rights are unclear, treat the material as reference/input only, keep the uncertainty explicit, and use an independent/open/licensed replacement for the release rather than assuming permission.
7. Do not infer that technical visibility of private/internal APIs, implementation details, credentials or restricted data authorizes copying, depending on, publishing or redistributing them. Use public/authorized contracts where the target product needs an integration.
8. Trademarks, logos, proprietary media, text/copy, catalogs and other protected content follow the same rule: access for an authorized task does not itself grant retention, sharing, target-product or redistribution rights.

When useful, a source record may note compact handling constraints such as `retention=ephemeral|local-only|project`, `vcs=forbidden|allowed`, `target_inclusion=forbidden|allowed|conditional`, and `redistribution=forbidden|allowed|conditional`. Do not build a general rights-management system merely to encode these fields.

When applicable terms materially restrict the intended use, record that constraint and adjust the source/use path instead of silently overriding it. This procedure is not legal advice.
