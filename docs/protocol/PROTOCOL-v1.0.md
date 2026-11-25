# Study 2 v1.0 — Observed reach of untrusted text into write-capable agent Actions

**Status:** FROZEN. This file must not be edited in place. Any correction requires a new dated, superseding file (for example `PROTOCOL-v1.1.md`), with its own hash. Prior files remain unedited, including `/workspace/study2-scoping/PROTOCOL-DRAFT-v0.1.md`.

**Date frozen:** 23 November 2026, 9:25:00 PM America/Chicago (CST, UTC−6). That instant is the **collection freeze timestamp** and the end of the observation window (§10).

**Do not edit** any Study 1 frozen or locked files, including `/workspace/framework/study1-v1.0-FROZEN.md`, the Deviation 01/02 addenda, or the locked Study 1 coding, draw, IRR, or results files.

**Provenance.** Built from `/workspace/study2-scoping/PROTOCOL-DRAFT-v0.1.md` (SHA-256 `fb91cbdc106f3b60d01943d5f4c1e277a100be214ac5901a1c3c5825cadc7b39`, left unchanged), the scoping note and `sources.csv`, Study 1 v1.0 frozen conventions, and Jason's freeze authorization and five closed decisions (t42u), after official-docs verification of the log- and run-retention claims (§10.1).

**Relationship to prior work.** Config-only prevalence of untrusted issue/PR text reaching write-capable agents in public GitHub Actions is already measured (Heimdallr, TaintAWI, Grackle, node9; see `SCOPING.md`). Study 2's new estimand is *observed* reach in already-executed public runs. The static-config arm (RQ3) is a post-hardening *replication* and must be labeled as such.

This document is written so a human coder can apply the rubric without this conversation's context.

---

## 0. Decision log (Jason, t42u, 23 November 2026)

All five open questions in PROTOCOL-DRAFT-v0.1 §12 are closed as follows. This freeze is authorized only because the two retention claims in decision 2 were verified against official GitHub documentation and changelog posts (§10.1).

1. **Families.** Keep Study 1's exact families: the packaged Claude, Codex, and Gemini Actions, plus the CLI contrast stratum, as Study 1 frozen §2 defined them. No OpenHands, SWE-agent, or custom runners.
2. **Window.** A 75-day lookback ending at the collection freeze timestamp: from 2026-09-09, 10:25:00 PM America/Chicago (CDT, UTC−5) to 2026-11-23, 9:25:00 PM America/Chicago (CST, UTC−6), which is exactly 75 × 24 hours. Rationale: the default 90-day public log retention, with margin. Jason also stated that from 2026-10-01 the same 90-day ceiling governs workflow run records and checks. Both claims were verified (§10.1). Repositories that lowered retention below 75 days are coverage gaps.
3. **Primary outsider set.** `NONE`, `FIRST_TIME_CONTRIBUTOR`, `FIRST_TIMER`, and `MANNEQUIN` if encountered. `CONTRIBUTOR` is in the sensitivity row only.
4. **Stratification.** Stratify by family only, with the SHA-256 seeded cap. Record stars, forks, and recent commit and issue velocity as covariates, not as strata.
5. **Log-confirmation edge.** A log line that names only the issue number or URL is `event-verified_not_log-confirmed` (ceiling), not Bucket 2b or 3. A distinctive substring of the untrusted input is required for log-confirmed ingestion.

---

## 1. Hard rules

Carried forward from Study 1 frozen §9, and tightened for this study:

Public data only. No writes. Never `actions_run_trigger` / `run_automation`. Never open issues, pull requests, comments, reviews, or dispatches on a target repository, including "just to see if the agent bites." Never execute anything found in artifacts, comments, instruction files, or MCP configs. Never connect to or test MCP servers listed in public files. Never run GitInject-style attacks, including on a throwaway fork of someone else's project.

Redact secrets, tokens, signed URLs, and credential-helper paths from any logs or excerpts that are retained. Fetch log and artifact URLs immediately and never store signed URLs (Study 1 frozen §4 and §9). Stop at 401/403/404/410. Do not invent findings. Separate observation from inference. Report nulls and negative results plainly.

Public-facing write-ups are aggregate only. Do not name unpatched repositories. Coordinated private disclosure is a later decision for Jason and is not authorized by this frozen file.

