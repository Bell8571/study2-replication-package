# Study 2 v1.0 — Addendum 04: effective-gate definition

**Status:** locked (read-only). This addendum is not an edit to the frozen protocol or to earlier addenda.

**Addendum date:** 24 November 2026 (America/Chicago)

**Frozen protocol:** `PROTOCOL-v1.0.md` (SHA-256 `6d47296879bf9f102ff76b5eb754a43f12a98e6b8bb170d50bece614d9372741`)  
**Earlier addenda (unchanged):** `ADDENDUM-01-seeds.md` (SHA-256 `29339ca743ececc39b440147a9ecdfca53b790478ff23e5ac0ac58bac2c589ac`); `ADDENDUM-02-deviation-job-check-cap.md` (SHA-256 `40f2d98d03531e79032975b77721135cbc84cdd473964ea20dcd4a96a66b0ae8`); `ADDENDUM-03-protocol-gap-rulings.md` (SHA-256 `a7bd51c8dc75288019c36784609083e2ba622fdadd70986d7d41f2c89c80767a`)  
**Pre-adjudication IRR results (unchanged, on record):** `IRR-RESULTS-PRE-ADJUDICATION.md` in commit `ba1881dd9570de2b062580536a6af45da58272d9` (`ba1881d`)

Jason approved this definition and the procedure below (t51u, 24 November 2026).

This addendum does not change families, the observation window, seeds, the official sample, or the IRR subsample already drawn. It does not recode any unit or run. It states an operational definition of an effective gate for frozen §5.1, a sub-tag to be recorded on guarded units, and the procedure for a later recode and a later fresh blind IRR pass.

---

## 1. Why this addendum exists

