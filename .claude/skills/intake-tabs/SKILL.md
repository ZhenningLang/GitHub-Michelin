---
name: intake-tabs
description: 当要把 Chrome 里开着的 GitHub 项目标签页批量收录进本索引时使用（「收录浏览器里的项目」「处理我开的 tab」）；读用户本人 Chrome（按进程号，不碰自动化实例），逐个仓库分派 add-project（新项目）或 sync-entry（已收录），每个仓库门禁全绿、单独 commit 后关掉它的标签，读下来不适合收录的保留标签并列出来交用户定，最后汇报数量、PR、仍开着的标签、可被 ~/.dotfiles 吸收的项目和横向对比选题池。不用于写单个页面（用 add-project）、按领域搜新项目（用 project-harvester）或清 `未收录` 积压（用 tools/intake_sweep.py）。
argument-hint: "[--parallel N] [模型/额度要求]"
metadata:
  internal: true
---

# intake-tabs

Turn the GitHub repos the maintainer left open in Chrome into selection pages, one repo at a time,
closing each repo's tabs once its page is committed. This skill is the **batch loop**; the page
itself is `add-project` (new repo) or `sync-entry` (already indexed) — do not re-derive their rules
here. Deterministic parts live in `tools/tab_intake.py`; read its docstring once.

## Ground rules (from the maintainer, 2026-09-28 — they win over habits)

- **Include wide, research fully.** Every real repository gets a page per AGENTS.md inclusion
  criteria: young, hyped, archived, security/pentest, and single-author repos are all in; their risk
  goes into `Health & viability`. "Not judging" never means "not researching": no
  `<!-- oss-atlas:unresearched -->`, every page passes the full `add-project` procedure.
- **Unfit → propose, don't drop.** If reading a repo shows it fails the inclusion criteria (not a
  repository in substance, an exact duplicate, contentless) or sits in a gray zone (extracted
  prompts of a closed product, an article/tutorial collection, a leaked-source commentary), set it
  to `propose` with the reason, **keep its tab open**, and list it in the report. The user decides.
  Precedent: the 2026-09-28 batch skipped four such gray-zone repos and the user had all four added
  the next day — so the propose bar is narrow and the reason must be specific.
- **Touch only what you processed.** Never close a tab whose repo is not `done` in the ledger
  (`tab_intake.py close` refuses). Non-GitHub tabs (X posts, blogs) and the maintainer's own repos
  (`ZhenningLang/*`) are out of scope — leave them. An org/user page (`github.com/TanStack`) is
  printed as `OWNER-PAGE`: ask before expanding a whole org.
- **Don't ask mid-run.** Anything uncertain → pick the reversible option, note it in the ledger,
  surface it in the final report. Stop only for push authorization or a quota threshold the user set.
- **Tabs arrive while you work.** Re-run `scan` between repos; new tabs join the queue.

## Procedure

1. **Worktree + ledger.** Work outside the main checkout:
   `git worktree add ../oss-atlas-tabs-<UTC date> -b feat/intake-tabs-<UTC date> origin/main`.
   The ledger is `intake/tabs-<UTC date>/ledger.md` in that worktree (committed with the pages; it
   is the resume state — `done` rows are never redone). If today's ledger exists, continue it.

2. **Scan.** `python3 tools/tab_intake.py scan --ledger intake/tabs-<date>/ledger.md`
   canonicalizes each tab via `gh api` (renames/redirects collapse to one row) and classifies it:
   `sync` (frontmatter `repo:` already indexed; page path filled in), `add`, or `skip` (404, empty,
   own repo — tab stays). Notes flag forks (decide whether it diverged from upstream or is an exact
   duplicate → `propose`) and archived repos (include). `DEFER: …Chrome…` means the user's Chrome
   could not be singled out — do not fall back to AppleScript by app name; report it.