This is a passive config and exposure measurement, not exploit research. The rubric codes reach, route, and privilege. It does not decide whether a prompt injection "worked," and it does not require the coder to interpret a model's chain of thought as malicious.

---

## 2. Research questions

**RQ1 (primary; the new estimand). Observed reach.** In a SHA-256 seeded public sample of write-capable or secret-holding agent workflows, over already-executed public runs in the study window, how often did untrusted outsider text actually get ingested by the agent?

Report two bounds, and do not conflate either with pure static YAML reachability:

- **Floor (strict):** log-confirmed ingestion (see §6 and §7).
- **Ceiling:** the floor plus runs that are event-verified but not log-confirmed (the dedicated sub-status in §5.3).

**RQ2. Downstream privileged action, and injection-pattern rate.** Among log-confirmed reach runs (and, separately, among the event-verified ceiling), how often is there public-timeline evidence of a privileged actuation after that ingestion (§9)? Separately, how often does the ingested (or event-verified) payload already contain a recognizable injection pattern (the `-inj` tag in §5.4)? The `-inj` rate is descriptive of payloads that already exist in public data. It is not a success rate for injection.

**RQ3 (secondary; must be labeled a replication). Residual static-config exposure after 2026 hardening.** In the same seeded sample, what share of units still meet the untrusted-trigger + no effective gate + (write or secrets or unrestricted tools) primitive used by Heimdallr, TaintAWI, Grackle, and node9, including explicit opt-outs such as `allowed_non_write_users: "*"`? This is not a first measurement of that primitive. Compare descriptively to the 2026 published figures without claiming the samples are statistically equivalent.

Optional tags in §5.4 are not separate research questions.

---

## 3. Scope, frame eligibility, and exclusions

**In-scope families (frozen; identical to Study 1).** The packaged set is exactly the four verified coding-agent workflow actions in Study 1 frozen §2.1, grouped into three tool families for caps and reporting:

- **Claude:** `anthropics/claude-code-action` and `anthropics/claude-code-base-action` share one family cap.
- **Codex:** `openai/codex-action`.
- **Gemini:** `google-github-actions/run-gemini-cli`.

The contrast stratum is kept, with the same frozen quoted command forms in `.github/workflows` as Study 1 frozen §2.2:

- `"npx @anthropic-ai/claude-code"` — **Claude CLI**
- `"npx @openai/codex"` — **Codex CLI**
- `"npx @google/gemini-cli"` — **Gemini CLI**

**No further packaged identifiers and no further contrast signatures are added.** OpenHands, SWE-agent, custom LLM-tool runners, `actions/ai-inference`, and any `github/copilot*` workflow action are out of this frozen set. If a repository also qualifies for the packaged stratum, assign it to the packaged stratum only.

**Contrast allocation (unchanged from Study 1):** take all eligible Codex CLI and Gemini CLI units up to 4 each, then fill the remainder up to 10 with Claude CLI. Walk each CLI list in SHA-256 sort order as specified in §10. If a CLI list is exhausted before its allocation is filled, do not relax the rules; report the shortfall.

A Study 2 Tool Reference Sheet must be written from the pinned versions before the official draw and is a required coding aid (vendor defaults and security docs have changed since Study 1). The identifier set itself is frozen here and is not enlarged by that sheet.

**Frame eligibility.** A workflow file enters the frame only if the agent job has, or can inherit, non-read permissions, referenced secrets, or unrestricted / auto-approve tools (for example `--yolo`, `--dangerously-skip-permissions`, `permission-mode: bypassPermissions`, bare `Bash`). Read-only single-turn classifiers are **excluded at sampling**, not coded as Bucket 1. Effective permissions are those of the *agent job* (job-level `permissions:` and any passed tokens), not only the workflow-level block.

**Triggers in scope.** `issues`, `issue_comment`, `pull_request`, `pull_request_target`, `pull_request_review`, `pull_request_review_comment`, and `workflow_run` consumers chained off one of those, plus fork-PR checkout paths. Commit *metadata* on a fork PR (title, message) is a Direct route (§5.4), not a separate surface.

