# Study 2 Tool Reference Sheet (pre-draw)

**Written:** 2026-11-23, 9:40 PM America/Chicago  
**Purpose:** Required coding aid under frozen PROTOCOL-v1.0 §3, written from current default-branch vendor docs **before** the official sample walk. The identifier set is frozen in the protocol and is not enlarged by this sheet.

**Version-match at coding time.** Open the docs and source for the *pinned* `uses: owner/action@ref` (or the CLI version actually invoked). If the pin cannot be resolved, use this sheet and flag uncertainty.

**Default-branch SHAs consulted (core API, 23 November 2026, after 9:35 PM America/Chicago):**

| Identifier | Default branch SHA | Sources read |
|---|---|---|
| `anthropics/claude-code-action` (and `claude-code-base-action` companion) | `e5c0fcd41850b0178962e40a9ef7cb1f5ab0c8b6` on `main` | README.md, docs/security.md, action.yml, base-action/README.md |
| `openai/codex-action` | `4aac6da4b686168e147798ca841cf64ff0f027b8` on `main` | README.md, docs/security.md, action.yml |
| `google-github-actions/run-gemini-cli` | `c8bfcfc10cf7ec12752cbb35395598f2f2eb920a` on `main` | README.md, docs/trust-guidance.md, docs/best-practices.md, action.yml |

Copies of those files are under `/workspace/study2-scoping/collection/raw/vendor_docs/` (box only). Contrast CLI units use the corresponding CLI product docs, **without** Action-wrapper features.

This sheet is not the protocol. It does not change buckets, families, or confirmation rules.

---

## How to use this sheet while coding Study 2

Study 2 buckets are about *observed untrusted-input reach* and *privileged actuation*, not Study 1 leftovers. This sheet answers:

1. **What untrusted event text does the tool ingest by default** (Direct route)?
2. **What stored instruction / MCP files can it load** (Indirect/stored route)?
3. **What default gates exist** (`author_association` / write-permission checks, trigger phrases, fork-PR defaults), so a skipped or early-exit run can be recognized as a guard rather than a silent Bucket 1?
4. **Which flags count as unrestricted tools** for frame eligibility and for privileged-actuation context?

Vendor defaults have changed since Study 1. Prefer the pin over this sheet when they disagree.

---

## 1. `anthropics/claude-code-action` (Claude family; includes `claude-code-base-action`)

**Direct ingestion.** The Action is commonly triggered by a phrase in an issue or comment (`trigger_phrase`, default documented as looking in comments or issue body), by `assignee_trigger`, or by `label_trigger`. A `prompt` input can replace or wrap those event fields. `track_progress` forces tag mode with tracking comments on selected `pull_request` and `issue` events. `include_comments_by_actor` / `exclude_comments_by_actor` change which conversation comments are pulled into context.

**Default access gate.** The Action is built around a write-access check on the triggering actor. `allowed_bots` is empty by default (no bots). `allowed_non_write_users` is a documented risky bypass (and, when set, the vendor recommends passing `github_token: ${ secrets.GITHUB_TOKEN }` and restricting tools). For `workflow_run`, the Action also checks the *upstream* actor (for example the fork-PR author) and the fork owner, and "stops before running Claude" if any of those accounts lacks write access. Fork PRs are skipped unless `allow_fork_prs` is true. `restrict_untrusted_prs` (default on) restores a fixed list of config paths from the *base* (or default) branch before Claude starts.

**Stored / MCP files (Indirect route).** On pull requests the Action restores, from the PR base branch (or the default branch for authors without write access): `.claude/`, `.mcp.json`, `.claude.json`, `.gitmodules`, `.ripgreprc`, `CLAUDE.md`, `CLAUDE.local.md`, `AGENTS.md`, and `.husky/`. PR-authored versions of those paths are kept under `.claude-pr/` for reference only. A later merged change to those files on the base branch is therefore a stored-injection surface. `restrict_untrusted_prs: false` turns this restoration off.

**Tools / privileges.** Additional tools and flags go through `claude_args` and `settings`. Unrestricted/auto-approve examples relevant to Study 2 eligibility include `--dangerously-skip-permissions`, `permission-mode: bypassPermissions`, and a bare `Bash` tool. `additional_permissions` can request extra GitHub permissions (for example `actions: read`). OIDC federation inputs require `id-token: write`.

**`claude-code-base-action`.** Companion / thin wrapper in the same repository (`base-action/`). Same Claude family cap. It does not add the higher-level comment-trigger wrapper; treat it as the lower-level runner. Version-match at coding time.

---

## 2. `openai/codex-action` (Codex family)

