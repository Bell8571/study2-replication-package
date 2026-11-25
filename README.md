# Study 2 replication package — static configuration exposure vs. observed runtime outsider reach in public GitHub Actions coding agents

Companion package for: Jason Bell, *Static Configuration Exposure vs. Verified Runtime Outsider Reach in Public GitHub Actions Coding Agents (Study 2)*, 2026.

> **Status: PRIVATE REVIEW DRAFT.** Built for the author's review before any public release.

## What the study is

Study 2 asks how often untrusted outsider text (from issues, pull requests, comments, reviews, or fork-commit metadata) actually reached a write-capable or secret-holding AI coding agent in public GitHub Actions runs that had already executed. It also measures how much of the static-configuration exposure reported by earlier YAML-level work still shows up in this sample (RQ3, labelled as a replication). The sample is a seeded draw of **36 workflow units** with **135 harvested runs** (134 scorable). It covers the packaged Claude, Codex, and Gemini Actions plus a CLI contrast stratum.

The study was passive and used public data only. No writes were made to third-party repositories, no workflows were triggered, no test issues or pull requests were opened, and there was no live injection. The write-up is **aggregate-only** and names no repositories.

## What is in this package

| Path | Contents |
|---|---|
| `docs/protocol/PROTOCOL-v1.0.md` | Frozen v1.0 protocol (byte-identical to the frozen file) |
| `docs/protocol/ADDENDUM-02…`, `ADDENDUM-03…`, `ADDENDUM-04…` | Dated addenda (byte-identical) |
| `docs/redacted/ADDENDUM-01-seeds.REDACTED.md` | **Redacted derivative** of Addendum 01. The seed strings are withheld (see below). |
| `docs/protocol/TOOL-REFERENCE-SHEET.md` | Vendor-documentation reference used when coding vendor default gates |
| `docs/RUBRIC.md` | Index of the coding rubric (where each rule lives) and the codebook for every data column |
| `data/units.csv` | 36 pseudonymized units (`U01`–`U36`): family, stratum, bucket at each stage, gate-mechanism tags, run counts per bucket, sensitivity counts, IRR-sample membership |
| `data/runs.csv` | 135 pseudonymized runs (`R001`–`R135`): event type, author association class, bucket at each stage, sensitivity flags, tags |
| `data/irr_pass{1,2}_{units,runs}.csv` | Primary and blind second-coder codes for the 12-unit / 42-run IRR overlap |
| `scripts/` | Python 3 standard-library scripts that recompute every headline figure and IRR statistic |
| `results/` | Outputs of the scripts as committed |
| `PROVENANCE.md` | Per-file SHA-256 manifest citing the four archive commits `ba1881d`, `fc856e7`, `ae059a4`, `cacd05b` |
| `SHA256SUMS` | Checksums of every file in this package |

## Reproduce

Requires Python ≥ 3.8 and nothing else.

```sh
python3 scripts/verify_checksums.py     # package integrity against SHA256SUMS
python3 scripts/reproduce_aggregates.py # Table 1, abstract, conclusion → results/aggregates.json
python3 scripts/reproduce_irr.py        # Table 2 (kappa / PABAK / Gwet AC1) → results/irr_pass{1,2}.json
python3 scripts/check_paper_values.py   # asserts every reproduced number equals the manuscript (exit 0)
```

The agreement statistics follow the conventions documented in `scripts/agreement.py`. The category set is fixed, including categories that no rater used. Kappa is reported as 1 when chance agreement and observed agreement both equal 1. PABAK = (k·pₒ − 1)/(k − 1), and AC1 is Gwet's first-order coefficient. The study's original agreement computation was not kept as a standalone script. These scripts reimplement it, and they were checked against the archived metric records: for every bucket, reach, and exposure statistic in both passes, the counts, κ, PABAK, AC1, and both chance terms differ from the archived values by no more than 1e-9.

### Headline figures the scripts reproduce