**Excluded surfaces.** Webhooks and `repository_dispatch` as a primary surface (if a sampled unit happens to use dispatch, tag it; do not build a dispatch frame). Email. GitHub Apps that have no workflow file. Live MCP-server testing. Private repositories.

**Out of scope as a claim.** Proving theoretical exploits; naming a first config-only census; measuring enterprise mailbox exposure.

---

## 4. Unit of analysis

Two layers, both required, so that sampling stays in Study 1 form while RQ1/RQ2 stay run-aware.

- **Draw unit (sampling and RQ3):** one line-verified `(repository, workflow file)` pair. `unit_id` is `{owner}/{repo}|{workflow_path}`. This is Study 1 frozen §5.4. At most one sampled unit per repository per tool family. A repository may still contribute one unit in more than one family.
- **Coding unit (RQ1 and RQ2):** each inspected executed run of that draw unit, recorded as `(unit_id, run_id)` together with the triggering event payload and the job logs / artifacts actually read.

**Roll-up.** Every draw unit also receives one primary bucket, by precedence **3 > 2b > 2a > 1**, after all of its inspected runs and its static config have been coded. A unit with both a log-confirmed 2b run and a 2a-only config finding is coded **2b**, with both records kept. Event-verified-not-log-confirmed is a sub-status; it does not outrank 2a and does not enter 2b or 3.

Inspect the **5 most recent completed executed (not skipped) runs** of the agent job in the study window, uniformly, as in Study 1 frozen §5.4 and §6.1. Record skip counts. A candidate with **zero** executed runs in the window is not sampled; log it and continue the walk. A candidate with 1–4 executed runs remains eligible; inspect those runs and record the shortfall. Skipped-run counts and coverage gaps are not evidence of a clean Bucket 1.

---

## 5. Buckets, sub-status, and tags

### 5.1 Mapping (read this before coding)

Study 1 used buckets 1 / 2a / 2b / 3 for a *different* construct (operational exhaust and off-task A2A). Study 2 reuses the **label shape and the precedence**, not the Study 1 meanings of 2a and 2b. Do not carry Study 1 leftover rules into these codes.

| Study 2 bucket | Name | Jason's draft label | Meaning in this study |
|---|---|---|---|
| **1** | Guarded / not exposed | B0 | No untrusted path to the agent job, or an effective author / association / collaborator / allow-list gate is present and not visibly defeated. (Read-only agents never enter the frame.) |
| **2a** | Config-exposed only | B1 | Static YAML (and, if needed, pinned action docs) show: untrusted or outsider-reachable trigger, no effective gate, and write permissions or secrets or unrestricted tools. No inspected run of this unit is log-confirmed ingestion. |
| **2b** | Observed reach, no privileged actuation | B2 | Log-confirmed ingestion of untrusted outsider text into the agent, on an already-executed public run, and no qualifying privileged actuation on that run (§9). |
| **3** | Observed privileged actuation | B3 | 2b, plus public-timeline evidence that the same run performed a privileged actuation after that ingestion. |

Precedence at the draw-unit level: **3 > 2b > 2a > 1**.

**Log-confirmed ingestion is the strict gate for Buckets 2b and 3.** Without it, a run cannot enter 2b or 3. Bucket 2a is the static-config bucket (RQ3). It is *not* an observed-reach bucket, and it is *not* the event-verified ceiling.

### 5.2 What each observed bucket still requires, besides log confirmation

For 2b or 3, all of the following must hold for the run:

1. The triggering actor is an outsider under §8 (or the Direct payload is otherwise untrusted fork-PR / first-time comment text as defined there).
2. The agent job, on that run, held write permissions, secrets, or unrestricted tools (effective, not merely workflow-level).
3. Ingestion is **log-confirmed** under §7.

Bucket 3 additionally requires a confirmed privileged actuation under §9. Ordinary triage comments or labels under `issues: write` or `pull-requests: write` do **not** automatically promote a run to 3. Contents writes, releases, package publishes, workflow-file changes, secret-relevant tool use, or unrestricted shell on the runner are the intended 3 sinks. That promotion line is tight on purpose.

### 5.3 Dedicated sub-status: `event-verified_not_log-confirmed`

This is **not** a fifth bucket. It is a required sub-status on a run (and, if any such run exists and the unit is not already 2b or 3, on the draw unit).