**Direct ingestion.** The Action runs `codex exec` with a required `prompt` or `prompt-file`. Workflows typically interpolate event fields (`github.event.issue.*`, `github.event.pull_request.*`, `github.event.comment.*`) into that prompt. There is no Study-1-style built-in `@codex` mention parser documented as a required default in the Action itself; any mention/gate is in the *workflow* `if:` or in the prompt text.

**Default access gate.** Documented inputs include `allow-users`, `allow-bots`, and `allow-bot-users`. The security doc recommends limiting who can run the workflow and defending against untrusted input (including shell interpolation). Gates are therefore **workflow- and input-dependent**; do not assume a write-access check fired unless the YAML or logs show it.

**Stored / MCP files (Indirect route).** Codex instruction files such as `AGENTS.md` (and other project docs the CLI reads from the checkout) can enter context after a `actions/checkout` (or equivalent) of a branch that already contains them. MCP/config in the repo may also be loaded depending on the pinned CLI version — version-match. This is a stored-injection surface when those files were written by an earlier commit or merged PR.

**Tools / privileges.** `sandbox` may be `workspace-write`, `read-only`, or `danger-full-access` (legacy). `permission-profile` is preferred (`:read-only`, `:workspace`, or a dangerous profile). `safety-strategy` includes a documented `unsafe` value (required on Windows). Those last two, plus `danger-full-access`, are unrestricted-tool / safety-off signals for eligibility and for privileged-actuation context. The security doc recommends running this Action as the last step in a job.

---

## 3. `google-github-actions/run-gemini-cli` (Gemini family)

**Direct ingestion.** The Action passes `prompt` to the Gemini CLI `--prompt` argument. Workflows typically interpolate issue/PR/comment fields into that input. Optional `github_pr_number` and `github_issue_number` inputs exist for helpers.

**Default access gate.** The Action does **not** implement a built-in `author_association` write-access gate comparable to Claude's. Trust guidance tells *workflow authors* to prefer maintainer-initiated runs, minimal `GITHUB_TOKEN` permissions, and tight tool policy. Any gate is in the workflow YAML (`if:`, environment protection, etc.). Absence of a vendor gate is not itself Bucket 3.

**Stored / MCP files (Indirect route).** `GEMINI.md` and other checkout-resident instruction or extension files, plus `settings` / `extensions` inputs, can enter context from repo state. Version-match the CLI.

**Tools / privileges — important default.** The current `action.yml` invokes the CLI with **`--yolo`** in the packaged run steps (both the debug and non-debug branches inspected in the SHA above). That is an auto-approve / unrestricted-tools default of the *Action wrapper*, not something the workflow has to pass. Frozen §3 eligibility therefore treats a line-verified `run-gemini-cli` job as having unrestricted tools, even if the workflow YAML itself does not mention `--yolo`. If a future pin removes `--yolo`, version-match and do not assume this default.

Vendor trust guidance: if processing untrusted data, strictly limit which tools the CLI may execute, and keep token permissions minimal.

---

## 4. Contrast CLI (no Action wrapper)

Contrast units invoke these quoted command forms in `.github/workflows`:

- `"npx @anthropic-ai/claude-code"` — Claude CLI
- `"npx @openai/codex"` — Codex CLI
- `"npx @google/gemini-cli"` — Gemini CLI

Use the CLI's own documented behavior (instruction-file loading, MCP, permission/sandbox flags, trailers). **Ignore Action-only inputs and outputs** (for example Action `upload_artifacts`, Action-only `prompt` plumbing, comment integration that exists only in the Action). Unrestricted-tool flags are the CLI equivalents (`--dangerously-skip-permissions`, `--yolo`, `danger-full-access`, `bypassPermissions`, bare `Bash`, `safety-strategy: unsafe`). Stored instruction files (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `.mcp.json`, and documented siblings) remain an Indirect route once the workflow checks out a ref that contains them.

---

## 5. Eligibility reminder (sampling, not a bucket)

A workflow enters the Study 2 frame only if the **agent job** has, or can inherit, non-read permissions, referenced secrets (other than a bare `secrets.GITHUB_TOKEN` used only as the default token input), or unrestricted / auto-approve tools. Effective permissions are those of the agent job (job-level `permissions:` and any passed tokens), not only the workflow-level block. Read-only single-turn classifiers are excluded at sampling. Unspecified permissions are treated as "can inherit" the repository's default `GITHUB_TOKEN` (which may be write) and therefore do not, by themselves, drop a unit from the frame.

This sheet does not authorize any live injection test, any write, or any workflow trigger.
