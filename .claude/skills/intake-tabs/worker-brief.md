# Worker brief — one repo, parallel mode

Fill `{{REPO}}`, `{{ACTION}}` (`add` | `sync`), `{{PAGE}}` (sync only), `{{TODAY}}` (UTC),
`{{RESULT}}` (absolute path of the result JSON), `{{BATCH}}` (the other repos in this ledger).
The main session sends everything below the line.

---

You are a worker in the oss-atlas (GitHub-Michelin) repo. Your working directory is a scratch git
worktree nobody else touches. Task: **{{ACTION}}** the selection page for
https://github.com/{{REPO}} ({{PAGE}}), end to end, following this repo's contract.

Read first, in full, and follow exactly: `AGENTS.md`; `.claude/skills/add-project/SKILL.md` (for
`add`) or `.claude/skills/sync-entry/SKILL.md` (for `sync`); `.claude/skills/read-repo/SKILL.md`;
`tools/schema.md` and one golden example it names.

Batch overrides (these win over the skill text):
- Close-the-loop is OFF: do not create pages for comparison alternatives. An unindexed real repo
  stays `未收录` / `not indexed` with "not added in this tab batch" in its tradeoff cell. Grep
  `categories/` first — an indexed alternative must be linked instead.
- These repos are being processed in the same batch — never mark any of them `未收录`:
  {{BATCH}}.
- Full research: `gh api`, raw file reads, README, docs, manifests, releases, issues. Never leave
  `<!-- oss-atlas:unresearched -->`. Unverified claims get `[未验证]`/`[推断]` with the reason and a
  Caveats bullet.
- No Q&A section (there is no reading conversation). `last_verified` = {{TODAY}} (UTC).
- Run the whole procedure including INDEX (EN+ZH), README listing (EN+ZH), upstream snapshot,
  `health.py --write`, `health_card.py`, `flow_card.py`, `sync_index_health.py --apply`,
  `reverse_index.py --write`, and finish with `make gates` green. On a fanout WARN do not refactor;
  report it.
- Do NOT `git commit/push/checkout/reset`, touch anything outside this worktree except the result
  file, or open/close browser tabs.
- Inclusion: security tools, archived, young, hyped repos are all included. Only if the repo turns
  out to be extracted content of a closed product, purely prose/links with no reusable software, an
  exact duplicate, or empty: write no pages and report `propose` with the specific reason.
- Run every command in the foreground and wait for it. This is a one-shot headless session; it ends
  when you stop, and anything still pending is lost.

When finished (success or failure), write `{{RESULT}}`:

```json
{
  "repo": "{{REPO}}",
  "status": "done | failed | propose",
  "category_path": "categories/<...>/<slug>.md",
  "new_category": false,
  "gates": "<last lines of make gates, or the failing error>",
  "fanout_warn": "<fanout/overflow WARN text, else empty>",
  "notes_zh": "<一两句中文：归类理由、值得注意的风险、propose/失败原因>",
  "dotfiles_zh": {
    "fit": "none | low | medium | high",
    "what": "<中文：项目里哪部分机制可能被用户的 ~/.dotfiles（跨 Claude Code / kilo / opencode 的个人 agent harness：skills、hooks、记忆账本、常驻 capsule、模型路由）吸收；none 时一句为什么不相关>",
    "where": "<对应 dotfiles 里的现有 skill/hook/机制，或「新增」>"
  }
}
```

Judge `dotfiles_zh` honestly — most repos are `none` or `low`. Never write it into the pages.
