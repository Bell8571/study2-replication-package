> **REDACTED DERIVATIVE — NOT THE FROZEN FILE.** This is a redacted copy of `ADDENDUM-01-seeds.md`, produced for the public replication package on 2026-11-24 (America/Chicago). The frozen original was **not edited** and is retained in the author's private archive.
> Original SHA-256: `29339ca743ececc39b440147a9ecdfca53b790478ff23e5ac0ac58bac2c589ac`.
> Redactions (11 substitutions): the two operative seed strings, the six SHA-256 digests of those seed strings (listed and computed), and the time of day of the addendum timestamp. Reason: the sample digest is SHA-256 of `study2-v1.0|<seed>|<owner/repo>|<path>`; publishing the seed would let anyone re-run the seeded walk over public workflows and recover which repositories were sampled. Everything else is byte-for-byte unchanged. The SHA-256 of this derivative is recorded in `PROVENANCE.md`.

# Study 2 v1.0 — Addendum 01: official seeds

**Status:** locked (read-only). This addendum is not an edit to the frozen protocol.

**Addendum timestamp:** 2026-11-23 [time of day REDACTED] (America/Chicago, CST)

**Frozen protocol:** `/workspace/study2-scoping/PROTOCOL-v1.0.md`  
**Frozen protocol SHA-256:** `6d47296879bf9f102ff76b5eb754a43f12a98e6b8bb170d50bece614d9372741`  
**Protocol anchor:** [Bell8571/study2-untrusted-input-reach](https://github.com/Bell8571/study2-untrusted-input-reach) @ `37638e446d9b61abe14873e91e7995697ad226b7` (short `37638e4`)

This addendum records the official sample and IRR seed strings supplied by Jason (t43u) so that the official draw may start under frozen §10.2 and §13. It does not change buckets, families, the observation window, or any other frozen rule.

---

## 1. Observation window (unchanged; restated)

As frozen in PROTOCOL-v1.0 §10.1:

- **Start:** 2026-09-09T22:25:00-05:00 (America/Chicago, CDT) = 2026-09-10T03:25:00Z
- **End:** 2026-11-23T21:25:00-06:00 (America/Chicago, CST) = 2026-11-24T03:25:00Z

A run is in the window if its GitHub `created_at` (compared in UTC) is greater than or equal to the start instant and less than or equal to the end instant.

---

## 2. Official seed strings

The **operative seed is the seed string**, not any listed digest of that string. This follows Study 1 frozen §5.4–§5.5: the walk digest hashes a formula that *embeds the seed string*. Study 1's sample digest is SHA-256 of `study1-v1.0|<seed>|<owner/repo>|<path>`, where `<seed>` is the official seed string (for example `study1-v1.0|sample|2026-11-21|pewaukee-01`), and the result is lowercase hex, sorted ascending.

Study 2 frozen §10.2 requires the same digest *shape*, with the Study 2 seed strings recorded here. Therefore:

- **Sample walk digest:** SHA-256 of `study2-v1.0|<seed>|<owner/repo>|<path>`, using the sample seed string below. Expanded, that input is:

  `study2-v1.0|[REDACTED-SAMPLE-SEED]|<owner/repo>|<path>`

- **IRR digest (not drawn in this addendum):** SHA-256 of `study2-v1.0-irr|<seed>|<unit_id>`, using the IRR seed string below. Expanded:

  `study2-v1.0-irr|[REDACTED-IRR-SEED]|<unit_id>`

The IRR subsample is **not** drawn now. Frozen §11 draws it after the coding lock, and the official draw in this session does not compute IRR picks.

### 2.1 Sample seed

- **Seed string (operative):** `[REDACTED-SAMPLE-SEED]`
- **Jason-listed SHA-256:** `[REDACTED-SEED-DIGEST]`
- **Computed SHA-256 of the exact string, no trailing newline:** `[REDACTED-SEED-DIGEST]`
- **Computed SHA-256 of the exact string plus a single trailing LF (`\n`):** `[REDACTED-SEED-DIGEST]`

**Mismatch:** the computed no-newline digest and the computed LF digest both **differ** from the Jason-listed SHA-256. The listed value is recorded here and is **not** used as the walk seed. The walk uses the seed *string* in the Study 1-shaped formula above.

### 2.2 IRR seed (recorded now; draw deferred)

- **Seed string (operative):** `[REDACTED-IRR-SEED]`
- **Jason-listed SHA-256:** `[REDACTED-SEED-DIGEST]`
- **Computed SHA-256 of the exact string, no trailing newline:** `[REDACTED-SEED-DIGEST]`
- **Computed SHA-256 of the exact string plus a single trailing LF (`\n`):** `[REDACTED-SEED-DIGEST]`

**Mismatch:** the computed no-newline digest and the computed LF digest both **differ** from the Jason-listed SHA-256. The listed value is recorded here and is **not** used as the IRR-walk seed. When the IRR subset is drawn after the coding lock, the walk will use the seed *string* in the Study 1-shaped formula above.

---

## 3. Collection priority

Harvest and archive workflow-run logs and event payloads for runs dated **2026-09-09 through 2026-09-25** first. Those earliest runs in the window begin hitting the default 90-day GitHub Actions log-retention cliff around **2026-12-08**. Then continue through the rest of the window. Repositories that lowered retention below 75 days, and artifacts with a shorter `retention-days`, remain coverage gaps under frozen §10.1.

---

## 4. What this addendum does not change

- The frozen protocol file is not edited and remains mode 0444.
- Families, buckets, outsider set, confirmation rules, n and family caps, and the observation window are unchanged.
- No official IRR subsample is issued from this addendum.
