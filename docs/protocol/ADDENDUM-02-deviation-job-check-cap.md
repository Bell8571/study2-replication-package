# Study 2 v1.0 — Addendum 02: deviation note on the job-check coverage cap

**Status:** locked (read-only). This addendum is not an edit to the frozen protocol or to ADDENDUM-01.

**Addendum date:** 24 November 2026 (America/Chicago)

**Frozen protocol:** `PROTOCOL-v1.0.md` (SHA-256 `6d47296879bf9f102ff76b5eb754a43f12a98e6b8bb170d50bece614d9372741`)  
**Seeds addendum:** `ADDENDUM-01-seeds.md` (SHA-256 `29339ca743ececc39b440147a9ecdfca53b790478ff23e5ac0ac58bac2c589ac`), unchanged  
**Protocol anchor:** [Bell8571/study2-untrusted-input-reach](https://github.com/Bell8571/study2-untrusted-input-reach) @ `365afa938edabc272133037da60dc38c8eb9e9cb` (the official-draw summary commit, before this note)

Jason approved recording this as a deviation note (t45u, 24 November 2026).

This file does not change buckets, families, the observation window, seeds, or any other frozen rule. It records how a coverage cap was applied during the official walk.

---

## 1. What happened

When the official draw checked whether a candidate had executed (not skipped) agent-job runs in the observation window, the walk inspected **up to 80** non-skipped runs' jobs per candidate (`JOB_CHECK_SOFT_CAP = 80` in the walk script). If five executed agent-job runs had not been found by then, the walk stopped job-checking that candidate and, if no executed run had been found, excluded it with the reason `zero-executed-runs-within-coverage-cap`.

Study 1 used a tighter bound: **25 job checks** and **10 run-listing pages**. Frozen Study 2 v1.0 does not fix either number. It only requires that a cap, if used, be logged as a coverage cap, not as a demonstrated zero-executed result. The binding sentence (PROTOCOL-v1.0.md, immediately after the n and run-count bullets in §10.2) is, verbatim:

> A 25-job-check / 10-page run-listing cap, if used again, must be logged as a coverage cap (Study 1 D9 / skip-register v2 lesson), not as a demonstrated zero-executed result.

The official Study 2 walk also listed up to **20** pages of 100 completed in-window runs (a looser listing bound than Study 1's 10 pages). That listing bound is recorded here for completeness; the deviation Jason approved is the **job-check** cap of 80 versus Study 1's 25.

---

## 2. Exact counts from the official walk log

Source: `/workspace/study2-scoping/collection/draw/walk_log.jsonl` (official walk; contrast-preverify rows excluded). The count is units whose recorded walk decision is `excluded` with reason `zero-executed-runs-within-coverage-cap`. Every such unit has `runs.coverage_cap = true`, `runs.job_checked = 80`, and `runs.n_executed = 0`.

**Total: 12.** This matches the count in the notes (12). There is no discrepancy.

| Family | Units excluded at the 80-job-check cap |
|---|---:|
| claude | 1 |
| codex | 9 |
| gemini | 1 |
| codex-cli | 0 |
| gemini-cli | 0 |
| claude-cli | 1 |
| **Total** | **12** |

These 12 exclusions are **coverage caps, not demonstrated zero-executed results**. In each case, further non-skipped runs remained un-checked (or the agent job was not identified in the 80 checked runs). A later executed agent job, if any, was not observed.

---

## 3. Likely direction of the effect

A higher job-check cap can only *include* candidates that a 25-check cap would have left unresolved or excluded. It cannot exclude a unit that would have been sampled under 25. The higher cap therefore tends to admit more candidates that show an executed agent job only after many non-executed or unidentified job checks — a thicker tail than Study 1's 25-check rule. Direct comparability with Study 1's eligibility rate is imperfect for that reason.

The 12 units excluded at 80 would also have been excluded at 25: no executed agent job was found in 80 checks, so none was found in the first 25. The cap difference does not change those 12 outcomes. Any effect on the official sample would be additional inclusions among candidates that first show an executed run after the 25th job check.

---

## 4. Sensitivity: drawn units under a 25-job cap

This section uses only recorded fields on the 36 official sampled units (`runs.job_checked`, `n_executed`, `runs.skipped_over_after_job_check`, `runs.unidentified_agent_job`). No new GitHub queries were made.

- For **34 of 36** drawn units, `job_checked` was ≤ 25. Those units would still have been eligible under a 25-job cap (at least one executed agent job was found within 25 checks).
- For **2 of 36** drawn units (both in the Codex family), `job_checked` was greater than 25 (48 checks with 3 executed and 45 unidentified agent jobs; and 38 checks with 1 executed and 37 unidentified agent jobs). The walk log does not record *which* of those checks first found an executed agent job. The latest possible position of the first executed check is `job_checked - n_executed + 1` (46 and 38 respectively), which is after 25, so a 25-cap *might* have excluded either unit — or might still have included it, if the first executed job occurred at or before check 25. That cannot be determined from the recorded data without new queries, which were not run.

So the sensitivity result is a bound, not a point count: **at most 2** official drawn units (both Codex) could have failed a 25-job eligibility cap; **34** would still have been drawn; the number that actually would have failed is unknown from the recorded check-order.

---

## 5. What this addendum does not change

- The frozen protocol file and ADDENDUM-01 are not edited and remain mode 0444.
- The official sample, seeds, and digest formula are unchanged.
- The 12 cap exclusions remain coverage caps in the walk log. They must not be treated as demonstrated zeros in rates or in coding.
- The IRR subsample is still drawn only after the coding lock.