Code `event-verified_not_log-confirmed` when all of these hold:

- The run was triggered by an outsider-authored event in scope (§8).
- The workflow YAML (or a pinned action default that the YAML does not override) wires a field of that event — for example `github.event.issue.body`, a comment body, a PR title, a fork commit message — into the agent prompt, an argument the agent is documented to read, or a checkout/tool path that supplies context to the agent.
- The agent job on that run held write permissions, secrets, or unrestricted tools.
- The logs and artifacts actually read do **not** meet the §7 log-confirmed test. This includes missing, expired, 401/403/410, truncated-before-the-prompt, and sanitized logs that never echo the payload, and it includes a log line that names only the issue or pull-request number or URL without a distinctive substring of the untrusted input (decision 5).

A unit whose only untrusted-run evidence is this sub-status remains **Bucket 2a** (config-exposed). The sub-status is what distinguishes "YAML says this could happen, and we never saw a qualifying run" from "a qualifying run happened, and we could not confirm ingestion in the log."

**Findings table (required).** Every RQ1 result is reported as two bounds:

| Bound | Definition | Must not be described as |
|---|---|---|
| **Floor** | Share of inspected executed runs (and, separately, of draw units) in Bucket 2b or 3, i.e. log-confirmed ingestion | "exposure," unqualified; static YAML reachability |
| **Ceiling** | Floor plus runs (and units) with `event-verified_not_log-confirmed` | log-confirmed reach; static YAML reachability |
| **RQ3 residual (separate row)** | Share of draw units in Bucket 2a, 2b, or 3 (static primitive holds, whether or not a run confirmed it) | observed reach; the floor; the ceiling |

The ceiling is not "we proved the prompt was ingested." The floor is not "this is the only exposure that exists." Pure static YAML (RQ3, including 2a units with no qualifying run) is a third number.

### 5.4 Tags (not buckets; may co-occur)

**Injection route** (binding; code whenever 2b, 3, or `event-verified_not_log-confirmed` applies). Multi-label if both routes are present.

- **`route:direct`.** The untrusted text is trigger-event text: issue title or body, PR title or body, issue or PR comment, review or review comment, or fork-PR commit metadata (message / title).
  - *Event-verified evidence:* the run's event type is one of those; the actor is an outsider under §8; and the YAML or pinned default wires that event field into the agent.
  - *Log-confirmed evidence:* §7 is met on a distinctive substring of *that event payload* appearing in the agent prompt or input context (not merely in a later agent comment that paraphrases the issue, and not merely a log line that names the issue number or URL).
