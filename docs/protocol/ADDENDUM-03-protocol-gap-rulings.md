# Study 2 v1.0 — Addendum 03: protocol-gap rulings

**Status:** locked (read-only). This addendum is not an edit to the frozen protocol or to earlier addenda.

**Addendum date:** 24 November 2026 (America/Chicago)

**Frozen protocol:** `PROTOCOL-v1.0.md` (SHA-256 `6d47296879bf9f102ff76b5eb754a43f12a98e6b8bb170d50bece614d9372741`)  
**Earlier addenda (unchanged):** `ADDENDUM-01-seeds.md` (SHA-256 `29339ca743ececc39b440147a9ecdfca53b790478ff23e5ac0ac58bac2c589ac`); `ADDENDUM-02-deviation-job-check-cap.md` (SHA-256 `40f2d98d03531e79032975b77721135cbc84cdd473964ea20dcd4a96a66b0ae8`)  
**Protocol / first-pass anchor:** [Bell8571/study2-untrusted-input-reach](https://github.com/Bell8571/study2-untrusted-input-reach) @ `7f32554d3c18f9029ed32ffa344e0f7891d71406` (the first coding-pass summary commit, before this addendum)

Jason approved all three rulings, word for word (t48u, 24 November 2026).

These rulings close three gaps noted in the first coding pass (`CODING-PASS-SUMMARY.md`). They were **applied after the first pass and before the coding lock**. They do not change buckets, families, the observation window, seeds, or any other frozen rule. They only say how to apply the frozen text where it is silent or needs an explicit choice.

---

## 1. The rulings (verbatim)

Jason's approved text, quoted in full:

> 1. Unassociated bots: Count humans only in the primary outsider rate and report bots in a separate sensitivity row.
>
> 2. Claude Action default write-access check: Count the documented default gate as effective, and flag the CONTRIBUTOR runs where write access couldn't be verified so they cross-reference cleanly with the sensitivity analysis.
>
> 3. Codex steps without event text in the prompt: Keep coded as not wired, since untrusted event text has no path into the prompt.

---

## 2. Where the frozen protocol is silent, or needs this choice

**Ruling 1 — unassociated bots, and frozen §8.**  
§8 states the primary outsider set as `NONE`, `FIRST_TIMER`, `FIRST_TIME_CONTRIBUTOR`, and `MANNEQUIN` if encountered, plus a fork pull request whose author is not a collaborator, member, or owner. It does not say whether a *Bot* actor with one of those associations (in this sample, Bot + `NONE`) enters the primary outsider rate or is held out. Ruling 1 closes that silence: humans only in the primary rate; unassociated bots in a separate sensitivity row.

**Ruling 2 — the effective-gate definition, and frozen §5.1 / §8.**  
§5.1 Bucket 1 requires that "an effective author / association / collaborator / allow-list gate is present and not visibly defeated." §8 ("Gates") lists an `if:` check on `author_association`, a collaborator lookup, an owner-equality check, a user allow-list, "or the action's default 'write users only' behavior (when not disabled)" as an effective gate when it actually held. The first pass treated the Claude Action's documented default write-access check as that default behavior, and noted a residual uncertainty: some `CONTRIBUTOR` runs executed on a unit that relied on that default, and write permission was not independently verified. Ruling 2 confirms the documented default gate is counted as effective, and requires those `CONTRIBUTOR` runs to be flagged so they cross-reference the §8 `CONTRIBUTOR` sensitivity analysis.

**Ruling 3 — event-field wiring, and frozen §5.3.**  
§5.3 event-verified reach requires that "the workflow YAML (or a pinned action default that the YAML does not override) wires a field of that event … into the agent prompt, an argument the agent is documented to read, or a checkout/tool path that supplies context to the agent." It does not say whether a packaged Action step that is invoked *without* interpolating event text (and without a documented default that loads the triggering comment or body) is wired. Ruling 3 keeps such Codex steps coded as not wired, because untrusted event text has no path into the prompt.

---

## 3. Effect on the first-pass results

Applied to the official sheet after the first pass and before the lock:

- The **primary floor and ceiling are unchanged at 1/134 scorable runs and 1/36 units.** Ruling 1 matches the first-pass headline (human-only primary rates). Ruling 2 matches the first-pass unit coding (the documented Claude default counted as an effective gate; no Claude unit moves from 1 to 2a). Ruling 3 matches the first-pass event-verified coding (Codex steps without event text in the prompt were already not treated as wired). There is still no additional `event-verified_not_log-confirmed` primary-human run, and still no Bucket 3 run.
- Sheet *flags* are updated to make the three rulings explicit: a bot-sensitivity flag for unassociated (Bot + `NONE`) runs; a flag on the `CONTRIBUTOR` runs whose write access was not verified, cross-referenced to the `CONTRIBUTOR` sensitivity analysis; and a resolution on every first-pass `edge_case_notes` row. Those flag and resolution columns do not change the locked bucket roll-up.
- The first-pass letter-of-§8 discussion (Bot + `NONE` as if it were primary) is retired as a headline alternative. Those runs remain in the bot-sensitivity row only.

Any other difference from the first-pass sheet, if one appears when the rulings are applied, must be reported honestly in the lock manifest rather than smoothed over.
