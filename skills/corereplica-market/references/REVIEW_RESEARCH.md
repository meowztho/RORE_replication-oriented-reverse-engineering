# Review Research

Collect feedback only from allowed/public sources or user-provided data. Preserve source URL, date and text/quote provenance.

## Sampling

Prefer several source families and recent material where available: official app stores/feeds, reputable review platforms, public community discussions, public feature-request boards and changelogs. Do not scrape against terms or invent access that is unavailable.

A large sample is useful, not a magic threshold. Report actual sample size, source mix, date range and obvious bias. Deduplicate copied/reposted text.

## Analysis

Separate:

- complaint themes;
- explicit feature requests;
- praise/retention drivers;
- severe unthemed reports;
- whole-job/audience gaps;
- items already fixed in newer releases;
- sample-size/source-bias caveats.

Use the bundled `reviews.py` only on a legitimately assembled review CSV. Its theme counts/weights are heuristic evidence, not a statistically representative market survey unless the sample actually supports that claim.

For each proposed opportunity, retain the evidence count/source mix and representative linked quotes internally for research. Do not reuse third-party reviewer quotes as your product's testimonials.

Route any actual scope change through `corereplica-product`; market evidence proposes, Product Truth decides.