3. **Per repo** (`tab_intake.py pending` gives the queue; mark `set <repo> running` first):
   - `add` → run `add-project` end to end; `sync` → run `sync-entry` on the ledger's page (it
     gates on `last_verified` itself; a fresh page is `done` with no diff).
   - **Batch overrides for add-project** (they win over its text for this skill):
     - *Close-the-loop is off.* A comparison alternative that is a real, unindexed repo stays
       `未收录` with "not added in this tab batch" in its tradeoff cell. Grep `categories/` first — an
       indexed alternative must be linked, not marked `未收录` (the gate fails).
     - *Batch siblings.* Never mark another repo **in this ledger** as `未收录`: it will be indexed
       before the batch merges and the gate will fail. Mention it in prose instead.
     - *Q&A.* There is no reading conversation, so omit the section and write `no leftover Q&A` in
       the commit message.
   - `make gates` green → one commit per repo (`add(<owner/repo>): …` / `sync(<owner/repo>): …`,
     body `Tab intake <date>. no leftover Q&A.`) → `set <repo> done --page <path>` →
     `close --ledger … <repo>` (closes every tab of that repo, any subpath, case-insensitive).
   - Gates red after two real fix attempts → `set <repo> failed --note "<error>"`, tab stays,
     move on. Lint fanout WARN → a separate `refactor-index` commit, not inside the repo's commit.
   - Unfit after reading → `set <repo> proposed --action propose --note "<specific reason>"`.
   - Re-run `scan`.

4. **Push cadence.** Every ~10 commits, and at the end: push the branch, open or update one PR,
   merge when CI is green. Pushing needs the user's approval through their command guard; ask with
   the exact `! …` command, and run the push as its own command so the approval is not consumed by
   a compound command that fails first. After merge report only "已合并，同步后生效".

5. **Final report** (Chinese, one screen; tables in a file if longer):
   - Failures, `propose`, and still-open tabs **first**: which repo, why, what the user must decide.
   - Counts: added / synced (changed vs fresh) / skipped / failed; PR link(s).
   - **~/.dotfiles absorption:** for each processed repo, judge honestly whether a mechanism in it
     (a skill idea, a hook, a workflow, a tool) could be absorbed into the user's agent harness in
     `~/.dotfiles`; list only `medium`/`high` fits with priority, one-line summary, the mechanism,
     the dotfiles skill/hook it maps to (or "new"), and the **local page path** so another agent can
     read it. Never write dotfiles notes into the pages.
   - **Topic pool:** categories where this batch plus existing pages now hold ≥ 4 projects, each with
     one line: the most worth-comparing question in that category.

## Parallel mode (optional — when the user asks for workers or the queue is long)

Research and drafting parallelize; shared files do not. Each worker gets its own worktree detached
at the intake branch tip and the brief in [`worker-brief.md`](worker-brief.md); it runs the full
page procedure plus `make gates` but never commits, pushes, or touches tabs. The main session then
integrates **serially**, one repo at a time:

**Which runner.** The model the user names decides it — do not reuse an old batch's scripts:
- Claude models (`opus`, …): the Agent tool with `isolation: "worktree"` and that `model`.
- Any other provider (qwen, GLM, DeepSeek, …): **opencode**, not kilo (the maintainer moved from
  kilo to opencode on 2026-09-23). `opencode run` has no directory flag, so start it inside the
  worker's worktree:
  `cd <slot> && opencode run -m '<provider/model>' --auto --format json --title "tabs-intake <repo>" "<brief>"`.
  Look up the exact model id with `opencode models | grep <name>` (e.g.
  `alibaba-token-plan-cn/qwen3.8-flash`). Add a `#<variant>` suffix only if that model has one —
  qwen3.8-flash rejects `#high` and exits in seconds with `Variant unavailable`. A minute in,
  confirm the model actually answering — opencode has been seen to fall back to a default free
  model without saying so. The JSON log carries the `sessionID`; read its model from opencode's
  store: `sqlite3 -readonly ~/.local/share/opencode/opencode.db "select data from session_message
  where session_id='<sessionID>' limit 1"` → `"model":{"id":…,"providerID":…}`.

1. `git -C <slot> add -A && git -C <slot> diff --cached --binary <base> -- . ':(exclude)reports'`
   → `git apply --3way` in the intake worktree. INDEX/README conflicts where both sides appended
   rows: `python3 tools/tab_intake.py union-resolve`; anything else it lists is resolved by hand.
2. `python3 tools/sync_index_health.py --apply && python3 tools/reverse_index.py --write`
   (`reports/` is regenerated here, never taken from a worker), then `make gates`, commit, close.

Lessons from the 2026-09-28/30 run: wrap long runs in `caffeinate -i` (the laptop slept mid-batch);
follow the user's model mix and quota headroom exactly and re-check before each dispatch; a worker
that finishes suspiciously fast or with no result file gets its page read before it is integrated;
workers must run every command in the foreground (a headless session ends when it stops talking).

## Done means

Every ledger row is terminal (`done`/`skipped`/`failed`/`proposed`), every `done` repo's tabs are
closed, `make gates` is green on the branch, the PR is merged or its blocker is named in the report.