Frozen §11 requires a stop-and-revise of the rubric before any public claim when raw agreement is below the stated threshold (or when both Gwet's AC1 and PABAK are below the stated threshold). Pre-adjudication AI-versus-AI agreement on the official IRR overlap was below that §11 threshold. The measures, confusion matrices, and the isolation of the disagreement in the §5.1 gate / untrusted-path definition are on record in `IRR-RESULTS-PRE-ADJUDICATION.md` at `ba1881d`, which remains frozen and is not edited by this addendum.

This addendum closes that definitional gap. It does not itself apply the definition to the official sample.

---

## 2. Operational definition of an effective gate

For Study 2, a mechanism is an **effective gate** when it is one of the following and the evidence requirements for that mechanism are met. Mechanisms may co-occur. Record every mechanism that applies.

A mechanism is judged **per in-scope trigger** (the outsider-authored event types in frozen §3 / §5.3 that can invoke the agent job). If a check exists on some triggers but a different in-scope trigger bypasses it — for example the `if:` is absent on a second job, a second workflow event path, or a step that still invokes the agent — the mechanism is **not effective for that trigger**.

Bucket 1 requires that **at least one effective mechanism covers every in-scope trigger**. If any in-scope trigger is left uncovered, the unit is Bucket 2a (provided the other §5.1 conditions for 2a hold), not Bucket 1.

### (a) Documented vendor write-access default, verified as active

The packaged Action (or equivalent vendor entrypoint) documents, at the version the workflow actually pins or resolves, a default write-access or "write users only" check that withholds the agent from actors who lack write permission.

**Verified as active** requires all of the following, from public artifacts only:

1. The documented default is that of the action version in use (the pin, SHA, or tag in the workflow, or the resolved action SHA in the job log when the workflow uses a moving tag).
2. The workflow does not pass an input or setting that disables or widens the default (including, where the vendor documents it, `allowed_non_write_users: "*"` or an equivalent opt-out or wildcard).
3. There is no visible bypass of the default on this unit (for example a documented bot or app exception that the workflow relies on, or a template or bot that auto-satisfies the check).
4. Public artifacts show the check is in play: either the job log shows the action running the write-access check, or the pinned action's documented default applies and no override or bypass is present.

This mechanism is not limited to a single vendor family. Any vendor default that meets the same four points counts.

### (b) Explicit actor, association, allow-list, or same-repo check that actually restricts the active trigger surface

The workflow YAML, or a script the workflow invokes as part of the agent job, contains an explicit check on `author_association`, actor login, an allow-list, collaborator or owner equality, or a same-repository / non-fork / non-bot condition.

**Evidence requirements:**

1. The check is present in the public workflow file or in a script called on the path that can invoke the agent.
2. The check applies to the **job or step that invokes the agent**, not only to an unrelated job.
3. The check actually restricts the **in-scope trigger under review**: it is on the control-flow path that can start the agent for that event. A check that applies only to `issue_comment` does not, by itself, cover a `pull_request` path that skips it.
4. The check is not visibly defeated in the sense of frozen §5.4 `gate_present_but_ineffective` (for example a template or bot applies a required label; `allowed_non_write_users: "*"`; a documented bot or app bypass).

Platform behavior that withholds secrets from fork pull requests is not, by itself, mechanism (b), unless the workflow also contains an explicit same-repo or non-fork check that meets the points above.

### (c) Zero untrusted event-text path into the prompt or runtime context

No untrusted event-derived text has a path into the agent for the in-scope trigger under review.

**Event-derived text does not reach** any of: the agent prompt; an argument the agent is documented to read; an environment variable that feeds the agent; a file the workflow writes or the agent is instructed to read (including a workflow-fetched comments or issue file); or other runtime context supplied to the agent.

**Evidence requirements:**

1. The workflow YAML does not interpolate event fields (for example `github.event.issue.body`, a comment body, a PR title, or a fork commit message) into those channels.
2. A pinned action default does not load the triggering comment or body unless the workflow overrides that default so that it does not.
3. The job does not, on this trigger, fetch event text at runtime and hand it to the agent (for example `gh issue view`, a checkout of an untrusted ref used as prompt context, or writing `pr_comments.json` and telling the agent to read it).
4. Public job logs, where they echo the prompt or input context, are consistent with that reading.

Addendum 03 ruling 3 remains in force: a packaged Action step invoked without interpolating event text, and without a documented default that loads the triggering comment or body, is not wired. Mechanism (c) is the corresponding static-gate form of that fact, and it must be assessed for every in-scope trigger, including runtime fetches the YAML arranges.

---

## 3. Sub-tags on guarded units

When a unit is coded Bucket 1 under this definition, record how it is guarded.

| Column | Values | Meaning |
|---|---|---|
| `gate_mechanism` | `a`, `b`, `c`, or a combination in that letter order, joined by `+` (`a+b`, `a+c`, `b+c`, `a+b+c`) | Every mechanism that is effective on this unit. List all that apply, not only the primary one. |
| `gate_mechanism_evidence` | free text | The public-artifact basis for each listed mechanism (action version and default, the YAML or script check and which triggers it covers, and/or why no event-text path exists). Note any in-scope trigger that a given mechanism does not cover, and which other listed mechanism covers it. |

Partial coverage is recorded in the evidence field. It does not by itself make the unit Bucket 1. If any in-scope trigger lacks an effective mechanism, the unit is Bucket 2a and `gate_mechanism` is left blank (or is not treated as a guard tag).

These columns do not replace the frozen rubric fields. They are additional sub-tags so that a later revised RQ3 static residual can be shown with a breakdown by mechanism.

---

## 4. Procedure after this addendum is recorded

The following steps are **not** performed by this addendum. They follow it, in this order:

1. **Payload audit.** A harvest-payload audit of all 135 official executed runs is recorded with this addendum. Raw harvest files are not overwritten. Aggregate findings are in `PAYLOAD-AUDIT.md`. The identifying run-level table stays on the collection box. Later recoding should use the audit, the run logs, `runs_full`, and later public fetches, and must not treat a harvest payload as authoritative when the audit classifies it as a mismatch or as missing.
2. **Primary recode.** The primary coder recodes all 36 official draw units (and their official executed runs) under this addendum and under the frozen protocol and Addenda 01–03. The locked first-pass sheet (`coding_sheet_LOCKED_v1.csv`) remains frozen on record and is not overwritten. The recode is a new sheet.
3. **Fresh blind IRR.** A fresh second coder, working from a new blind packet, scores the same deterministic 12-unit / 42-run IRR sample. The official IRR seed string and `IRR-SAMPLE-MANIFEST.md` are unchanged. The fresh coder must not be given this addendum's later recode outcomes, the first-pass codes, or `IRR-RESULTS-PRE-ADJUDICATION.md` as a key. This addendum and the frozen protocol and earlier addenda are the rubric.
4. **Record.** Pre-adjudication results at `ba1881d` stay on record. Frozen §11 metrics (raw agreement, Cohen's kappa, PABAK, Gwet's AC1, the kappa-paradox flag, and the required tag tables) are recomputed on the new recode and the fresh blind codes, still labeled AI-versus-AI if both coders are AI systems. No kappa gate is applied.

---

## 5. What this addendum does not change

- The frozen protocol file and Addenda 01–03 are not edited and remain mode 0444.
- `IRR-RESULTS-PRE-ADJUDICATION.md` and commit `ba1881d` remain on record and are not edited.
- Official seeds, the official 36-unit sample, and the IRR sample already drawn are unchanged.
- No unit or run is recoded in this addendum.