- **`route:indirect_stored`.** The untrusted text is repo-state or runtime-fetched content such as `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `.mcp.json`, `.gemini/` settings, hooks, or skills, that was (a) modified by an earlier merged pull request, or (b) fetched at runtime via checkout of an untrusted ref or via a tool call.
  - *Provenance evidence (required in both confirmation states):* a public commit and, where it exists, the merged PR that introduced or last changed the relevant passage, or a checkout of `github.event.pull_request.head.sha` (or equivalent) that includes the file; plus a note of whether the author of that change was an outsider. A maintainer-written instruction file that has always lived on the default branch, with no outsider-authored change in the relevant passage, is **not** this tag. That is trusted operator state.
  - *Event-verified evidence:* provenance as above, and the job checks out a ref that contains the file, and the agent family is documented or observed in the pinned source to load that filename from the workspace (or the workflow explicitly passes it). The log need not echo the file.
  - *Log-confirmed evidence:* §7 is met on a distinctive substring of *that file's untrusted passage* in the agent prompt or input context, plus the same provenance.

**`-inj` (injection-pattern tag).** The already-public payload (Direct event text or Indirect/stored file) contains a recognizable instruction-like pattern: "ignore previous instructions," hidden HTML comments aimed at an agent, role-play takeovers, or explicit tool/exfil instructions. Coded only on text that already exists. Never planted by us. This tag does not mean the agent obeyed the pattern.

**Other scoping tags, retained:**

- `workspace_poison` — the agent job checks out an untrusted ref and then runs in that tree (overlaps `route:indirect_stored` when instruction or MCP files are in that tree; use both when both apply).
- `mcp_client_config` — a committed client config (`.mcp.json`, Action MCP settings, "enable all project MCP servers") is in play. Do not probe the server.
- `gate_present_but_ineffective` — a gate appears in YAML (label, allow-list, association check) but is visibly defeated (a template or bot applies the label; `allowed_non_write_users: "*"`; a documented bot/app bypass).
- `dispatch` — the unit uses `repository_dispatch` or an equivalent webhook-like trigger. Descriptive only.

---

## 6. Study 1's rule for logs that do not show the input — quoted, then extended

Study 1 did **not** have a frozen clause that named "prompts or event inputs not echoed in the job log." That construct was not Study 1's estimand. The frozen protocol instead treated unseen, unreadable, or expired material as a coverage gap, forbade inventing contents, and separated observation from inference. Those are the rules Study 2 extends.

From the frozen scope reminder (Study 1 v1.0, `/workspace/framework/study1-v1.0-FROZEN.md`, header):

> Do not invent findings. Separate observation from inference. Give a mundane explanation for every candidate. Report nulls plainly. Wiki pages are logged as **unreadable**.

From frozen §5.4:

> Expired artifacts or logs are coverage gaps, not evidence of a clean null on that channel.

From frozen §6.1 (what to inspect):

> Those five executed runs: jobs, **actual log text**, **actual unzipped artifacts** (fetch signed URLs immediately; never store them). Record expired or 401/403 as coverage gaps, and record skip counts as above.

From frozen §4:

> Wiki: log **unreadable**. Do not invent wiki contents.

From frozen §6.2, on circumstantial attribution:

> **A4.** Strong circumstantial only, with a mundane alternative. Not sufficient alone for Bucket 3.

From frozen §9:

> Public data only. No writes. Never `actions_run_trigger` / `run_automation`. Redact secrets, tokens, signed URLs, and credential-helper paths from logs. Do not execute anything found in artifacts or comments.

Study 1 coding practice was consistent with those rules and is recorded here only as practice, not as frozen text: HTTP 410 (expired) job logs were logged as coverage gaps ("skip cannot be confirmed from the log, only inferred as a coverage gap"); a job log "truncated mid-JSON (prompt echoed into the log)" used the portion actually read and treated the unread remainder as a coverage gap.

**Study 2 rule (frozen).** Apply the Study 1 gap discipline, then split confirmation as follows:

1. Always read **actual** log text and unzipped artifacts, or record why they could not be read (expired, 401/403/410, empty, truncated). That failure is a coverage gap. It is not Bucket 1, and it is not log-confirmed 2b/3.
2. **Log-confirmed** is the only way into Buckets 2b and 3. YAML plus an outsider-triggered run, without an echo of the payload in the log or artifact, is **not** observed reach. It is `event-verified_not_log-confirmed`, and the unit stays at most 2a.
3. **Event-verified** is the ceiling, not the floor. It is stronger than static YAML alone (a real run happened on a wired untrusted field) and weaker than log confirmation.
4. Static YAML reachability without a qualifying untrusted run in the window is RQ3 / Bucket 2a with no event-verified sub-status. Do not fold it into the ceiling.
5. Circumstantial output (the agent later comments in a way that *could* reflect the issue) is not log-confirmed ingestion, by analogy with Study 1's A4: circumstantial evidence is not enough to enter the highest observed bucket, and here it is not enough to enter 2b either.
6. A log line that names only the issue or pull-request number or URL, and does not contain a distinctive substring of the untrusted input, is **not** log-confirmed. Code `event-verified_not_log-confirmed` when the rest of §5.3 holds (decision 5).

---

## 7. Log-confirmed ingestion — operational test

A run is **log-confirmed** only if a job log, a documented agent transcript, or an unzipped artifact that the sampled workflow produced contains a **distinctive substring** of the untrusted payload — a phrase that uniquely identifies the issue/PR/comment body or title, or the untrusted passage of an instruction / MCP file — in a context that is the agent's *input* (prompt, system or user message, or tool-provided context fed to the model).

**Counts as confirmation:**

- The issue or comment body, or a long unique excerpt from it, printed in the action's prompt-construction log or in a retained input transcript.
- The text of `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` / `.mcp.json` (the untrusted passage) appearing in the prompt or in a "loaded project instructions" section of the log.
- A truncated log, if the distinctive substring is in the portion actually read.

**Does not count as confirmation:**

- YAML interpolation alone, or run metadata that names `issues` / `pull_request` as the event.
- An agent *output* comment that paraphrases the issue ("You reported a build failure on Node 22") without the input side appearing in the log.
- A log line that only shows a command such as `gh issue view 123` and not the issue content.
- A log line that names only the issue or pull-request **number or URL**, without a distinctive substring of the untrusted title or body. That is `event-verified_not_log-confirmed`, not 2b or 3.
- A checkout listing that names `CLAUDE.md` but does not show its contents in the model context.
- Sanitized or redacted placeholders (`[issue body redacted]`, `***`) with no distinctive payload text.
- A coverage gap: expired, 410, 403, or a truncation that ends *before* any prompt echo. Record the gap. If §5.3 otherwise holds, code `event-verified_not_log-confirmed`.

When in doubt, do not confirm. Flag `confirmation-uncertain` and leave the run in the event-verified sub-status. Redact secrets and signed URLs from any excerpt that is kept.

---

## 8. Author association and "outsider"

Code the triggering actor from the event payload and, where the API provides it, `author_association`.

**Primary outsider set (used for the floor and the ceiling):** `NONE`, `FIRST_TIMER`, `FIRST_TIME_CONTRIBUTOR`, and `MANNEQUIN` if encountered, and a pull request from a fork whose author is not a collaborator, member, or owner. Same-repository branches opened by `MEMBER`, `OWNER`, or `COLLABORATOR` are not outsider triggers for the primary rates.

**`CONTRIBUTOR`.** A `CONTRIBUTOR` association means prior commits, not write access. It is **not** in the primary outsider set. Report a sensitivity analysis that adds `CONTRIBUTOR` (and fork PRs from contributors) to the outsider set.

**Missing association.** If `author_association` is absent, use other public evidence (fork PR, first-time commenter history) when it is clear. If it is still unclear, tag `association_unknown` and **do not** count the run as outsider in the primary floor or ceiling. A sensitivity column may include these runs when a fork or first-time history is later resolved.

**Gates.** An `if:` check on `author_association`, a collaborator lookup, an owner-equality check, a user allow-list, or the action's default "write users only" behavior (when not disabled) is an effective gate when it actually held. If the run executed for an outsider, the gate did not hold; code the run under §5 and add `gate_present_but_ineffective` when a gate was written but bypassed or auto-satisfied.

---

## 9. Confirming privileged actuation from public timelines

Bucket 3 requires a public, durable, attributable side effect of the *same* run, after ingestion, not a claim in the agent's comment that it "pushed" or "fixed it."

**Confirm from:** the issue or PR timeline and events; commits and compare views on the run's branch or on the default branch; newly opened or merged pull requests; releases or published packages; workflow-file commits; and job-log lines that show unrestricted shell or secret-relevant tool use *already present* in the public log. Attribution follows Study 1 frozen §6.2 in spirit: prefer identity that ties the side effect to this workflow run (bot login, `performed_via_github_app`, commit trailer, or the job log of this `run_id`). Sibling workflows and later apps are context unless this file produced the side effect.

**Timing.** The side effect must occur after the run's start and in a window consistent with the run (during the run or immediately after its conclusion). A commit from a week later is not this run.

**Do not confirm from:** the agent's narrative alone; a human maintainer's later commit; a dependabot or sibling-bot change; or `issues: write` comments and labels, unless a later superseding file tightens or loosens that line (this frozen file keeps them at 2b).

If ingestion is only event-verified, a contemporaneous privileged side effect may be recorded as a note on the ceiling case. It still does **not** move the run to Bucket 3, because 3's gate is log-confirmed ingestion.

---

## 10. Sampling

Reuse Study 1's walk, not a convenience sample.

### 10.1 Observation window, and verification of the retention claims

**Collection freeze timestamp (window end):** 23 November 2026, 9:25:00 PM America/Chicago (CST, UTC−6) = 24 November 2026, 3:25:00 AM UTC.

**Window start:** exactly 75 × 24 hours earlier: 9 September 2026, 10:25:00 PM America/Chicago (CDT, UTC−5) = 10 September 2026, 3:25:00 AM UTC.

A run is in the window if its GitHub `created_at` (compared in UTC) is greater than or equal to the start instant and less than or equal to the end instant. Inspect, per unit, the five most recent completed *executed* (not skipped) agent-job runs in that window.

**Jason's two retention claims, verified against official GitHub sources before this freeze (URLs retrieved HTTP 200 on 23 November 2026):**

1. **Default 90-day public log retention.** GitHub's repository Actions settings documentation states: "By default, checks, workflow runs, commit statuses, and the artifacts and log files generated by workflows are retained for 90 days before they are automatically deleted." For public repositories the same page states that the period can be changed to anywhere between 1 day and 90 days (so 90 days is both the default and the public-repository maximum). Source: [Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository). The same default and public 1–90 day range is restated in the organization-level page, [Configuring the retention period for checks, workflow runs, commit statuses, artifacts, and logs in your organization](https://docs.github.com/en/organizations/managing-organization-settings/configuring-the-retention-period-for-github-actions-artifacts-and-logs-in-your-organization), and in [Downloading workflow artifacts](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/download-workflow-artifacts) ("By default, GitHub stores build logs and artifacts for 90 days").
2. **From 1 October 2026, the same ceiling governs workflow run records and checks.** The 1 October 2026 GitHub Changelog states that, as previously announced, "checks, workflow runs, and statuses are now governed by the same GitHub Actions retention setting that controls how long artifacts and logs are kept," that these records "are automatically cleaned up when they exceed the retention period configured for your enterprise, organization, or repository," and that "the maximum retention for public repositories is 90 days." Source: [Actions retention now covers checks, runs, and statuses](https://github.blog/changelog/2026-10-01-actions-retention-now-covers-checks-runs-and-statuses/) (1 October 2026). The advance notice of 27 August 2026 stated the same start date and "a default of 90 days," and that for public repositories "the maximum retention for checks, workflow runs, and statuses is 90 days, matching the existing limit for artifacts and logs." Source: [Actions retention will cover checks, workflow runs, and statuses](https://github.blog/changelog/2026-08-27-actions-retention-will-cover-checks-workflow-runs-and-statuses/).

Repositories (or organizations or enterprises) that lowered the configured retention below 75 days, and individual artifacts whose `retention-days` is shorter than the window, are **coverage gaps**, not evidence of a clean Bucket 1. Per-artifact retention can be shorter than the repository default; that remains a coverage gap, as in Study 1.

### 10.2 Frame construction, draw, covariates, and n

**Frame construction.** Refresh identifier queries for the frozen Study 1 families only. Recalibrate any GitHub code-search slice that hits the 1,000-hit cap (Study 1 Deviation 01: one-time remainder re-fetch, then freeze the union; do not chase live `total_count` drift). Log `total_count` and `incomplete_results` per slice. Private, archived, unreadable, comment-or-example-only, and the tool's own source repo and its forks are excluded, as in Study 1 frozen §5.4. Dogfood may be inspected as adjunct, not in the rate denominator.

**Draw.** After the bounded, line-verified, deduplicated frame is built, form a SHA-256-sorted list per family. Digest shape as in Study 1 frozen §5.5, with Study 2 seed strings **to be supplied by Jason before the official draw**. No official sample is issued until those seeds are recorded in a dated addendum. Walk strictly in digest order. Log every exclusion and every zero-executed-run candidate. Do not skip ahead. One unit per repo per family; only an actually sampled unit consumes the slot (Study 1 Deviation 01(b)).

**Stratification and covariates.** Family walks are the only strata (decision 4). Record, for each sampled unit and walked candidate as available, star count, fork count, and recent commit and issue velocity as **covariates**, not as sampling strata.

**n.** Study 1 hand-coded 38 units and 156 executed runs (up to five runs per unit; 13 shortfall units). Study 2 coding is heavier. This frozen file therefore keeps a Study 1-like draw:

- Target **30 packaged units** (family cap **10** for Claude, Codex, and Gemini), plus about **10 contrast CLI units**: about **40 draw units**.
- Up to **5** executed runs per unit in the window: about **150–200 runs** inspected, of which many will be shortfalls, as in Study 1.
- An IRR overlap of n = 200 is not used.

A 25-job-check / 10-page run-listing cap, if used again, must be logged as a coverage cap (Study 1 D9 / skip-register v2 lesson), not as a demonstrated zero-executed result.

---

## 11. IRR

Report, at least, as in Study 1 frozen §8.3: the confusion matrix for the four-way bucket {1, 2a, 2b, 3}; **raw percent agreement**; **Cohen's kappa**; a collapsed table as needed; **PABAK**; **Gwet's AC1**; and the **kappa-paradox flag**. Also report agreement on (a) `event-verified_not_log-confirmed` yes/no, (b) the injection-route tags, and (c) `-inj`, as separate tag tables, not as extra bucket levels.

**Do not** use "Cohen's kappa ≥ 0.80 before single-annotator scaling" as a gate. Study 1 already showed the paradox: with a Bucket 1–heavy draw, kappa can be undefined or 0 even when raw agreement is high. Adopt Study 1's stop-and-revise rule: revise before any public claim if raw agreement is < 80%, or if both AC1 and PABAK are < 0.60. Do not stop solely because kappa is < 0.60 when raw agreement is ≥ 80% and at least one of AC1 or PABAK is ≥ 0.60. In that case report all measures, show the marginals, and flag "possible kappa paradox / skewed prevalence." Blind measures are computed on untouched blind codes. Any adjudication log or consensus recode is a separate column.

**The IRR draw must include non-Bucket-1 units.** Study 1 frozen §5.5 said not to stratify on bucket; the issued 8-unit draw (Deviation 02, after the coding lock) landed entirely in Bucket 1, so four-way kappa was undefined. This frozen file therefore **does stratify after the coding lock**:

- Packets are still blind: no our bucket, no our tags, no our mundane explanation, no hinted adjectives (Study 1 frozen §8.2 format, plus event payloads, association fields, log excerpts actually read, and coverage gaps).
- Take **every** draw unit the primary coder placed in 2a, 2b, or 3, up to a cap of 12, plus a SHA-256 sample of Bucket 1 units so that the overlap is about 20% of the official sample or at least 8, whichever is larger, and not more than 16 packets.
- If non-Bucket-1 units exceed 12, SHA-256-sort those units and take the first 12, recording the remainder.

An IRR overlap of 200 is rejected as unworkable.

**Labeling.** If the second coder is again an AI system, label the IRR transparently as **AI-versus-AI**, as Study 1 did (GEM-IND = Gemini vs Lopez, initials GB). If a human second-codes, label it as human-versus-AI or human-versus-human as appropriate. The adjudication log lists disagreements, the rule applied, and the consensus code, and is not used as the blind IRR claim.

---

## 12. Ethics, disclosure, and honesty limits

Already stated in §1. Recapped for the freeze checklist:

- Public data only; no writes; no triggering; no test issues or test PRs; no live payloads; no MCP-server exercises.
- Redact secrets, tokens, signed URLs, and credential-helper paths. Never store signed URLs.
- Public write-up: aggregate rates, maybe anonymized examples. No list of unpatched repositories (Grackle / node9 practice).
- Coordinated private disclosure is a separate, later authorization by Jason. This frozen file does not grant it.
- Rates are rates in the retrieved, line-verified, seeded sample, not population estimates of all of GitHub. The 1,000-hit cap, log and run retention (including repositories that lowered retention below 75 days), UI-only repo settings, and hidden action self-gates are limits and must be reported as such.
- RQ3 must be labeled a replication of 2026 config-prevalence work, not a first measurement.
- Emails remain out of scope. There is no public-data mailbox frame.

---

## 13. Path from here

This file is **frozen**. Do not edit it in place. Do not change the hash by silent amendment. If a correction is required, write a new dated superseding file and record the hash; log any execution that already used this file. The v0.1 draft stays as-is.

After freeze: Jason supplies sample and IRR seed strings (recorded in a dated addendum, not by editing this file). Then refresh identifier queries for the frozen families, write the Tool Reference Sheet, recalibrate capped search slices, build the bounded frame, execute the seeded walk, code units and runs, lock codes, then build blind IRR packets under §11. No official sample is issued until the seeds are recorded.