| Measure | Value |
|---|---|
| Final unit buckets 1 / 2a / 2b / 3 | 31 / 4 / 1 / 0 |
| Final scorable-run buckets 1 / 2a / 2b / 3 | 120 / 13 / 1 / 0 |
| RQ3 static-config residual | 5/36 units (13.9%), 14/134 runs (10.4%) |
| Strict bound (validation/test-harness checkout counted as exposed) | 6/36 units, 16/134 runs |
| Observed primary-outsider reach (floor = ceiling) | 1/36 units, 1/134 runs; 0 Bucket 3 |
| `CONTRIBUTOR` sensitivity | reach 6/134 runs, 2/36 units; 0 Bucket 3 |
| Pass 1 IRR (units / runs, 4-way) | 25.0% κ 0.107 / 26.2% κ 0.038 |
| Pass 2 IRR (units / runs, 4-way) | 83.3% κ 0.667 / 92.9% κ 0.835 |
| Guarded units never second-coded | 23 of 31 |

Bucket labels follow the protocol (1 = guarded, 2a = config-only exposure, 2b = log-confirmed reach, 3 = privileged actuation). The manuscript's tiers map to them as Tier 2b = Bucket 2a, Tier 3 = Bucket 2b, and Tier 5 = Bucket 3. Tier 4, the event-verified ceiling, is a reporting bound.

## What is withheld, and why

The protocol (§12) commits the public write-up to aggregate reporting that never lists unpatched repositories. This package therefore leaves out the following:

- **Repository, owner, and workflow identifiers.** That covers repository and owner names, workflow paths and URLs, run and job IDs, actor logins, issue and PR numbers, commit SHAs of third-party repositories, run timestamps, log-archive digests, and repository covariates (stars, forks, velocity).
- **Raw logs, event payloads, log excerpts, and payload text**, plus the free-text coder notes and evidence fields, which quote them.
- **The sample and IRR seed strings.** The sample digest is SHA-256 of `study2-v1.0|<seed>|<owner/repo>|<path>`. With the seed, anyone could re-run the seeded walk over public workflows and recover the sampled repositories. Addendum 01 is therefore published only as a clearly labelled redacted derivative. The frozen original is unedited, and its checksum is in `PROVENANCE.md`.
- **The archive's interim narrative reports** (draw, harvest, sanity, coding-pass, lock, IRR, recode, adjudication, and consistency documents). They identify units by SHA-256 hashes of the repository/workflow path, and some list run IDs. Their checksums at each cited commit are in `PROVENANCE.md`, and every figure they report can be recomputed from the tables here.
- **Unit pseudonyms.** The labels `U01`–`U36` and `R001`–`R135` were assigned by a cryptographically random shuffle. They are not derived from any identifier, and the mapping exists only in the author's private archive.

**Identifying data is available to vetted reviewers on request from the author** (for example, artifact-evaluation committees, or researchers coordinating disclosure). It is shared under an agreement not to republish repository identities.

## Provenance

The analysis was recorded in a private, append-only archive repository. Frozen files were never edited in place, and every correction was made through a new dated file. `PROVENANCE.md` cites four commits: `ba1881d` (Pass 1 IRR), `fc856e7` (Pass 2 IRR under Addendum 4), `ae059a4` (adjudication), and `cacd05b` (consistency ruling, final state). It gives the SHA-256 of every file at each of those commits, shows which ones are included here verbatim or as a redacted derivative, and confirms that the withheld coding sheets still match the checksums recorded at those commits. This package has its own history. The cited commits are references, not live commits in this repository.

## Licence

Documentation and data are released under CC BY 4.0 (`LICENSE-DATA`), and scripts under the MIT License (`LICENSE`).

## Acknowledgments

AI research assistance (Liz Lopez) handled log harvesting, integrity checks, primary coding, the blind second-coder passes, and assembly of this package. All of it ran under the author's protocol governance, and the author made the final adjudication rulings.
