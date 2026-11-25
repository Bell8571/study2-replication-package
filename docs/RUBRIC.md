# Rubric index and codebook

This file was written for the replication package. It is **not** a protocol document and adds no rules. The binding rules are in the frozen protocol and the addenda in `docs/protocol/` and `docs/redacted/`. This file says where each rule lives and defines every column in `data/`.

## Where the rubric lives

| Rule | Location |
|---|---|
| Bucket definitions 1 / 2a / 2b / 3 and unit precedence 3 > 2b > 2a > 1 | `PROTOCOL-v1.0.md` §5.1–§5.2 |
| `event-verified_not_log-confirmed` sub-status (ceiling) | §5.3 |
| Tags (`route`, `-inj`, `workspace_poison`, `mcp_client_config`, `gate_present_but_ineffective`, `dispatch`) | §5.4 |
| Logs that do not show the input; coverage gaps | §6 |
| Log-confirmed ingestion test | §7 |
| Author association and the primary outsider set; `CONTRIBUTOR` sensitivity | §8, and decision 3 in §0 |
| Privileged actuation (Bucket 3) from public timelines | §9 |
| Sampling, window, and IRR procedure | §10–§11; seeds in Addendum 01 (redacted); job-check cap deviation in Addendum 02 |
| Unassociated bots; Claude default write-access gate; unwired Codex steps | `ADDENDUM-03` rulings 1–3 |
| Effective-gate definition: mechanisms (a), (b), (c) | `ADDENDUM-04` §2 |
| Vendor default behaviours relied on for mechanism (a) | `TOOL-REFERENCE-SHEET.md` |

Two later rulings, the t57u adjudication (`ae059a4`) and the t61u consistency ruling (`cacd05b`), applied Addendum 4 §2(c)(3) to individual units. Their documents are withheld (see `README.md`), but their effects are visible in the `adjudication` column of `data/units.csv`, and the stage columns let anyone trace every change.

## Mechanism tags

| Data value | Addendum 4 | Manuscript name |
|---|---|---|
| `vendor_default` | (a) documented vendor write-access default, verified active | vendor_default |
| `explicit_check` | (b) explicit actor / association / allow-list / same-repo check | explicit_check |
| `no_prompt_path` | (c) no untrusted event-text path into prompt or runtime context | no_prompt_path |

Combined tags are joined with `+`. Mechanism tags exist only from the Addendum 4 recode onward. Pass 1 had no mechanism field.

## Coding stages (column prefixes)

| Prefix | Stage | Archive anchor |
|---|---|---|
| `pass1_` | Primary coding locked before IRR (Pass 1) | `ba1881d` |
| `v2_locked_` | Primary recode under Addendum 4, locked before the v2 blind coder's results were seen | `fc856e7` |
| `post_adj_v1_` | After t57u adjudication | `ae059a4` |
| `final_` | After t61u consistency ruling (final) | `cacd05b` |

## `data/units.csv`

| Column | Meaning |
|---|---|
| `unit_label` | Random pseudonym U01–U36 (no relation to any identifier or to the manuscript's 8-hex IDs) |
| `family`, `stratum` | Agent family label; `packaged` Action vs `contrast` CLI |
| `has_in_scope_outsider_trigger` | Workflow `on:` includes at least one outsider-authorable event (pull_request, pull_request_target, issues, issue_comment, pull_request_review, pull_request_review_comment, discussion, discussion_comment) |
| `*_unit_bucket` | Unit roll-up bucket at each stage |
| `*_gate_mechanism` | Addendum 4 mechanism tags for guarded units (blank if not guarded) |
| `adjudication` | `t57u`, `t61u`, or `none`: whether a later ruling touched this unit's runs |
| `strict_bound_harness_checkout` | `true` for the unit kept guarded under t57u ruling 2 (fork checkout feeds validation/test tooling, not the agent prompt). The strict bound counts it as exposed |
| `irr_sample` | `selected` (in the 12-unit blind IRR overlap), `remainder` (non-Bucket-1 at lock but beyond the cap of 12), `not_drawn` |
| `n_runs_harvested`, `n_runs_scorable` | Runs harvested, and runs with a non-empty log |
| `final_runs_b1` … `final_runs_b3` | Scorable runs by final run-level bucket |
| `runs_*` | Scorable-run counts for the sensitivity flags defined below |

## `data/runs.csv`

| Column | Meaning |
|---|---|
| `run_label` | Random pseudonym R001–R135 |
| `event` | Triggering event type |
| `scorable` | `false` only for the one empty-log coverage gap |
| `association` | Author association of the triggering content (`n/a` for events with none, e.g. push, schedule, workflow_dispatch) |
| `actor_type` | `User` or `Bot` |
| `*_bucket` | Run-level bucket at each stage (blank for the unscorable run) |
| `outsider_primary` | Triggering author is in the primary outsider set (human; §8 and Addendum 03 ruling 1) |
| `outsider_contributor_sensitivity` | Triggering association is `CONTRIBUTOR` (sensitivity row only) |
| `contributor_log_confirmed` | A `CONTRIBUTOR` run whose triggering text was log-confirmed in the agent input (counts toward the `CONTRIBUTOR`-relaxed reach only) |
| `log_confirmed`, `event_verified` | §7 log-confirmed ingestion of primary-outsider text; §5.3 event-verified-not-log-confirmed |
| `bot_sensitivity` | Bot actor with association `NONE` (Addendum 03 ruling 1) |
| `contributor_write_access_unverified` | `CONTRIBUTOR` run whose write access was not independently verified (Addendum 03 ruling 2) |
| `route`, `workspace_poison`, `dispatch_tag` | §5.4 tags |
| `coverage_gap_empty_log` | Empty (22-byte) log archive: a coverage gap, not a null |

## `data/irr_pass{1,2}_*.csv`

Primary (non-blind) and blind second-coder codes for the same 12 units and 42 runs. Pass 1 used blind coder v1 against the Pass 1 lock. Pass 2 used blind coder v2 against the Addendum 4 recode lock. Both comparisons are pre-adjudication. `*_route` uses `none` for no route tag, and `*_event_verified_not_log_confirmed` is derived from the sub-status field.
