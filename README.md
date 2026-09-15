# oss-atlas

**A natural-language, agent-first index for open-source *selection* (选型).**
When a coding agent gets a task, it reads this index to pick the right OSS project —
weighing *when NOT to use* each option, not just what it does.

> 中文版 README：[README.zh.md](README.zh.md)

## Install

Install the public oss-atlas selection skills into your coding agent:

- **`select-oss`** — choose an open-source project, library, tool, framework, model, or system.
- **`select-agent-skills`** — choose installable `SKILL.md` packs and agent-skill combinations.

Both skills read the public index over HTTP (no local copy needed) and work in a clone too.

**Any agent, via [skills.sh](https://skills.sh)** (Claude Code, Codex, Cursor, OpenCode, Droid,
Kilo, Gemini CLI, Copilot, and ~70 more — the CLI knows each agent's skills path):

```bash
# Global (all your projects); drop -g for project-local. Pick agents with -a, e.g. -a claude-code
npx skills add ZhenningLang/oss-atlas -g
```

**Manual** (no Node) — copy the skill folder into your agent's skills dir, e.g. Claude Code:

```bash
git clone https://github.com/ZhenningLang/oss-atlas
cp -r oss-atlas/skills/select-oss ~/.claude/skills/
cp -r oss-atlas/skills/select-agent-skills ~/.claude/skills/
```

The skills fetch pages from `raw.githubusercontent.com/ZhenningLang/oss-atlas/main/`; only the
small `SKILL.md` files are installed, so they stay tiny and always read the latest index. For agents
without web access, the skills fall back to a local clone.

Maintainers also have an internal **`project-harvester`** skill in `skills/project-harvester/` for
batch discovery waves. It is marked `metadata.internal: true` and is not part of the normal public
installer surface.

## Projects

The complete index, grouped by category. Each project has an English page (`<slug>.md`) and a Chinese sibling (`<slug>.zh.md`) — click straight through. Browse interactively from [INDEX.md](INDEX.md); agents start at [AGENTS.md](AGENTS.md).

### agent-tooling

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **beads** | Use it when an AI agent loses task state across sessions and you want a versioned, dependency-aware task graph in the repo. | MIT | B (6/6) | [EN](categories/agent-tooling/beads.md) · [中](categories/agent-tooling/beads.zh.md) |
| **CCPM** | Use it when a feature is too big for one session and you want PRD-to-GitHub-Issues specs plus parallel git-worktree agents. | MIT | B (4/6) | [EN](categories/agent-tooling/ccpm.md) · [中](categories/agent-tooling/ccpm.zh.md) |
| **Entire** | Use it when you want AI agent sessions captured as Git checkpoints alongside commits, searchable and rewindable. | MIT | B (5/6) | [EN](categories/agent-tooling/entire-cli.md) · [中](categories/agent-tooling/entire-cli.zh.md) |
| **Ralph for Claude Code** | Use it when you want Claude Code to grind through a fix_plan.md checklist unattended with rate limits, a circuit breaker, and a dual-condition exit gate. | MIT | B (6/6) | [EN](categories/agent-tooling/ralph-claude-code.md) · [中](categories/agent-tooling/ralph-claude-code.zh.md) |
| **Context Mode** | Use it when a coding agent burns context on raw tool output and you want sandboxed execution plus compaction-surviving session memory. | Elastic-2.0 | D (6/6) | [EN](categories/agent-tooling/context-mode.md) · [中](categories/agent-tooling/context-mode.zh.md) |
| **Planning with Files** | Use it when a long agent run keeps losing its plan to /clear, compaction, or crashes. | MIT | B (4/6) | [EN](categories/agent-tooling/planning-with-files.md) · [中](categories/agent-tooling/planning-with-files.zh.md) |
| **Vercel Skills** | Use it when you want an npm-style CLI to install, find, and update SKILL.md packs across many coding agents. | MIT | D (6/6) | [EN](categories/agent-tooling/vercel-skills.md) · [中](categories/agent-tooling/vercel-skills.zh.md) |
| **OpenSandbox** | Use it when you must self-host isolated sandboxes to run untrusted agent-generated code at K8s scale with egress controls and a credential vault — but the repo is only months old (created 2025-12), so its API and Lindy track record are unproven. | Apache-2.0 | B (5/6) | [EN](categories/agent-tooling/opensandbox.md) · [中](categories/agent-tooling/opensandbox.zh.md) |
| **AgentsView** | Use it when you run several coding agents and want local-first cross-agent session search and token/cost analytics — but it's months-old and pre-1.0, expect churn. | MIT | B (6/6) | [EN](categories/agent-tooling/agentsview.md) · [中](categories/agent-tooling/agentsview.zh.md) |
| **Agent Orchestrator** | Use it when you supervise several parallel coding agents on real branches and want a desktop control plane that isolates each in a git worktree and auto-routes CI/review/conflict feedback — but it's ~4.5 months old, pre-1.0, single-User-owned, with a loopback-no-auth daemon. | Apache-2.0 | B (5/6) | [EN](categories/agent-tooling/agent-orchestrator.md) · [中](categories/agent-tooling/agent-orchestrator.zh.md) |
### document-management

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **paperless-ngx** | Use it when you want to self-host OCR + tagging + full-text search over scanned paperwork. | GPL-3.0 | B (5/6) | [EN](categories/document-management/paperless-ngx.md) · [中](categories/document-management/paperless-ngx.zh.md) |
| **copyparty** | Use it when you need a single-file portable file server with resumable uploads, dedup, and multi-protocol access — not OCR document search. | MIT | B (6/6) | [EN](categories/document-management/copyparty.md) · [中](categories/document-management/copyparty.zh.md) |
| **Twake Drive** | Use it when you want a self-hosted Google-Drive-style file network drive inside the Twake/Cozy stack, not OCR archiving. | AGPL-3.0 | B (5/6) | [EN](categories/document-management/twake-drive.md) · [中](categories/document-management/twake-drive.zh.md) |
| **Immich** | Use it when you want a self-hosted Google Photos alternative with AI-powered face/object recognition, smart search, and mobile app sync — but it requires significant server resources (RAM, storage, GPU for ML). | AGPL-3.0 | ? (0/6) | [EN](categories/document-management/immich.md) · [中](categories/document-management/immich.zh.md) |

### on-device-ml

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **LiteRT-LM** | Use it when you want to run Gemma-class LLMs on phone/laptop/edge via Google's LiteRT runtime (CPU/GPU/NPU). | Apache-2.0 | B (6/6) | [EN](categories/on-device-ml/litert-lm.md) · [中](categories/on-device-ml/litert-lm.zh.md) |
| **BitNet** | Use it when you need fast, low-energy CPU inference of natively-trained 1.58-bit ternary LLMs on x86/ARM laptops, offline. | MIT | C (6/6) | [EN](categories/on-device-ml/bitnet.md) · [中](categories/on-device-ml/bitnet.zh.md) |
| **Google AI Edge Gallery** | Use it when you need to demo and benchmark on-device Gemma LLMs on real phones before building. | Apache-2.0 | A (5/6) | [EN](categories/on-device-ml/ai-edge-gallery.md) · [中](categories/on-device-ml/ai-edge-gallery.zh.md) |
| **TimesFM** | Use it when you need zero-shot time-series forecasts run locally on CPU/GPU without per-dataset training. | Apache-2.0 | B (5/6) | [EN](categories/on-device-ml/timesfm.md) · [中](categories/on-device-ml/timesfm.zh.md) |
| **MiniCPM-V** | Use it when you need efficient on-device/edge multimodal (image+video) understanding with a small footprint — verify the per-weight license. | Apache-2.0 | A (4/6) | [EN](categories/on-device-ml/minicpm-v.md) · [中](categories/on-device-ml/minicpm-v.zh.md) |
| **Stable Diffusion WebUI** | Use it when you want a local web-based GUI for Stable Diffusion image generation, editing, and upscaling on your own GPU — but it requires technical setup and an NVIDIA GPU. | AGPL-3.0 | ? (0/6) | [EN](categories/on-device-ml/stable-diffusion-webui.md) · [中](categories/on-device-ml/stable-diffusion-webui.zh.md) |
| **ComfyUI** | The most powerful and modular diffusion model GUI with a node-graph interface for building complex workflows locally — but it has a steep learning curve and requires significant GPU resources. | GPL-3.0 | ? (0/6) | [EN](categories/on-device-ml/comfyui.md) · [中](categories/on-device-ml/comfyui.zh.md) |
| **MLX / mlx-lm** | Run LLMs with MLX | MIT | ? (0/6) | [EN](categories/on-device-ml/mlx-mlx-lm.md) · [中](categories/on-device-ml/mlx-mlx-lm.zh.md) |

### web-automation

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **page-agent** | Use it when you want to control a web UI with natural language in-page via direct DOM read/write, no backend. | MIT | B (6/6) | [EN](categories/web-automation/page-agent.md) · [中](categories/web-automation/page-agent.zh.md) |
| **Chrome DevTools MCP** | Use it when an agent needs to drive and DevTools-inspect real Chrome — traces, network, console, heap. | Apache-2.0 | A (6/6) | [EN](categories/web-automation/chrome-devtools-mcp.md) · [中](categories/web-automation/chrome-devtools-mcp.zh.md) |
| **Cua** | Use it when an agent must control a full desktop OS via vision in isolated VM sandboxes, not just web pages. | MIT | B (6/6) | [EN](categories/web-automation/cua.md) · [中](categories/web-automation/cua.zh.md) |
| **Agent Browser** | Use it when an agent must shell-drive a real Chrome over CDP with stable element refs instead of CSS selectors. | Apache-2.0 | B (6/6) | [EN](categories/web-automation/agent-browser.md) · [中](categories/web-automation/agent-browser.zh.md) |
| **Selenium** | Use it when you need cross-browser WebDriver automation across a browser/language matrix — Playwright/Cypress are nicer for modern single-browser DX. | Apache-2.0 | B (6/6) | [EN](categories/web-automation/selenium.md) · [中](categories/web-automation/selenium.zh.md) |
| **PhantomJS** | Avoid for new work — an archived, abandoned scriptable headless browser; use headless Chrome (Puppeteer/Playwright) or Selenium instead. | BSD-3-Clause | D (5/6) | [EN](categories/web-automation/phantomjs.md) · [中](categories/web-automation/phantomjs.zh.md) |
| **Selenium Wire** | Use it when a legacy Selenium suite needs to read or modify the browser's background HTTP traffic — but it's archived, so new projects should use Selenium 4's native CDP/BiDi or Playwright. | MIT | D (5/6) | [EN](categories/web-automation/selenium-wire.md) · [中](categories/web-automation/selenium-wire.zh.md) |
| **nodriver** | Use it when Python async code needs direct Chromium CDP control without WebDriver — Chromium-only, AGPL-3.0, and not a full test framework. | AGPL-3.0 | C (5/6) | [EN](categories/web-automation/nodriver.md) · [中](categories/web-automation/nodriver.zh.md) |
| **browser-use** | 🌐 Make websites accessible for AI agents. Automate tasks online with ease. | MIT | ? (0/6) | [EN](categories/web-automation/browser-use.md) · [中](categories/web-automation/browser-use.zh.md) |
| **Playwright** | Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API. | Apache-2.0 | ? (0/6) | [EN](categories/web-automation/playwright.md) · [中](categories/web-automation/playwright.zh.md) |
| **Puppeteer** | JavaScript API for Chrome and Firefox | Apache-2.0 | ? (0/6) | [EN](categories/web-automation/puppeteer.md) · [中](categories/web-automation/puppeteer.zh.md) |

### llm-training

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **LlamaFactory** | Zero-code unified fine-tuning framework for 100+ LLMs/VLMs with a Gradio web UI (LlamaBoard), covering LoRA/QLoRA/full tuning and the full SFT→RLHF stack. | Apache-2.0 | B (6/6) | [EN](categories/llm-training/llamafactory.md) · [中](categories/llm-training/llamafactory.zh.md) |
| **Unsloth** | Triton-kernel-accelerated single-GPU LoRA/QLoRA/RL fine-tuning that trains 500+ open LLMs ~2x faster with large VRAM savings. | Apache-2.0 | B (5/6) | [EN](categories/llm-training/unsloth.md) · [中](categories/llm-training/unsloth.zh.md) |
| **ART (Agent Reinforcement Trainer)** | Use it when a Python CLI needs pure-Python figlet-style ASCII text banners with no system binaries — but it's text-to-art only (not image-to-ASCII) and won't match figlet's exact fonts. | Apache-2.0 | B (5/6) | [EN](categories/llm-training/art.md) · [中](categories/llm-training/art.zh.md) |
| **Agent Lightning** | Microsoft RL/optimization trainer that improves agents built in any framework (LangChain, AutoGen, OpenAI SDK…) with near-zero code changes by decoupling agent execution from the training backend. | MIT | C (5/6) | [EN](categories/llm-training/agent-lightning.md) · [中](categories/llm-training/agent-lightning.zh.md) |
| **Colossal-AI** | Use it when you must train/fine-tune large models across many GPUs with tensor/pipeline/ZeRO parallelism — overkill for single-GPU LoRA. | Apache-2.0 | B (5/6) | [EN](categories/llm-training/colossalai.md) · [中](categories/llm-training/colossalai.zh.md) |
| **Hugging Face TRL** | Train transformer language models with reinforcement learning. | Apache-2.0 | ? (0/6) | [EN](categories/llm-training/trl.md) · [中](categories/llm-training/trl.zh.md) |
| **torchtune** | PyTorch native post-training library | BSD-3-Clause | ? (0/6) | [EN](categories/llm-training/torchtune.md) · [中](categories/llm-training/torchtune.zh.md) |
| **Axolotl** | Go ahead and axolotl questions | Apache-2.0 | ? (0/6) | [EN](categories/llm-training/axolotl.md) · [中](categories/llm-training/axolotl.zh.md) |
| **verl** | verl/HybridFlow: A Flexible and Efficient RL Post-Training Framework | Apache-2.0 | ? (0/6) | [EN](categories/llm-training/verl.md) · [中](categories/llm-training/verl.zh.md) |

### agent-frameworks

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **DSPy** | You have eval data and a metric and want optimizers to compile prompts instead of hand-tuning them. | MIT | A (6/6) | [EN](categories/agent-frameworks/workflow-builders/dspy.md) · [中](categories/agent-frameworks/workflow-builders/dspy.zh.md) |
| **AgentScope** | Shipping a production multi-agent LLM service needing sandboxed tools, permissions, tracing, and human-in-the-loop. | Apache-2.0 | B (6/6) | [EN](categories/agent-frameworks/agent-runtimes/agentscope.md) · [中](categories/agent-frameworks/agent-runtimes/agentscope.zh.md) |
| **OpenFang** | You want autonomous agents that run on a schedule from one self-hosted Rust binary. | Apache-2.0 OR MIT | B (5/6) | [EN](categories/agent-frameworks/agent-runtimes/openfang.md) · [中](categories/agent-frameworks/agent-runtimes/openfang.zh.md) |
| **Symphony** | Your Linear backlog and Codex agent need a self-hosted orchestrator running isolated per-issue autonomous implementation runs. | Apache-2.0 | B (5/6) | [EN](categories/agent-frameworks/agent-runtimes/symphony.md) · [中](categories/agent-frameworks/agent-runtimes/symphony.zh.md) |
| **Claude Octopus** | You live in Claude Code and want other AI models to cross-review tasks for blindspots before shipping. | MIT | C (6/6) | [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/claude-octopus.md) · [中](categories/agent-frameworks/coding-agents/orchestration-and-review/claude-octopus.zh.md) |
| **oh-my-claudecode** | You live in Claude Code and need staged multi-agent teams with model routing and tmux parallelism. | MIT | B (5/6) | [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/oh-my-claudecode.md) · [中](categories/agent-frameworks/coding-agents/orchestration-and-review/oh-my-claudecode.zh.md) |
| **smolagents** | Use it when you want a tiny, transparent code-acting agent loop from Hugging Face — not a heavy production agent OS. | Apache-2.0 | B (6/6) | [EN](categories/agent-frameworks/agent-runtimes/smolagents.md) · [中](categories/agent-frameworks/agent-runtimes/smolagents.zh.md) |
| **Kilo Code** | Use it when you want an open, BYOK in-IDE (VS Code) coding agent with planning and modes — an end-user tool, not a library to build agents. | MIT | B (6/6) | [EN](categories/agent-frameworks/coding-agents/ide-agents/kilocode.md) · [中](categories/agent-frameworks/coding-agents/ide-agents/kilocode.zh.md) |
| **Parlant** | Use it when you build a customer-facing agent that must stay on-rails via behavioral guidelines — overkill for simple or free-form agents. | Apache-2.0 | B (6/6) | [EN](categories/agent-frameworks/agent-runtimes/parlant.md) · [中](categories/agent-frameworks/agent-runtimes/parlant.zh.md) |
| **SkillOpt** | Use it when you must optimize an agent's natural-language skill doc for a frozen LLM against a scorable benchmark — but without a reliable eval to gate edits the method has no signal, and it's a brand-new v0.1.0. | MIT | B (6/6) | [EN](categories/agent-frameworks/workflow-builders/skillopt.md) · [中](categories/agent-frameworks/workflow-builders/skillopt.zh.md) |
| **Open Interpreter** | Use it when you want a Codex-fork terminal coding agent with swappable harnesses tuned for low-cost/open models (DeepSeek, Kimi, Qwen) — not the old Python REPL (that moved to a community fork), and it's a weeks-old 0.0.x rewrite that executes code. | Apache-2.0 | A (6/6) | [EN](categories/agent-frameworks/coding-agents/terminal-agents/open-interpreter.md) · [中](categories/agent-frameworks/coding-agents/terminal-agents/open-interpreter.zh.md) |
| **Codex** | Use it when you want a lightweight OpenAI-backed coding agent that runs in your terminal and can edit files, run tests, and commit changes — but it requires OpenAI API access and an internet connection. | Apache-2.0 | ? (0/6) | [EN](categories/agent-frameworks/coding-agents/terminal-agents/codex.md) · [中](categories/agent-frameworks/coding-agents/terminal-agents/codex.zh.md) |
| **OpenClaw** | A personal AI assistant that runs on your own devices and answers you across 20+ messaging channels — but it's extremely young with no Lindy track record. | MIT | ? (0/6) | [EN](categories/agent-frameworks/agent-runtimes/openclaw.md) · [中](categories/agent-frameworks/agent-runtimes/openclaw.zh.md) |
| **CC Switch** | A cross-platform desktop manager for multiple AI coding agents with provider routing and MCP support — but it's under a year old with a single maintainer. | MIT | ? (0/6) | [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/cc-switch.md) · [中](categories/agent-frameworks/coding-agents/orchestration-and-review/cc-switch.zh.md) |
| **Hermes Agent** | The self-improving AI agent built by Nous Research with a learning loop — but it's under a year old and the learning-loop stability is unproven. | MIT | ? (0/6) | [EN](categories/agent-frameworks/agent-runtimes/hermes-agent.md) · [中](categories/agent-frameworks/agent-runtimes/hermes-agent.zh.md) |
| **AutoGPT** | A platform to create, deploy, and manage continuous AI agents that automate complex workflows — but it has no declared license and requires significant resources to self-host. | NOASSERTION | ? (0/6) | [EN](categories/agent-frameworks/workflow-builders/autogpt.md) · [中](categories/agent-frameworks/workflow-builders/autogpt.zh.md) |
| **Dify** | A production-ready visual platform for building agentic workflows with low-code, RAG, and MCP support — but verify the license before commercial use. | NOASSERTION | ? (0/6) | [EN](categories/agent-frameworks/workflow-builders/dify.md) · [中](categories/agent-frameworks/workflow-builders/dify.zh.md) |
| **LangChain** | A code-first framework to compose LLM agents, tools, and memory with a vast integration ecosystem — but avoid for simple single-prompt apps. | MIT | ? (0/6) | [EN](categories/agent-frameworks/workflow-builders/langchain.md) · [中](categories/agent-frameworks/workflow-builders/langchain.zh.md) |
| **OpenCode** | An open-source AI coding agent that runs in your terminal, edits files, and executes commands — but it's extremely young (created 2025-04) with no Lindy track record. | MIT | ? (0/6) | [EN](categories/agent-frameworks/coding-agents/terminal-agents/opencode.md) · [中](categories/agent-frameworks/coding-agents/terminal-agents/opencode.zh.md) |
| **Langflow** | A visual drag-and-drop platform for building and deploying LLM workflows and agents with built-in API and MCP servers — but visual flows are harder to diff/review than code. | MIT | ? (0/6) | [EN](categories/agent-frameworks/workflow-builders/langflow.md) · [中](categories/agent-frameworks/workflow-builders/langflow.zh.md) |
| **Gemini CLI** | An open-source AI agent that brings Gemini power into your terminal with a free tier, built-in tools, and MCP support — but it's Google-only and very young. | Apache-2.0 | ? (0/6) | [EN](categories/agent-frameworks/coding-agents/terminal-agents/gemini-cli.md) · [中](categories/agent-frameworks/coding-agents/terminal-agents/gemini-cli.zh.md) |
| **RTK** | A CLI proxy that compresses shell output before it reaches AI agents, reducing token costs by 60–90% — but extremely young (6 months) with a suspiciously high star count. | Apache-2.0 | ? (0/6) | [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/rtk.md) · [中](categories/agent-frameworks/coding-agents/orchestration-and-review/rtk.zh.md) |
| **CrewAI** | Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks. | MIT | ? (0/6) | [EN](categories/agent-frameworks/agent-runtimes/crewai.md) · [中](categories/agent-frameworks/agent-runtimes/crewai.zh.md) |
| **LangGraph** | Build resilient agents. | MIT | ? (0/6) | [EN](categories/agent-frameworks/agent-runtimes/langgraph.md) · [中](categories/agent-frameworks/agent-runtimes/langgraph.zh.md) |
| **LlamaIndex** | LlamaIndex is the leading document agent and OCR platform | MIT | ? (0/6) | [EN](categories/agent-frameworks/workflow-builders/llamaindex.md) · [中](categories/agent-frameworks/workflow-builders/llamaindex.zh.md) |
| **AutoGen** | A programming framework for agentic AI | CC-BY-4.0 | ? (0/6) | [EN](categories/agent-frameworks/agent-runtimes/autogen.md) · [中](categories/agent-frameworks/agent-runtimes/autogen.zh.md) |
| **Pydantic AI** | AI Agent Framework, the Pydantic way | MIT | ? (0/6) | [EN](categories/agent-frameworks/agent-runtimes/pydantic-ai.md) · [中](categories/agent-frameworks/agent-runtimes/pydantic-ai.zh.md) |
| **OpenAI Agents SDK** | A lightweight, powerful framework for multi-agent workflows | MIT | ? (0/6) | [EN](categories/agent-frameworks/agent-runtimes/openai-agents-sdk.md) · [中](categories/agent-frameworks/agent-runtimes/openai-agents-sdk.zh.md) |
| **aider** | aider is AI pair programming in your terminal | Apache-2.0 | ? (0/6) | [EN](categories/agent-frameworks/coding-agents/terminal-agents/aider.md) · [中](categories/agent-frameworks/coding-agents/terminal-agents/aider.zh.md) |
| **Cline** | Autonomous coding agent as an SDK, IDE extension, or CLI assistant. | Apache-2.0 | ? (0/6) | [EN](categories/agent-frameworks/coding-agents/ide-agents/cline.md) · [中](categories/agent-frameworks/coding-agents/ide-agents/cline.zh.md) |
| **SWE-agent** | SWE-agent takes a GitHub issue and tries to automatically fix it, using your LM of choice. It can also be employed for offensive cybersecurity or competitive coding challenges. [NeurIPS 2024] | MIT | ? (0/6) | [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/swe-agent.md) · [中](categories/agent-frameworks/coding-agents/orchestration-and-review/swe-agent.zh.md) |
| **Flowise** | Build AI Agents, Visually | NOASSERTION | ? (0/6) | [EN](categories/agent-frameworks/workflow-builders/flowise.md) · [中](categories/agent-frameworks/workflow-builders/flowise.zh.md) |
| **OpenHands** | 🙌 OpenHands: AI-Driven Development | NOASSERTION | ? (0/6) | [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/openhands.md) · [中](categories/agent-frameworks/coding-agents/orchestration-and-review/openhands.zh.md) |
| **T3 Code** | Use it when one local GUI should drive already authenticated Codex, Claude, Cursor, and OpenCode CLIs. | MIT | ? (0/6) | [EN](categories/agent-frameworks/coding-agents/terminal-agents/t3code.md) · [中](categories/agent-frameworks/coding-agents/terminal-agents/t3code.zh.md) |
| **Background Agents (Open-Inspect)** | Use it when one trusted organization needs self-hosted background coding-agent sandboxes, integrations, and automation. | MIT | ? (0/6) | [EN](categories/agent-frameworks/coding-agents/orchestration-and-review/background-agents.md) · [中](categories/agent-frameworks/coding-agents/orchestration-and-review/background-agents.zh.md) |

### agent-memory

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Mem0** | Use it when your LLM agent must remember users across sessions without bloating the prompt context. | Apache-2.0 | A (5/6) | [EN](categories/agent-memory/mem0.md) · [中](categories/agent-memory/mem0.zh.md) |
| **Memori** | Use it when you want LLM-agnostic persistent agent memory captured by wrapping your existing client. | Apache-2.0 | B (5/6) | [EN](categories/agent-memory/memori.md) · [中](categories/agent-memory/memori.zh.md) |
| **Claude Subconscious** | Use it when you want a background Letta agent to give Claude Code cross-session memory via hooks. | MIT | C (6/6) | [EN](categories/agent-memory/claude-subconscious.md) · [中](categories/agent-memory/claude-subconscious.zh.md) |
| **claude-mem** | Use it when your coding agent loses context across sessions and you want local hook/MCP-captured memory compressed and injected back in. | Apache-2.0 | B (6/6) | [EN](categories/agent-memory/claude-mem.md) · [中](categories/agent-memory/claude-mem.zh.md) |
| **ByteRover CLI** | Use it when you want a portable, structured memory layer for coding agents with git-like versioning and cloud sync — but it is extremely young (2025-06) and the license is ambiguous. | NOASSERTION | ? (0/6) | [EN](categories/agent-memory/byterover.md) · [中](categories/agent-memory/byterover.zh.md) |
| **Letta (MemGPT)** | Platform for stateful agents: AI with advanced memory that can learn and self-improve over time. | Apache-2.0 | ? (0/6) | [EN](categories/agent-memory/letta.md) · [中](categories/agent-memory/letta.zh.md) |
| **Zep** | Zep \| Examples, Integrations, & More | Apache-2.0 | ? (0/6) | [EN](categories/agent-memory/zep.md) · [中](categories/agent-memory/zep.zh.md) |
| **Graphiti** | Build Real-Time Knowledge Graphs for AI Agents | Apache-2.0 | ? (0/6) | [EN](categories/agent-memory/graphiti.md) · [中](categories/agent-memory/graphiti.zh.md) |
| **LangMem** | Use it when you need LangMem in the agent-memory area. | MIT | ? (0/6) | [EN](categories/agent-memory/langmem.md) · [中](categories/agent-memory/langmem.zh.md) |
| **Cognee** | Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory across sessions with a self-hosted knowledge graph engine. | Apache-2.0 | ? (0/6) | [EN](categories/agent-memory/cognee.md) · [中](categories/agent-memory/cognee.zh.md) |

### deep-research

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **deep-research** | Use it when you want a minimal, readable ~500-LOC TypeScript reference deep-research agent to fork and adapt. | MIT | C (4/6) | [EN](categories/deep-research/deep-research.md) · [中](categories/deep-research/deep-research.zh.md) |
| **Vane** | Use it when you want a self-hosted, privacy-focused Perplexity-style cited answer engine over your own SearxNG and chosen LLM. | MIT | B (5/6) | [EN](categories/deep-research/vane.md) · [中](categories/deep-research/vane.zh.md) |
| **Local Deep Research** | Use it when you need a self-hosted, fully-local deep-research agent that keeps sensitive queries on your own machine. | MIT | B (6/6) | [EN](categories/deep-research/local-deep-research.md) · [中](categories/deep-research/local-deep-research.zh.md) |
| **Agent-Reach** | Use it when your agent needs to read and search web plus social platforms without paid APIs. | MIT | B (5/6) | [EN](categories/deep-research/agent-reach.md) · [中](categories/deep-research/agent-reach.zh.md) |
| **MiroThinker** | Use it when you want a self-hosted, open-weights deep-research agent you can study and extend on your own GPUs — but it needs a GPU cluster plus paid external APIs and is under a year old with no Lindy. | Apache-2.0 | C (6/6) | [EN](categories/deep-research/mirothinker.md) · [中](categories/deep-research/mirothinker.zh.md) |
| **GPT Researcher** | An autonomous agent that conducts deep research on any data using any LLM providers | Apache-2.0 | ? (0/6) | [EN](categories/deep-research/gpt-researcher.md) · [中](categories/deep-research/gpt-researcher.zh.md) |
| **Open Deep Research** | Use it when you need Open Deep Research in the deep-research area. | MIT | ? (0/6) | [EN](categories/deep-research/open-deep-research.md) · [中](categories/deep-research/open-deep-research.zh.md) |
| **STORM** | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. | MIT | ? (0/6) | [EN](categories/deep-research/storm.md) · [中](categories/deep-research/storm.zh.md) |
| **node-DeepResearch** | Keep searching, reading webpages, reasoning until it finds the answer (or exceeding the token budget) | Apache-2.0 | ? (0/6) | [EN](categories/deep-research/node-deepresearch.md) · [中](categories/deep-research/node-deepresearch.zh.md) |

### ai-code-review

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Open Code Review** | Use it when you want precise, line-level LLM review comments on Git diffs in CI without PR noise. | Apache-2.0 | B (6/6) | [EN](categories/ai-code-review/open-code-review.md) · [中](categories/ai-code-review/open-code-review.zh.md) |
| **Claude Code Security Review** | Use it when you want LLM-driven, context-aware security review on trusted PRs via a GitHub Action. | MIT | C (5/6) | [EN](categories/ai-code-review/claude-code-security-review.md) · [中](categories/ai-code-review/claude-code-security-review.zh.md) |
| **React Doctor** | Use it when a coding agent writes React and you want deterministic, repeatable checks for React-specific anti-patterns. | LicenseRef-Modified-MIT | B (5/6) | [EN](categories/ai-code-review/react-doctor.md) · [中](categories/ai-code-review/react-doctor.zh.md) |
| **PR-Agent** | 🚀 PR Agent: The Original Open-Source PR Reviewer.  This project It is not the Qodo free tier. | Apache-2.0 | ? (0/6) | [EN](categories/ai-code-review/pr-agent.md) · [中](categories/ai-code-review/pr-agent.zh.md) |
| **Metis** | Metis is an open-source, AI-driven tool for deep security code review | Apache-2.0 | ? (0/6) | [EN](categories/ai-code-review/metis.md) · [中](categories/ai-code-review/metis.zh.md) |
| **OpenReview** | An open-source, self-hosted AI code review bot powered by Vercel. | NOASSERTION | ? (0/6) | [EN](categories/ai-code-review/openreview.md) · [中](categories/ai-code-review/openreview.zh.md) |

### rag-retrieval

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **FalkorDB** | Use it when GraphRAG needs vector similarity plus multi-hop graph traversal in one low-latency Redis-embedded engine. | SSPL-1.0 | D (5/6) | [EN](categories/rag-retrieval/falkordb.md) · [中](categories/rag-retrieval/falkordb.zh.md) |
| **graphify** | Use it when an agent needs to query a whole repo's code, schemas and docs as a knowledge graph instead of grepping. | MIT | B (6/6) | [EN](categories/rag-retrieval/graphify.md) · [中](categories/rag-retrieval/graphify.zh.md) |
| **code-review-graph** | Use it when an AI reviewer keeps burning context on a large repo and you want only the blast-radius files. | MIT | B (6/6) | [EN](categories/rag-retrieval/code-review-graph.md) · [中](categories/rag-retrieval/code-review-graph.zh.md) |
| **PageIndex** | Use it when vector RAG returns similar-but-irrelevant chunks over a few long, structured documents needing auditable citations. | MIT | B (5/6) | [EN](categories/rag-retrieval/pageindex.md) · [中](categories/rag-retrieval/pageindex.zh.md) |
| **Understand-Anything** | Use it when you want any codebase turned into an explorable, queryable knowledge graph for an agent — younger and less proven than graphify. | MIT | B (6/6) | [EN](categories/rag-retrieval/understand-anything.md) · [中](categories/rag-retrieval/understand-anything.zh.md) |
| **FAISS** | Use it when you need a fast in-process ANN vector index for embeddings — a library, not a managed vector DB. | MIT | A (6/6) | [EN](categories/rag-retrieval/faiss.md) · [中](categories/rag-retrieval/faiss.zh.md) |
| **text2vec** | Use it when you need Chinese-first sentence embeddings for semantic search or FAQ matching from a single pip install — it's only the encoder, so bring your own vector index (FAISS/Milvus). | Apache-2.0 | C (5/6) | [EN](categories/rag-retrieval/text2vec.md) · [中](categories/rag-retrieval/text2vec.zh.md) |
| **SCIP** | SCIP Code Intelligence Protocol | Apache-2.0 | ? (0/6) | [EN](categories/rag-retrieval/scip.md) · [中](categories/rag-retrieval/scip.zh.md) |
| **Milvus** | Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search | Apache-2.0 | ? (0/6) | [EN](categories/rag-retrieval/milvus.md) · [中](categories/rag-retrieval/milvus.zh.md) |
| **Sourcegraph** | Code AI platform with Code Search & Cody | NOASSERTION | ? (0/6) | [EN](categories/rag-retrieval/sourcegraph.md) · [中](categories/rag-retrieval/sourcegraph.zh.md) |

### llm-eval

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **promptfoo** | Use it when you need declarative YAML evals plus red-teaming for your LLM app in CI. | MIT | A (6/6) | [EN](categories/llm-eval/promptfoo.md) · [中](categories/llm-eval/promptfoo.zh.md) |
| **Pezzo** | Use it when a small team wants one self-hosted control plane for prompt versioning plus cost/latency observability — but it looks stalled since mid-2025, so assume you'll maintain it yourself. | Apache-2.0 | C (4/6) | [EN](categories/llm-eval/pezzo.md) · [中](categories/llm-eval/pezzo.zh.md) |
| **DeepEval** | The LLM Evaluation Framework | Apache-2.0 | ? (0/6) | [EN](categories/llm-eval/deepeval.md) · [中](categories/llm-eval/deepeval.zh.md) |
| **Ragas** | Supercharge Your LLM Application Evaluations 🚀 | Apache-2.0 | ? (0/6) | [EN](categories/llm-eval/ragas.md) · [中](categories/llm-eval/ragas.zh.md) |
| **garak** | the LLM vulnerability scanner | Apache-2.0 | ? (0/6) | [EN](categories/llm-eval/garak.md) · [中](categories/llm-eval/garak.zh.md) |
| **Giskard OSS** | 🐢 Open-Source Evaluation & Testing library for LLM Agents | Apache-2.0 | ? (0/6) | [EN](categories/llm-eval/giskard.md) · [中](categories/llm-eval/giskard.zh.md) |
| **Langfuse** | 🪢 Open source AI engineering platform: LLM evals, observability, metrics, prompt management, playground, datasets. Integrates with OpenTelemetry, LangChain, OpenAI SDK, LiteLLM, and more. 🍊YC W23 | NOASSERTION | ? (0/6) | [EN](categories/llm-eval/langfuse.md) · [中](categories/llm-eval/langfuse.zh.md) |

### agent-dev-methodology

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **12-Factor Agents** | Use it when you want production-agent design principles to guide a hand-rolled or thinly-framed agent. | CC-BY-SA-4.0 (content) / Apache-2.0 (code examples) | C (3/6) | [EN](categories/agent-dev-methodology/12-factor-agents.md) · [中](categories/agent-dev-methodology/12-factor-agents.zh.md) |
| **Superpowers** | Use it when you want a drop-in brainstorm→plan→TDD→verify SDLC methodology installed into your coding agent. | MIT | B (4/6) | [EN](categories/agent-dev-methodology/superpowers.md) · [中](categories/agent-dev-methodology/superpowers.zh.md) |
| **SuperClaude Framework** | Use it when you live in Claude Code and want a ready-made command, agent, and behavioral-mode framework installed at once. | MIT | B (6/6) | [EN](categories/agent-dev-methodology/superclaude.md) · [中](categories/agent-dev-methodology/superclaude.zh.md) |
| **Get Shit Done (GSD)** | Use it when you build through a coding agent and want a spec-driven, fresh-context phase pipeline that fights context rot. | MIT | C (6/6) | [EN](categories/agent-dev-methodology/get-shit-done.md) · [中](categories/agent-dev-methodology/get-shit-done.zh.md) |
| **Compound Engineering** | Use it when you want a turnkey brainstorm→plan→work→review→compound loop that persists learnings across coding-agent sessions. | MIT | B (4/6) | [EN](categories/agent-dev-methodology/compound-engineering.md) · [中](categories/agent-dev-methodology/compound-engineering.zh.md) |
| **ECC** | Use it when you want a maintained, batteries-included Claude Code harness of skills, agents, hooks, memory, and a security scanner. | MIT | B (6/6) | [EN](categories/agent-dev-methodology/ecc.md) · [中](categories/agent-dev-methodology/ecc.zh.md) |
| **Spec Kit** | A spec-driven development methodology from GitHub for AI coding agents — but it is extremely young and tightly coupled to the GitHub ecosystem. | MIT | ? (0/6) | [EN](categories/agent-dev-methodology/spec-kit.md) · [中](categories/agent-dev-methodology/spec-kit.zh.md) |
| **Spec-Anchored Agentic Development** | Use it when permanent capability specs must remain the code-conformance oracle — Claude Code-specific and only days old. | MIT | B (3/6) | [EN](categories/agent-dev-methodology/spec-anchored-agentic-development.md) · [中](categories/agent-dev-methodology/spec-anchored-agentic-development.zh.md) |
| **USDAD** | Use it when you want a prose-first multi-agent spec and context method to adapt manually — it has no CLI or executable enforcement. | MIT | C (4/6) | [EN](categories/agent-dev-methodology/usdad.md) · [中](categories/agent-dev-methodology/usdad.zh.md) |
| **QUAD Framework** | Use it only to study a docs-first four-Circles operating model and deployment blueprint — it is inactive, proprietary, and partly inaccessible. | Proprietary | D (3/6) | [EN](categories/agent-dev-methodology/quad.md) · [中](categories/agent-dev-methodology/quad.zh.md) |
| **LTBL Experiment** | Use it only as an index to three agent-context experiment implementations — it has no runnable code, results, or license grant. | NOASSERTION | D (4/6) | [EN](categories/agent-dev-methodology/ltbl-experiment.md) · [中](categories/agent-dev-methodology/ltbl-experiment.zh.md) |
| **PURE** | Use it when intent traceability needs Git-native schemas, registries, phase gates, and Shell checks — structured, but very young. | MIT | C (5/6) | [EN](categories/agent-dev-methodology/pure-agentic.md) · [中](categories/agent-dev-methodology/pure-agentic.zh.md) |
| **Learn Claude Code** | Use it when you want to learn how a Claude Code–style agent harness works by rebuilding all 17 mechanisms yourself in runnable Python — but it's a course, not a library or production CLI. | MIT | B (5/6) | [EN](categories/agent-dev-methodology/learn-claude-code.md) · [中](categories/agent-dev-methodology/learn-claude-code.zh.md) |

### ai-design-generation

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **HTML Anything** | Use it when you already run a logged-in coding-agent CLI and want local-first, key-free Markdown-to-shippable-HTML generation with one-click WeChat/X/Zhihu export. | Apache-2.0 | B (5/6) | [EN](categories/ai-design-generation/html-anything.md) · [中](categories/ai-design-generation/html-anything.zh.md) |
| **Open Design** | Use it when you want a local-first, BYOK desktop studio that makes your coding agent generate HTML prototypes, decks, images and HTML→MP4. | Apache-2.0 | B (4/6) | [EN](categories/ai-design-generation/open-design.md) · [中](categories/ai-design-generation/open-design.zh.md) |
| **Impeccable** | Use it when your AI agent keeps shipping same-looking frontend slop and you want deterministic detection plus design critique. | Apache-2.0 | B (6/6) | [EN](categories/ai-design-generation/impeccable.md) · [中](categories/ai-design-generation/impeccable.zh.md) |
| **ian-xiaohei-illustrations** | Use it when you need consistent hand-drawn 16:9 Chinese article illustrations with a fixed IP. | MIT | C (4/6) | [EN](categories/agent-skills/visual-content/ian-illustrations.md) · [中](categories/agent-skills/visual-content/ian-illustrations.zh.md) |
| **Guizang PPT Skill** | Use it when you want an agent to turn an article into a designed single-file HTML swipe deck. | AGPL-3.0-only | C (4/6) | [EN](categories/agent-skills/slides-ppt/guizang-ppt.md) · [中](categories/agent-skills/slides-ppt/guizang-ppt.zh.md) |
| **Guizang Social Card Skill** | Use it when a coding agent needs art-directed Xiaohongshu carousels or WeChat cover pairs as single-file HTML rendered to PNG. | AGPL-3.0-only | D (3/6) | [EN](categories/agent-skills/visual-content/guizang-social-card.md) · [中](categories/agent-skills/visual-content/guizang-social-card.zh.md) |
| **SdPaint** | Use it when you already run AUTOMATIC1111 + ControlNet and want a live sketch-to-image painting loop — but it's stalled since 2024 and provides no model of its own. | MIT | D (3/6) | [EN](categories/ai-design-generation/sdpaint.md) · [中](categories/ai-design-generation/sdpaint.zh.md) |
### dev-utilities

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **DevToys** | Use it when you want offline, local-only dev utilities (Base64/JSON/hash/diff) in one cross-platform desktop app instead of untrusted online tools. | MIT | B (4/6) | [EN](categories/dev-utilities/data-tools/devtoys.md) · [中](categories/dev-utilities/data-tools/devtoys.zh.md) |
| **CyberChef** | Use it when you need to chain encode/decode, crypto, compression and data-analysis transforms offline in your browser. | Apache-2.0 | B (6/6) | [EN](categories/dev-utilities/data-tools/cyberchef.md) · [中](categories/dev-utilities/data-tools/cyberchef.zh.md) |
| **Cockpit** | Use it when you need a browser-based, systemd-native admin UI for a few Linux servers. | LGPL-2.1-or-later | D (5/6) | [EN](categories/dev-utilities/ops-infra/cockpit.md) · [中](categories/dev-utilities/ops-infra/cockpit.zh.md) |
| **Telegraf** | Use it when you need one plugin-driven agent to collect and route heterogeneous metrics/logs to many backends. | MIT | A (5/6) | [EN](categories/dev-utilities/ops-infra/telegraf.md) · [中](categories/dev-utilities/ops-infra/telegraf.zh.md) |
| **OpenZL** | Use it when you must squeeze terabytes of one highly structured/numeric format better than generic zstd. | BSD-3-Clause | B (4/6) | [EN](categories/dev-utilities/data-tools/openzl.md) · [中](categories/dev-utilities/data-tools/openzl.zh.md) |
| **Certbot** | Use it when a sysadmin must auto-provision & renew free Let's Encrypt TLS certs — though reverse proxies' built-in auto-TLS often makes it redundant. | Apache-2.0 | A (5/6) | [EN](categories/dev-utilities/ops-infra/certbot.md) · [中](categories/dev-utilities/ops-infra/certbot.zh.md) |
| **tqdm** | Use it when you want a fast, low-overhead progress bar for Python loops/CLI/notebooks. | MPL-2.0 AND MIT | B (5/6) | [EN](categories/dev-utilities/data-tools/tqdm.md) · [中](categories/dev-utilities/data-tools/tqdm.zh.md) |
| **SlimToolkit** | Use it when you want to auto-minify & harden a bloated container image without rewriting the Dockerfile — beware it can strip dynamically-loaded files. | Apache-2.0 | B (5/6) | [EN](categories/dev-utilities/ops-infra/slim.md) · [中](categories/dev-utilities/ops-infra/slim.zh.md) |
| **Faker (faker-js)** | Use it when you need realistic fake/mock data (names, addresses, finance…) for tests and seeding in JS/TS. | MIT | A (5/6) | [EN](categories/dev-utilities/data-tools/faker-js.md) · [中](categories/dev-utilities/data-tools/faker-js.zh.md) |
| **fontTools** | Use it when you need programmatic font surgery — subset webfonts, convert formats, inspect/patch tables — but it edits font files, it won't design glyphs or shape text. | MIT | A (6/6) | [EN](categories/dev-utilities/data-tools/fonttools.md) · [中](categories/dev-utilities/data-tools/fonttools.zh.md) |
| **Flashlight** | Use it when you're keeping a vintage macOS 10.10–10.15 machine and want Spotlight plugins — but it's abandoned since 2020 and requires disabling SIP, avoid on real machines. | MIT AND GPL-2.0-only (component split) | E (3/6) | [EN](categories/dev-utilities/data-tools/flashlight.md) · [中](categories/dev-utilities/data-tools/flashlight.zh.md) |
| **IdeaVim** | Use it when you live in a JetBrains IDE but want Vim motions, modes, and a `.ideavimrc` — but it's an emulation subset, power users will hit fidelity gaps. | MIT | B (5/6) | [EN](categories/dev-utilities/editors-and-runtimes/ideavim.md) · [中](categories/dev-utilities/editors-and-runtimes/ideavim.zh.md) |
| **VS Code** | A fast, cross-platform code editor with intelligent completion, debugging, and the largest extension marketplace — but it's Electron-based and the distributed build includes Microsoft telemetry. | MIT | ? (0/6) | [EN](categories/dev-utilities/editors-and-runtimes/vscode.md) · [中](categories/dev-utilities/editors-and-runtimes/vscode.zh.md) |
| **Clash Verge Rev** | A modern cross-platform GUI proxy client with rule-based routing, built-in mihomo kernel, and TUN mode — but it's desktop-only and GPL-3.0 licensed. | GPL-3.0 | ? (0/6) | [EN](categories/dev-utilities/ops-infra/clash-verge-rev.md) · [中](categories/dev-utilities/ops-infra/clash-verge-rev.zh.md) |
| **RustDesk** | An open-source, self-hosted remote desktop application for accessing your own machines across platforms — but it requires managing your own relay server or accepting P2P limitations. | AGPL-3.0 | ? (0/6) | [EN](categories/dev-utilities/ops-infra/rustdesk.md) · [中](categories/dev-utilities/ops-infra/rustdesk.zh.md) |
| **Tauri** | Build smaller, faster, and more secure desktop and mobile applications with a web frontend using Rust and native OS webviews instead of Electron. | Apache-2.0 | ? (0/6) | [EN](categories/dev-utilities/editors-and-runtimes/tauri.md) · [中](categories/dev-utilities/editors-and-runtimes/tauri.zh.md) |
| **Deno** | A modern runtime for JavaScript, TypeScript, and WebAssembly with secure defaults and built-in tooling — no node_modules, but smaller ecosystem than Node.js. | MIT | ? (0/6) | [EN](categories/dev-utilities/editors-and-runtimes/deno.md) · [中](categories/dev-utilities/editors-and-runtimes/deno.zh.md) |
| **Vaultwarden** | An unofficial Bitwarden-compatible server written in Rust for self-hosted password management — unofficial, AGPL-3.0, single-core maintainer. | AGPL-3.0 | ? (0/6) | [EN](categories/dev-utilities/ops-infra/vaultwarden.md) · [中](categories/dev-utilities/ops-infra/vaultwarden.zh.md) |
| **Zed** | A high-performance, native code editor with real-time multiplayer collaboration from the creators of Atom — but far smaller extension ecosystem than VS Code and only ~4 years old. | NOASSERTION | ? (0/6) | [EN](categories/dev-utilities/editors-and-runtimes/zed.md) · [中](categories/dev-utilities/editors-and-runtimes/zed.zh.md) |
| **ripgrep** | A fast, gitignore-aware line-oriented search tool with first-class cross-platform support; 10 years old with strong Lindy signal and single-maintainer reliability. | Unlicense | ? (0/6) | [EN](categories/dev-utilities/data-tools/ripgrep.md) · [中](categories/dev-utilities/data-tools/ripgrep.zh.md) |
| **Bun** | An incredibly fast all-in-one JavaScript/TypeScript toolkit (runtime, bundler, test runner, package manager) in a single binary — but verify the custom license before commercial use. | NOASSERTION | ? (0/6) | [EN](categories/dev-utilities/editors-and-runtimes/bun.md) · [中](categories/dev-utilities/editors-and-runtimes/bun.zh.md) |
| **fzf** | :cherry_blossom: A command-line fuzzy finder | MIT | ? (0/6) | [EN](categories/dev-utilities/data-tools/fzf.md) · [中](categories/dev-utilities/data-tools/fzf.zh.md) |
| **jq** | Command-line JSON processor | NOASSERTION | ? (0/6) | [EN](categories/dev-utilities/data-tools/jq.md) · [中](categories/dev-utilities/data-tools/jq.zh.md) |

### frontend-animation

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Anime.js** | Dependency-free JS animation engine: CSS, SVG, DOM attrs and JS objects through one animate() API, with timeline, stagger, spring easings, and scroll-linked playback. | MIT | B (6/6) | [EN](categories/frontend-animation/anime.md) · [中](categories/frontend-animation/anime.zh.md) |

### api-gateway

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Kong Gateway** | OpenResty/Nginx API gateway whose plugin layer makes one reverse-proxy a programmable edge for REST/microservice traffic and, since 3.x, LLM/MCP traffic. | Apache-2.0 | A (5/6) | [EN](categories/api-gateway/kong.md) · [中](categories/api-gateway/kong.zh.md) |
| **Funtool** | Use it only for the exact Windows + Claude Code + NVIDIA proxy path — the current executable is opaque and cannot be rebuilt from the published source. | MIT | C (5/6) | [EN](categories/api-gateway/funtool.md) · [中](categories/api-gateway/funtool.zh.md) |

### geospatial

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **QGIS** | Full-featured cross-platform desktop GIS (Qt/C++) to view, edit, analyze and publish vector/raster/mesh/point-cloud spatial data, with PyQGIS plugins and a headless server. | GPL-2.0-or-later | A (5/6) | [EN](categories/geospatial/qgis.md) · [中](categories/geospatial/qgis.zh.md) |

### team-chat

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **HiveChat** | Self-hostable, admin-managed AI chat for small/medium teams: one admin wires many LLM providers; the team chats with per-group model access and token quotas. | Apache-2.0 | C (3/6) | [EN](categories/team-chat/hivechat.md) · [中](categories/team-chat/hivechat.zh.md) |

### captcha

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Cap** | Lightweight self-hosted CAPTCHA alternative: an invisible proof-of-work challenge (SHA-256 nonce in a Rust→WASM worker) issuing a server-verifiable token — no images, no third-party calls. | Apache-2.0 | B (5/6) | [EN](categories/captcha/capjs.md) · [中](categories/captcha/capjs.zh.md) |
| **Text_select_captcha** | Use it when automating Chinese click-to-select-text CAPTCHAs (YOLO + Siamese, CPU-only) — there's no LICENSE file, so all rights reserved and legality is the decisive filter. | NONE (no LICENSE file — all rights reserved) | D (5/6) | [EN](categories/captcha/text-select-captcha.md) · [中](categories/captcha/text-select-captcha.zh.md) |
| **pytorch-captcha-recognition** | Use it as a readable teaching baseline for fixed-length text-in-image CAPTCHAs via a multi-head CNN — it's a frozen 2020 tutorial, expect to modernize the dated PyTorch APIs. | Apache-2.0 | D (4/6) | [EN](categories/captcha/pytorch-captcha-recognition.md) · [中](categories/captcha/pytorch-captcha-recognition.zh.md) |
| **captcha (lepture)** | Use it when a Python web form needs a self-hosted image/audio CAPTCHA renderer with no third-party call — it's render-only and weak against modern OCR, treat it as a UX speed-bump, not security. | BSD-3-Clause | B (5/6) | [EN](categories/captcha/lepture-captcha.md) · [中](categories/captcha/lepture-captcha.zh.md) |
| **NopeCHA** | Use it only for authorized unattended automation across several CAPTCHA families — the maintained implementation is closed and depends on a hosted API. | MIT | B (6/6) | [EN](categories/captcha/nopecha-extension.md) · [中](categories/captcha/nopecha-extension.zh.md) |
| **Buster** | Use it for human-triggered reCAPTCHA audio accessibility or authorized testing — source-auditable and local-capable, but narrow and nondeterministic. | GPL-3.0-only | B (5/6) | [EN](categories/captcha/buster.md) · [中](categories/captcha/buster.zh.md) |

### blockchain-dev-infrastructure

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **PoWFaucet** | Use it when a public EVM testnet needs a faucet with modular anti-abuse controls — you still own hot-wallet custody, funding, and high service operations. | AGPL-3.0 | B (5/6) | [EN](categories/blockchain-dev-infrastructure/powfaucet.md) · [中](categories/blockchain-dev-infrastructure/powfaucet.zh.md) |
### ml-research

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **autoresearch** | Self-contained single-GPU LLM training harness so an AI agent can iterate on train.py overnight — 5-minute experiments scored by validation bits-per-byte, keeping only loss-lowering changes. | MIT | D (5/6) | [EN](categories/ml-research/autoresearch.md) · [中](categories/ml-research/autoresearch.zh.md) |
| **llm-circuit-finder** | Python toolkit that searches a GGUF model for contiguous reasoning-circuit layer blocks and duplicates them in the forward pass (no training, no weight edits), validated with built-in probes. | MIT | D (5/6) | [EN](categories/ml-research/llm-circuit-finder.md) · [中](categories/ml-research/llm-circuit-finder.zh.md) |
| **CLIP** | Use it when you need zero-shot image classification or image↔text retrieval embeddings — the original frozen reference; OpenCLIP has more checkpoints. | MIT | C (5/6) | [EN](categories/ml-research/clip.md) · [中](categories/ml-research/clip.zh.md) |
| **TaskMatrix** | Use it only to study an early visual-tool-routing agent (Visual ChatGPT) — abandoned since ~2024, don't build on it. | MIT | ? (2/6) | [EN](categories/ml-research/taskmatrix.md) · [中](categories/ml-research/taskmatrix.zh.md) |
| **PyTorch-GAN** | Read it to learn GAN architectures from clean reference implementations — idle since 2024 and superseded by diffusion; not production code. | MIT | D (4/6) | [EN](categories/ml-research/pytorch-gan.md) · [中](categories/ml-research/pytorch-gan.zh.md) |
| **LSTM Neural Network for Time Series Prediction** | Use it as a readable article-companion example for learning Keras LSTM time-series forecasting — pinned to EOL TF1/Python 3.5 and AGPL-3.0, re-implement from the article rather than vendoring. | AGPL-3.0 | E (4/6) | [EN](categories/ml-research/lstm-time-series.md) · [中](categories/ml-research/lstm-time-series.zh.md) |
| **Agriculture Knowledge Graph (AgriKG)** | Use it as a complete blueprint and bundled datasets for a Chinese domain knowledge-graph pipeline (NER, RE, Neo4j, Django) — author-declared unmaintained on a dated GPL-3.0 stack, lift techniques not code. | GPL-3.0 | D (3/6) | [EN](categories/ml-research/agriculture-knowledge-graph.md) · [中](categories/ml-research/agriculture-knowledge-graph.zh.md) |
| **Senta (SKEP)** | Use it when working inside PaddlePaddle/ERNIE and needing SKEP sentiment checkpoints with a published method — pinned to EOL PaddlePaddle 1.6.3, so environment archaeology is unavoidable. | Apache-2.0 | D (3/6) | [EN](categories/ml-research/senta.md) · [中](categories/ml-research/senta.zh.md) |
| **Depth Anything V2** | Use it as the current default monocular-depth foundation model for single-image depth in PyTorch/Transformers — only the Small weights are Apache-2.0; Base/Large/Giant are CC-BY-NC-4.0 (non-commercial). | Apache-2.0 | B (4/6) | [EN](categories/ml-research/depth-anything-v2.md) · [中](categories/ml-research/depth-anything-v2.zh.md) |
| **pymoo** | Use it as the de-facto Python library for evolutionary multi-objective optimization (NSGA-II/III, MOEA/D) to find Pareto fronts — for convex/linear/single-objective problems an LP/gradient solver is far faster. | Apache-2.0 | C (6/6) | [EN](categories/ml-research/pymoo.md) · [中](categories/ml-research/pymoo.zh.md) |
### agent-skills

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **book-to-skill** | Use it when you want to turn technical book PDFs (and other document formats) into installable agent skills for Claude Code, Copilot CLI, or Amp. | MIT | ? (0/6) | [EN](categories/agent-skills/book-to-skill.md) · [中](categories/agent-skills/book-to-skill.zh.md) |

#### agent-skills / engineering

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Agent Skills (addyosmani)** | A curated pack of ~24 production-engineering skills (quality, security, web-perf, API, ship) installed into your coding agent and routed through ~8 SDLC slash commands. | MIT | B (4/6) | [EN](categories/agent-skills/engineering/addyosmani-agent-skills.md) · [中](categories/agent-skills/engineering/addyosmani-agent-skills.zh.md) |
| **web-quality-skills** | A six-skill agent pack encoding Lighthouse / Core Web Vitals / WCAG / SEO best practices as on-demand instruction sets so a coding agent can audit and fix web-quality issues; advisory, not a measurement tool. | MIT | B (4/6) | [EN](categories/agent-skills/engineering/addyosmani-web-quality.md) · [中](categories/agent-skills/engineering/addyosmani-web-quality.zh.md) |
| **Scientific Agent Skills** | A large skill pack (~147 skills) that turns a coding agent into a research assistant for biology, chemistry, medicine, and drug discovery — each skill wraps a scientific Python library or database with a documented SKILL.md loaded on demand. | MIT | B (4/6) | [EN](categories/agent-skills/engineering/scientific-agent-skills.md) · [中](categories/agent-skills/engineering/scientific-agent-skills.zh.md) |
| **Vercel Agent Skills** | Vercel's official agent-skill pack — install-on-demand React/Next.js/Vercel deploy, web-design, and docs audit guides in the agentskills.io/skills.sh format. | MIT | B (4/6) | [EN](categories/agent-skills/engineering/vercel-agent-skills.md) · [中](categories/agent-skills/engineering/vercel-agent-skills.zh.md) |
| **Waza** | A compact collection of eight "engineering habit" skills (plan, design, review, debug, write, research, read, audit) a coding agent loads on demand across Claude Code, Codex, and Cursor. | MIT | B (4/6) | [EN](categories/agent-skills/engineering/waza.md) · [中](categories/agent-skills/engineering/waza.zh.md) |

#### agent-skills / design

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Designer Skills** | A broad design-practice skill pack — 97 skills and 30 commands across 9 plugins (research, design systems, UX strategy, UI, interaction, prototyping/testing, design ops, toolkit, visual critique) for Claude Code and Gemini CLI. | MIT | B (4/6) | [EN](categories/agent-skills/design/designer-skills.md) · [中](categories/agent-skills/design/designer-skills.zh.md) |
| **Skills For Design Engineers** | Emil Kowalski's six-skill design-engineering pack for UI motion, animation vocabulary, Apple-style interface principles, strict animation review, and animation improvement planning. | MIT | B (4/6) | [EN](categories/agent-skills/design/emilkowalski-skills.md) · [中](categories/agent-skills/design/emilkowalski-skills.zh.md) |
| **make-interfaces-feel-better** | A single, focused agent skill that injects ~16 concrete UI-polish principles (concentric radius, interruptible transitions, tabular numbers, enter/exit animation) so a coding agent ships interfaces that feel finished, not merely correct. | MIT | D (4/6) | [EN](categories/agent-skills/design/make-interfaces-feel-better.md) · [中](categories/agent-skills/design/make-interfaces-feel-better.zh.md) |
| **Stitch Skills** | A library of Agent Skills (open standard) that drive Google's Stitch MCP server to generate UI screens, convert code↔design, extract DESIGN.md, and export React/React Native/shadcn components. | Apache-2.0 | B (4/6) | [EN](categories/agent-skills/design/stitch-skills.md) · [中](categories/agent-skills/design/stitch-skills.zh.md) |
| **Taste-Skill** | A portable, framework-agnostic agent skill pack that gives coding agents visual taste — stopping generic AI-slop frontends and pushing intentional layout, typography, motion, and spacing. | MIT | B (4/6) | [EN](categories/agent-skills/design/taste-skill.md) · [中](categories/agent-skills/design/taste-skill.zh.md) |
| **UI UX Pro Max Skill** | A design-intelligence skill pack that gives a coding agent UI/UX taste via a local CSV-backed retrieval engine (style/palette/font/rule databases) plus a pre-delivery accessibility checklist, installed across many agent harnesses. | MIT | B (4/6) | [EN](categories/agent-skills/design/ui-ux-pro-max.md) · [中](categories/agent-skills/design/ui-ux-pro-max.zh.md) |
| **Hallmark** | Use it when a Claude Code, Cursor, or Codex agent needs an opinionated anti-slop design brief, audit, redesign, or study workflow. | MIT | ? (0/6) | [EN](categories/agent-skills/design/hallmark.md) · [中](categories/agent-skills/design/hallmark.zh.md) |

#### agent-skills / writing

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Baoyu Skills** | A 20+ skill pack for coding agents (translation, markdown/HTML formatting, transcript/URL capture, image/diagram/slide generation), installable into Claude Code, Codex, and other skill-capable harnesses. | MIT | B (4/6) | [EN](categories/agent-skills/writing/baoyu-skills.md) · [中](categories/agent-skills/writing/baoyu-skills.zh.md) |
| **Humanizer-zh** | A single Chinese Claude Code skill that rewrites text to strip ~24 tell-tale AI-writing patterns; a localization of blader/humanizer. | MIT | C (4/6) | [EN](categories/agent-skills/de-ai-writing/humanizer-zh.md) · [中](categories/agent-skills/de-ai-writing/humanizer-zh.zh.md) |
| **Webnovel Writer** | Use it when a Claude Code serial novel needs chapters, facts, retrieval, reviews, and summaries to stay consistent over a long run. | GPL-3.0 | B (5/6) | [EN](categories/agent-skills/writing/webnovel-writer.md) · [中](categories/agent-skills/writing/webnovel-writer.zh.md) |

#### agent-skills / security

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Anthropic Cybersecurity Skills** | A large (~817 skill) cybersecurity skill pack of SKILL.md runbooks cross-mapped to MITRE ATT&CK, NIST CSF, ATLAS, D3FEND, NIST AI RMF and MITRE F3, loaded on demand into a coding agent. | Apache-2.0 | B (4/6) | [EN](categories/agent-skills/security/anthropic-cybersecurity-skills.md) · [中](categories/agent-skills/security/anthropic-cybersecurity-skills.zh.md) |

#### agent-skills / context-engineering

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Agent Skills for Context Engineering** | A 15-skill Claude Code plugin pack teaching context-engineering discipline: fundamentals, degradation, compression, multi-agent coordination, memory, tool design, evaluation, and harness engineering. | MIT | B (4/6) | [EN](categories/agent-skills/context-engineering/context-engineering-skills.md) · [中](categories/agent-skills/context-engineering/context-engineering-skills.zh.md) |
| **NotebookLM Claude Code Skill** | A Claude Code skill that drives real Chrome to query your Google NotebookLM notebooks, returning source-grounded, citation-backed answers from your own docs instead of file-reading or hallucinating. | MIT | C (4/6) | [EN](categories/agent-skills/context-engineering/notebooklm-skill.md) · [中](categories/agent-skills/context-engineering/notebooklm-skill.zh.md) |

#### agent-skills / vendor-collections

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Anthropic Skills** | Anthropic's official public collection of Agent Skills — self-contained SKILL.md folders (document editing, design, MCP/skill authoring, comms) installable into Claude Code, Claude.ai, or the Claude API. | Apache-2.0 | B (4/6) | [EN](categories/agent-skills/vendor-collections/anthropic-skills.md) · [中](categories/agent-skills/vendor-collections/anthropic-skills.zh.md) |
| **Agent Plugins for AWS** | AWS Labs' official collection of nine agent plugins (serverless, Amplify, SageMaker, migration, databases, deploy/cost-estimate, etc.) that teach Claude Code / Cursor / Codex to architect, deploy, and operate on AWS via marketplace-installed, trigger-phrase skills wired to AWS MCP servers. | Apache-2.0 | A (4/6) | [EN](categories/agent-skills/vendor-collections/aws-agent-plugins.md) · [中](categories/agent-skills/vendor-collections/aws-agent-plugins.zh.md) |
| **Claude Plugins (Official)** | Anthropic's first-party Claude Code plugin marketplace: a curated directory of installable plugins (commands, agents, skills, MCP servers) installed by name via the native /plugin system. | Apache-2.0 | B (4/6) | [EN](categories/agent-skills/vendor-collections/claude-plugins-official.md) · [中](categories/agent-skills/vendor-collections/claude-plugins-official.zh.md) |
| **MiniMax Skills** | MiniMax's official ~16-skill Agent Skills bundle (frontend/mobile/shader dev plus pdf/docx/xlsx/pptx, music & multimodal generation), installable into Claude Code and other coding agents via plugin marketplace. | MIT | B (4/6) | [EN](categories/agent-skills/vendor-collections/minimax-skills.md) · [中](categories/agent-skills/vendor-collections/minimax-skills.zh.md) |
| **Anthropic Knowledge Work Plugins** | Use it when you want Anthropic's official open-source plugins aimed at knowledge work (docs, comms, research) for Claude — very young. | Apache-2.0 | B (4/6) | [EN](categories/agent-skills/vendor-collections/knowledge-work-plugins.md) · [中](categories/agent-skills/vendor-collections/knowledge-work-plugins.zh.md) |

#### agent-skills / subagent-collections

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Agency-Agents** | A curated collection of ~232 specialized subagent personas (markdown) across 16 functional divisions, with install/convert scripts that deploy them into Claude Code and ~11 other agent harnesses. | MIT | B (4/6) | [EN](categories/agent-skills/subagent-collections/agency-agents.md) · [中](categories/agent-skills/subagent-collections/agency-agents.zh.md) |
| **awesome-claude-code-subagents** | A curated bundle of 100+ specialized Claude Code subagent definitions (one markdown persona per role) you drop into ~/.claude/agents/ so Claude Code can delegate to a domain expert. | MIT | A (4/6) | [EN](categories/agent-skills/subagent-collections/awesome-claude-code-subagents.md) · [中](categories/agent-skills/subagent-collections/awesome-claude-code-subagents.zh.md) |
| **wshobson/agents** | Large single-maintainer multi-harness plugin marketplace (~194 subagents, ~158 skills, ~106 commands, ~16 orchestrators) authored once in Markdown and generated into harness-native artifacts for Claude Code, Codex CLI, Cursor, OpenCode, Gemini CLI and Copilot. | MIT | B (4/6) | [EN](categories/agent-skills/subagent-collections/wshobson-agents.md) · [中](categories/agent-skills/subagent-collections/wshobson-agents.zh.md) |

#### agent-skills / personal-collections

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **antfu/skills** | Anthony Fu's personal curated agent-skill collection for the Vue/Vite/Nuxt stack (his ESLint/pnpm/Vitest/UnoCSS prefs + generated/vendored framework skills), installed via the skills CLI. | MIT | B (4/6) | [EN](categories/agent-skills/personal-collections/engineering-workflows/antfu-skills.md) · [中](categories/agent-skills/personal-collections/engineering-workflows/antfu-skills.zh.md) |
| **claude-code-harness** | A personal Claude Code harness that installs a governed plan → work → review → release loop (spec-first contracts, TDD-gated execution, independent review) as a plugin, with a Go-native doctor CLI for diagnosing plugin-cache and skill drift. | MIT | B (4/6) | [EN](categories/agent-skills/personal-collections/engineering-workflows/claude-code-harness.md) · [中](categories/agent-skills/personal-collections/engineering-workflows/claude-code-harness.zh.md) |
| **dbskill** | A personal, curated pack of ~21 Chinese-language agent skills (/dbs-*) for business-model diagnosis, content creation, and personal decision-making, installable into Claude Code and other harnesses. | CC-BY-NC-4.0 | C (3/6) | [EN](categories/agent-skills/personal-collections/knowledge-content/dbskill.md) · [中](categories/agent-skills/personal-collections/knowledge-content/dbskill.zh.md) |
| **Dimillian Skills** | One developer's personal collection of 16 self-contained Codex skills, heavily focused on Apple-platform work (SwiftUI/iOS/macOS) plus generic review/refactor swarms. | MIT | C (4/6) | [EN](categories/agent-skills/personal-collections/engineering-workflows/dimillian-skills.md) · [中](categories/agent-skills/personal-collections/engineering-workflows/dimillian-skills.zh.md) |
| **gstack** | Garry Tan's personal Claude Code setup: ~23 opinionated slash-command skills that role-play a virtual engineering team (CEO review, designer, eng-manager, QA, security officer) across a plan-build-review-ship-retro loop. | MIT | B (4/6) | [EN](categories/agent-skills/personal-collections/engineering-workflows/gstack.md) · [中](categories/agent-skills/personal-collections/engineering-workflows/gstack.zh.md) |
| **andrej-karpathy-skills** | A single behavioral-guidelines pack — one CLAUDE.md (plus a Cursor variant and a thin skills wrapper) distilling Karpathy's four LLM-coding principles (Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution) into Claude Code / Cursor. | MIT | C (4/6) | [EN](categories/agent-skills/personal-collections/engineering-workflows/karpathy-skills.md) · [中](categories/agent-skills/personal-collections/engineering-workflows/karpathy-skills.zh.md) |
| **Khazix Skills** | A small personal collection of five SKILL.md-format Agent Skills from 数字生命卡兹克 (Khazix) — disk cleanup, AI-news lookup, doc/memory reconciliation, long-form research reports, and WeChat-style writing — for SKILL.md-capable agents. | MIT | B (4/6) | [EN](categories/agent-skills/personal-collections/knowledge-content/khazix-skills.md) · [中](categories/agent-skills/personal-collections/knowledge-content/khazix-skills.zh.md) |
| **ljg-skills** | Li Jigang's personal Claude Code skill collection (20+ skills) for Chinese knowledge work — reading, paper/book deconstruction, concept analysis, plain-language rewriting, and rendering content into visual PNG cards, installed via the skills CLI. | NOASSERTION | C (4/6) | [EN](categories/agent-skills/personal-collections/knowledge-content/ljg-skills.md) · [中](categories/agent-skills/personal-collections/knowledge-content/ljg-skills.zh.md) |
| **PUA** | A high-agency persona skill pack that frames your coding agent as a P8 engineer on a 30-day PIP, using corporate-PUA/PIP rhetoric to push it to exhaust debugging approaches instead of giving up early. | MIT | C (4/6) | [EN](categories/agent-skills/personal-collections/engineering-workflows/pua.md) · [中](categories/agent-skills/personal-collections/engineering-workflows/pua.zh.md) |
| **Qiushi-Skill** | A methodology skill pack arming a coding agent with "seek truth from facts" plus nine dialectical-materialist thinking tools (contradiction analysis, investigation-first, practice-cognition, etc.), installable across Claude Code/Cursor/Codex/OpenCode via an npx installer. | MIT | B (4/6) | [EN](categories/agent-skills/personal-collections/engineering-workflows/qiushi-skill.md) · [中](categories/agent-skills/personal-collections/engineering-workflows/qiushi-skill.zh.md) |
| **shaping-skills** | Ryan Singer's personal Claude Code skill pack that brings Shape Up "shaping" — problem framing, breadboarding, and framing/kickoff docs — into your coding agent so the AI helps define what to build before any code is written. | NOASSERTION | D (4/6) | [EN](categories/agent-skills/personal-collections/engineering-workflows/shaping-skills.md) · [中](categories/agent-skills/personal-collections/engineering-workflows/shaping-skills.zh.md) |
| **TÂCHES CC Resources** | A personal, opinionated Claude Code bundle from TÂCHES (glittercowboy): ~27 slash commands, 9 skills (mostly meta-generators for building new commands/skills/subagents/hooks/MCP servers), 3 auditor subagents, and hooks — installable as one marketplace plugin. | MIT | C (4/6) | [EN](categories/agent-skills/personal-collections/engineering-workflows/taches-cc-resources.md) · [中](categories/agent-skills/personal-collections/engineering-workflows/taches-cc-resources.zh.md) |
| **skills** | Sahil Lavingia's Claude Code skill pack translating The Minimalist Entrepreneur journey into 10 business-building commands. | NOASSERTION | C (4/6) | [EN](categories/agent-skills/personal-collections/knowledge-content/slavingia-skills.md) · [中](categories/agent-skills/personal-collections/knowledge-content/slavingia-skills.zh.md) |
| **canghe-skills** | Canghe's personal Claude Code skills marketplace for content publishing, image/video generation backends, business intelligence, extraction utilities, Obsidian helpers, Remotion guidance, and document parsing. | NOASSERTION | D (4/6) | [EN](categories/agent-skills/personal-collections/knowledge-content/canghe-skills.md) · [中](categories/agent-skills/personal-collections/knowledge-content/canghe-skills.zh.md) |
| **huashu-skills** | 花叔的内容创作 Skills 合集 - AI审校、选题生成、视频大纲、素材搜索等 11 个实用技能 | NOASSERTION | D (4/6) | [EN](categories/agent-skills/writing/huashu-skills.md) · [中](categories/agent-skills/writing/huashu-skills.zh.md) |
| **De-AI-Prompt-Enhancer-Writer-Booster-SKILL** | Chinese de-AI writing prompt suite packaged as two SKILL-format folders: `de-AI-writing/SKILL.md` for AI-tone cleanup and `good-writing/SKILL.md` for stronger author-style reconstruction. | NOASSERTION | C (4/6) | [EN](categories/agent-skills/de-ai-writing/de-ai-prompt-enhancer-writer-booster-skill.md) · [中](categories/agent-skills/de-ai-writing/de-ai-prompt-enhancer-writer-booster-skill.zh.md) |
| **chatgpt-comparison-detection** | Human ChatGPT Comparison Corpus (HC3), Detectors, and more! 🔥 | NOASSERTION | ? (0/6) | [EN](categories/llm-eval/chatgpt-comparison-detection.md) · [中](categories/llm-eval/chatgpt-comparison-detection.zh.md) |
| **writing-agent** | 🚀 一个基于 Claude Code (Skills + Subagents) 的“去AI味”全栈写作系统。不仅防套路，更通过专属规则强制注入人类观点与细节，搭配读者测试评估与自动图文排版。全面支持 DeepSeek / 智谱GLM / MiniMax 等国产低成本大模型，提供从选题、风格建模到审稿发布的高维全自动写作工作流。 | MIT | B (4/6) | [EN](categories/agent-skills/writing/writing-agent.md) · [中](categories/agent-skills/writing/writing-agent.zh.md) |
| **nuwa-skill** | 你想蒸馏的下一个员工，何必是同事。蒸馏任何人的思维方式——心智模型、决策启发式、表达DNA。Distill how anyone thinks. | MIT | B (4/6) | [EN](categories/agent-skills/context-engineering/nuwa-skill.md) · [中](categories/agent-skills/context-engineering/nuwa-skill.zh.md) |
| **shuorenhua** | 说人话｜中文优先的去 AI 味改写 skill：保事实、分场景、改完可直接发。Chinese-first rewrite skill for Codex / Claude Code / Cursor / ChatGPT — removes AI tone, preserves facts. | MIT | B (4/6) | [EN](categories/agent-skills/de-ai-writing/shuorenhua.md) · [中](categories/agent-skills/de-ai-writing/shuorenhua.zh.md) |
| **ai-flavor-remover** | Single-file Chinese prompt snippet for removing “AI flavor”, with the upstream README saying it was only tested on Gemini 2.5 Pro. | NOASSERTION | D (4/6) | [EN](categories/agent-skills/de-ai-writing/ai-flavor-remover.md) · [中](categories/agent-skills/de-ai-writing/ai-flavor-remover.zh.md) |
| **stop-slop** | A skill file for removing AI tells from prose | MIT | B (4/6) | [EN](categories/agent-skills/de-ai-writing/stop-slop.md) · [中](categories/agent-skills/de-ai-writing/stop-slop.zh.md) |
| **humanizer** | Claude Code skill that removes signs of AI-generated writing from text | MIT | B (4/6) | [EN](categories/agent-skills/de-ai-writing/humanizer.md) · [中](categories/agent-skills/de-ai-writing/humanizer.zh.md) |
| **cangjie-skill** | Methodology skill for distilling books, long videos, podcasts, courses, interviews, and transcripts into reusable, testable agent skill packs. | MIT | B (4/6) | [EN](categories/agent-skills/context-engineering/cangjie-skill.md) · [中](categories/agent-skills/context-engineering/cangjie-skill.zh.md) |
| **archify** | Any agent Skill: generate beautiful architecture diagrams with dark/light theme toggle and PNG/JPEG/WebP/SVG export | MIT | B (4/6) | [EN](categories/agent-skills/design/archify.md) · [中](categories/agent-skills/design/archify.zh.md) |
| **mattpocock/skills** | Matt Pocock's engineering skill pack for Claude Code and skills.sh: grilling, domain docs, TDD, bug diagnosis, architecture, review, tickets, and implementation flow. | MIT | B (4/6) | [EN](categories/agent-skills/engineering/mattpocock-skills.md) · [中](categories/agent-skills/engineering/mattpocock-skills.zh.md) |
| **BrowserAct Skills** | Agent-facing browser automation skill pack for BrowserAct: indexed browser control, stealth/private sessions, remote human handoff, and Skill Forge scraping workflows. | MIT | B (4/6) | [EN](categories/agent-skills/engineering/browser-act-skills.md) · [中](categories/agent-skills/engineering/browser-act-skills.zh.md) |
| **caveman** | Prompt and installer pack that makes many coding agents answer in deliberately terse "caveman" style while preserving code, commands, and errors. | MIT | B (4/6) | [EN](categories/agent-skills/engineering/caveman.md) · [中](categories/agent-skills/engineering/caveman.zh.md) |
| **open-seo** | Open source alternative to Semrush and Ahrefs | MIT | B (5/6) | [EN](categories/agent-skills/writing/open-seo.md) · [中](categories/agent-skills/writing/open-seo.zh.md) |
| **ai-website-cloner-template** | Clone any website with one command using AI coding agents | MIT | B (4/6) | [EN](categories/agent-skills/design/ai-website-cloner-template.md) · [中](categories/agent-skills/design/ai-website-cloner-template.zh.md) |
| **huashu-design** | Huashu Design · HTML-native design skill for Claude Code · Claude Code 里 HTML 原生的设计 skill · 高保真原型 / 幻灯片 / 动画 + 20 设计哲学 + 5 维评审 + MP4 导出 · Agent-agnostic | MIT | B (4/6) | [EN](categories/agent-skills/design/huashu-design.md) · [中](categories/agent-skills/design/huashu-design.zh.md) |
| **ppt-master** | AI generates a real, editable PowerPoint from any document — native shapes & animations, editable charts & tables you can change the data on, speaker notes voiced as audio narration, and the option to follow your own .pptx template, not slide images · by Hugo He | MIT | B (3/6) | [EN](categories/agent-skills/slides-ppt/ppt-master.md) · [中](categories/agent-skills/slides-ppt/ppt-master.zh.md) |
| **frontend-slides** | Create beautiful slides on the web using a coding agent's frontend skills | MIT | B (4/6) | [EN](categories/agent-skills/slides-ppt/frontend-slides.md) · [中](categories/agent-skills/slides-ppt/frontend-slides.zh.md) |
| **html-ppt-skill** | HTML PPT Studio — AgentSkill with 36 themes, 15 full-deck templates, 31 layouts, 47 animations, and presenter mode for building professional static HTML presentations. | MIT | B (4/6) | [EN](categories/agent-skills/slides-ppt/html-ppt-skill.md) · [中](categories/agent-skills/slides-ppt/html-ppt-skill.zh.md) |
| **tacit-mining** | Let AI truly understand you. A Claude Code skill that extracts tacit knowledge through structured dialogue. 隐性知识挖掘技能。 | NOASSERTION | D (4/6) | [EN](categories/agent-skills/context-engineering/tacit-mining.md) · [中](categories/agent-skills/context-engineering/tacit-mining.zh.md) |
| **soul.md** | The best way to build a personality for your agent. Let Claude Code / OpenClaw ingest your data & build your AI soul. | MIT | B (4/6) | [EN](categories/agent-skills/context-engineering/soul-md.md) · [中](categories/agent-skills/context-engineering/soul-md.zh.md) |
| **marketingskills** | Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering. | MIT | B (4/6) | [EN](categories/agent-skills/writing/marketingskills.md) · [中](categories/agent-skills/writing/marketingskills.zh.md) |

### observability

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Grafana** | Use it when you need one dashboard + alerting layer over Prometheus/Loki/Elasticsearch and other sources — it visualizes, it doesn't store. | AGPL-3.0 | B (5/6) | [EN](categories/observability/grafana.md) · [中](categories/observability/grafana.zh.md) |
| **Prometheus** | The Prometheus monitoring system and time series database. | Apache-2.0 | ? (0/6) | [EN](categories/observability/prometheus.md) · [中](categories/observability/prometheus.zh.md) |
| **OpenTelemetry Collector** | OpenTelemetry Collector | Apache-2.0 | ? (0/6) | [EN](categories/observability/opentelemetry-collector.md) · [中](categories/observability/opentelemetry-collector.zh.md) |
| **Loki** | Like Prometheus, but for logs. | AGPL-3.0 | ? (0/6) | [EN](categories/observability/loki.md) · [中](categories/observability/loki.zh.md) |
| **Jaeger** | CNCF Jaeger, a Distributed Tracing Platform | Apache-2.0 | ? (0/6) | [EN](categories/observability/jaeger.md) · [中](categories/observability/jaeger.zh.md) |

### data-visualization

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Apache Superset** | Use it when you want self-hosted SQL BI dashboards and exploration over a warehouse — not infra metrics/observability. | Apache-2.0 | A (6/6) | [EN](categories/data-visualization/superset.md) · [中](categories/data-visualization/superset.zh.md) |
| **Evidence** | Business intelligence as code: build fast, interactive data visualizations in SQL and markdown | MIT | ? (0/6) | [EN](categories/data-visualization/evidence.md) · [中](categories/data-visualization/evidence.zh.md) |
| **Metabase** | The easy-to-use open source Business Intelligence and Embedded Analytics tool that lets everyone work with data :bar_chart: | NOASSERTION | ? (0/6) | [EN](categories/data-visualization/metabase.md) · [中](categories/data-visualization/metabase.zh.md) |

### ocr

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Tesseract** | Use it when you need offline, embeddable OCR over clean printed text in 100+ languages — not wild photos or handwriting. | Apache-2.0 | A (5/6) | [EN](categories/ocr/tesseract.md) · [中](categories/ocr/tesseract.zh.md) |
| **LaTeX-OCR (pix2tex)** | Use it when you must convert images of math equations into LaTeX (pix2tex) — equations only, idle/coasting, and VLMs may beat it. | MIT | C (3/6) | [EN](categories/ocr/latex-ocr.md) · [中](categories/ocr/latex-ocr.zh.md) |
| **Laravel OCR** | Use it when a Laravel app needs one wrapper for local and cloud OCR plus template field extraction — PDF/layout handling is shallow and the repo lacks a license file. | NOASSERTION | D (5/6) | [EN](categories/ocr/laravel-ocr.md) · [中](categories/ocr/laravel-ocr.zh.md) |

### document-parsing

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Docling** | Use it when you must parse messy PDF/DOCX/PPTX into clean structured Markdown/JSON for RAG ingestion — a parser, not a DMS. | MIT | A (5/6) | [EN](categories/document-parsing/docling.md) · [中](categories/document-parsing/docling.zh.md) |
| **MarkItDown** | Use it when you need a lightweight Python library to convert various office documents and files to Markdown for LLM ingestion — simpler than Docling but less layout-aware. | MIT | ? (0/6) | [EN](categories/document-parsing/markitdown.md) · [中](categories/document-parsing/markitdown.zh.md) |
| **olmOCR** | Use it when you must convert complex PDFs with equations, tables, handwriting, and multi-column layouts into clean Markdown for LLM training datasets — requires a GPU. | Apache-2.0 | ? (0/6) | [EN](categories/document-parsing/olmocr.md) · [中](categories/document-parsing/olmocr.zh.md) |
| **Marker** | Convert PDF to markdown + JSON quickly with high accuracy | GPL-3.0 | ? (0/6) | [EN](categories/document-parsing/marker.md) · [中](categories/document-parsing/marker.zh.md) |
| **unstructured** | Convert documents to structured data effortlessly. Unstructured is open-source ETL solution for transforming complex documents into clean, structured formats for language models.  Visit our website to learn more about our enterprise grade Platform product for production grade workflows, partitioning, enrichments, chunking and embedding. | Apache-2.0 | ? (0/6) | [EN](categories/document-parsing/unstructured.md) · [中](categories/document-parsing/unstructured.zh.md) |
| **any2html** | Use it when you need any2html in the document-parsing area. | NOASSERTION | ? (0/6) | [EN](categories/document-parsing/any2html.md) · [中](categories/document-parsing/any2html.zh.md) |
| **Dedoc** | Use it when mixed PDF and Office archives must become logical trees with tables and attachments — broad local parsing, but with heavy Linux and system-package dependencies. | Apache-2.0 | A (5/6) | [EN](categories/document-parsing/dedoc.md) · [中](categories/document-parsing/dedoc.zh.md) |
| **Bella Domify** | Use it when a Python RAG pipeline needs detailed PDF/Office DOM trees and optional vision OCR — license conflict and provider/infrastructure coupling raise adoption cost. | GPL-2.0-only | D (5/6) | [EN](categories/document-parsing/bella-domify.md) · [中](categories/document-parsing/bella-domify.zh.md) |
| **MinerU Skill** | Use it when an agent needs one-command cloud document-to-Markdown with batch, resume, and delivery — files leave your environment and quality depends on MinerU. | MIT | C (5/6) | [EN](categories/document-parsing/mineru-skill.md) · [中](categories/document-parsing/mineru-skill.zh.md) |

### diagramming

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Mermaid** | Use it when you want diagrams as version-controlled plain text (flowchart/sequence/ER) rendered in Markdown and docs — not pixel-precise layouts. | MIT | A (6/6) | [EN](categories/diagramming/mermaid.md) · [中](categories/diagramming/mermaid.zh.md) |
| **flowchart.js** | Use it when you want simple flowcharts authored as git-diffable text and rendered to SVG in the browser — but it only renders, depends on aging Raphael.js, and chokes on complex diagrams. | MIT | B (5/6) | [EN](categories/diagramming/flowchart-js.md) · [中](categories/diagramming/flowchart-js.zh.md) |
| **bpmn-js** | Use it when business analysts must author or view standards-correct BPMN 2.0 diagrams inside your web app — but its license mandates a non-removable bpmn.io watermark, so confirm terms before white-labeling. | MIT + bpmn.io watermark clause | B (5/6) | [EN](categories/diagramming/bpmn-js.md) · [中](categories/diagramming/bpmn-js.zh.md) |
| **Excalidraw** | A virtual whiteboard for sketching hand-drawn style diagrams — collaborative and end-to-end encrypted, but stores JSON not plain text, so it is not diffable in Git. | MIT | ? (0/6) | [EN](categories/diagramming/excalidraw.md) · [中](categories/diagramming/excalidraw.zh.md) |
### media-download

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **youtube-dl** | Use it when you need a battle-tested CLI/library to download video & audio from YouTube and 1000+ sites — but prefer the active yt-dlp fork for hot sites. | Unlicense | B (5/6) | [EN](categories/media-download/youtube-dl.md) · [中](categories/media-download/youtube-dl.zh.md) |
| **you-get** | Use it when you want a tiny Python CLI to grab video/audio from YouTube and many Chinese sites (Bilibili/Youku) — lighter than yt-dlp. | MIT | D (3/6) | [EN](categories/media-download/you-get.md) · [中](categories/media-download/you-get.zh.md) |
| **cobalt** | Use it when you want a clean self-hostable web-UI + API media saver with no ads/trackers — not a scriptable CLI. | AGPL-3.0 | B (5/6) | [EN](categories/media-download/cobalt.md) · [中](categories/media-download/cobalt.zh.md) |
| **lux** | Use it when you want a fast single-binary Go downloader, strong on Chinese video sites — smaller coverage and slower updates than yt-dlp. | MIT | B (5/6) | [EN](categories/media-download/lux.md) · [中](categories/media-download/lux.zh.md) |
| **youtube-transcript-api** | Use it when you need timestamped YouTube transcripts key-free for a RAG/summarization pipeline — but it rides an undocumented endpoint that can break anytime, and cloud/datacenter IPs now require paid residential proxies. | MIT | A (6/6) | [EN](categories/media-download/youtube-transcript-api.md) · [中](categories/media-download/youtube-transcript-api.zh.md) |
| **bulk-downloader-for-reddit** | Use it when you want a scriptable, reproducible Reddit archive of files plus metadata via OAuth — but Reddit's ~1000-post listing cap is unbypassable, and releases have stalled since early 2023 (GPL-3.0). | GPL-3.0 | D (5/6) | [EN](categories/media-download/bulk-downloader-for-reddit.md) · [中](categories/media-download/bulk-downloader-for-reddit.zh.md) |
| **yt-dlp** | Use it when you need an actively maintained CLI to download video & audio from YouTube and thousands of other sites — the de-facto successor to youtube-dl with faster fixes and more features. | Unlicense | ? (0/6) | [EN](categories/media-download/yt-dlp.md) · [中](categories/media-download/yt-dlp.zh.md) |
| **gallery-dl** | Command-line program to download image galleries and collections from several image hosting sites | GPL-2.0 | ? (0/6) | [EN](categories/media-download/gallery-dl.md) · [中](categories/media-download/gallery-dl.zh.md) |

### media-processing

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **FFmpeg** | Use it when you must decode/encode/transcode/filter virtually any audio or video in a pipeline — mind the LGPL→GPL build trap. | LGPL-2.1-or-later | A (3/6) | [EN](categories/media-processing/video-audio/ffmpeg.md) · [中](categories/media-processing/video-audio/ffmpeg.zh.md) |
| **HandBrake** | Use it when you need a preset-driven GUI or CLI to rip/transcode video to modern MP4/MKV with H.264/H.265 — but it's an end-user app, not a library, and far narrower than raw FFmpeg. | GPL-2.0-or-later | — | [EN](categories/media-processing/video-audio/handbrake.md) · [中](categories/media-processing/video-audio/handbrake.zh.md) |
| **ffmpeg-python** | Use it when you're scripting complex FFmpeg filter graphs in Python and want readable DAG code instead of write-only -filter_complex strings — but it's coasting since 2024, single-maintainer, and still needs the ffmpeg binary installed. | Apache-2.0 | C (4/6) | [EN](categories/media-processing/video-audio/ffmpeg-python.md) · [中](categories/media-processing/video-audio/ffmpeg-python.zh.md) |
| **PyAV** | Use it when you need programmatic, in-process access to video/audio frames as NumPy arrays from Python — but it's lower-level than a CLI wrapper and heavier to install (Cython compilation against FFmpeg headers). | MIT | — | [EN](categories/media-processing/video-audio/pyav.md) · [中](categories/media-processing/video-audio/pyav.zh.md) |
| **VMAF** | Use it when you're tuning an encoding ladder and need a perceptual 0-100 score to compare codecs/presets the way the industry does — but it's full-reference only, and picking the wrong model silently invalidates cross-version comparisons. | BSD-2-Clause-Patent | B (5/6) | [EN](categories/media-processing/quality-metrics/vmaf.md) · [中](categories/media-processing/quality-metrics/vmaf.zh.md) |
| **SSIMULACRA2** | Use it when you're benchmarking image codecs (JPEG XL, AVIF, WebP) and need a perceptual quality score that correlates with human subjective ratings — but it's image-only, asymmetric, and lacks the adoption of VMAF. | MIT | — | [EN](categories/media-processing/quality-metrics/ssimulacra2.md) · [中](categories/media-processing/quality-metrics/ssimulacra2.zh.md) |
| **m3u8** | Use it when you must parse or rewrite HLS .m3u8 manifests programmatically as a typed object model rather than regex — but it's Python-only, HLS-specific, and quiet since 2025 so the newest rfc8216bis tags may lag. | MIT | C (3/6) | [EN](categories/media-processing/video-audio/m3u8.md) · [中](categories/media-processing/video-audio/m3u8.zh.md) |
| **ffsubsync** | Use it when a subtitle file is off by a constant global offset and you want one-command FFT audio-sync without manual sync points — but it can't fix per-line/variable drift inside the content, and it's single-maintainer. | MIT | B (6/6) | [EN](categories/media-processing/video-audio/ffsubsync.md) · [中](categories/media-processing/video-audio/ffsubsync.zh.md) |
| **MoviePy** | Use it when you want a friendly Python API for programmatic video editing — cutting, compositing, text, effects — but it's batch-only, slower than raw FFmpeg for large files, and maintenance has slowed from its peak. | MIT | ? (0/6) | [EN](categories/media-processing/video-audio/moviepy.md) · [中](categories/media-processing/video-audio/moviepy.zh.md) |
| **GStreamer** | Use it when you need a real-time, persistent, application-embedded audio/video pipeline framework — not a CLI tool — but accept a steep learning curve and plugin-dependency management. | LGPL-2.1-or-later | — | [EN](categories/media-processing/video-audio/gstreamer.md) · [中](categories/media-processing/video-audio/gstreamer.zh.md) |
| **MLT** | Use it when you're building a custom video editor or automated editing pipeline that needs a timeline model — but it's a framework, not a ready-to-use NLE, and delegates all codec work to FFmpeg. | LGPL-2.1-or-later | — | [EN](categories/media-processing/video-audio/mlt.md) · [中](categories/media-processing/video-audio/mlt.zh.md) |
| **OpenAI Whisper** | Use it when you need general-purpose multilingual speech-to-text transcription or translation to English from audio/video files — but it's not real-time by default, large models are slow on CPU, and it hallucinates on non-speech content. | MIT | — | [EN](categories/media-processing/video-audio/whisper.md) · [中](categories/media-processing/video-audio/whisper.zh.md) |
| **sharp** | High performance Node.js image processing, the fastest module to resize JPEG, PNG, WebP, AVIF and TIFF images. Uses the libvips library. | Apache-2.0 | ? (0/6) | [EN](categories/media-processing/image-processing/sharp.md) · [中](categories/media-processing/image-processing/sharp.zh.md) |
| **ImageMagick** | ImageMagick is a free, open-source software suite for creating, editing, converting, and displaying images. It supports 200+ formats and offers powerful command-line tools and APIs for automation, scripting, and integration across platforms. | NOASSERTION | ? (0/6) | [EN](categories/media-processing/image-processing/imagemagick.md) · [中](categories/media-processing/image-processing/imagemagick.zh.md) |
| **Screenshot Service** | Use it only as an isolated internal HTML-to-image worker — API authentication is disabled and Chromium runs without its sandbox or web security. | NOASSERTION | D (4/6) | [EN](categories/media-processing/image-processing/screenshot-service.md) · [中](categories/media-processing/image-processing/screenshot-service.zh.md) |

### video-production

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **OpenMontage** | Use it when you want an AI coding assistant to produce full videos — explainers, trailers, animations, or documentary montages — from a plain-language prompt through research, scripting, asset generation, and render. | AGPL-3.0 | C (6/6) | [EN](categories/video-production/open-montage.md) · [中](categories/video-production/open-montage.zh.md) |
| **claude-video** | Give Claude the ability to watch any video. /watch downloads, extracts frames, transcribes, hands it all to Claude. | MIT | C (4/6) | [EN](categories/media-processing/video-audio/claude-video.md) · [中](categories/media-processing/video-audio/claude-video.zh.md) |

### llm-chat-ui

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **NextChat** | Use it when you want a private, self-deployable multi-provider AI chat UI across web/desktop/mobile — not a multi-user RBAC team platform. | MIT | B (5/6) | [EN](categories/llm-chat-ui/nextchat.md) · [中](categories/llm-chat-ui/nextchat.zh.md) |
| **Open WebUI** | A self-hosted AI chat platform with built-in RAG, Ollama support, and offline operation — but it's single-user-shaped by default. | NOASSERTION | ? (0/6) | [EN](categories/llm-chat-ui/open-webui.md) · [中](categories/llm-chat-ui/open-webui.zh.md) |
| **LibreChat** | Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active | MIT | ? (0/6) | [EN](categories/llm-chat-ui/librechat.md) · [中](categories/llm-chat-ui/librechat.zh.md) |

### markdown-tools

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **CommonMark** | Use it when you need the canonical, spec-compliant Markdown reference implementation with a traversable AST — but not for speed, GFM, or a plugin ecosystem. | BSD-3-Clause | — | [EN](categories/markdown-tools/commonmark.md) · [中](categories/markdown-tools/commonmark.zh.md) |
| **Markdown Here** | Use it when you want to write email in Markdown and render it before sending via a browser/Thunderbird extension — mind its slow maintenance. | MIT | C (4/6) | [EN](categories/markdown-tools/markdown-here.md) · [中](categories/markdown-tools/markdown-here.zh.md) |
| **marked** | Use it when you need a fast, low-level Markdown→HTML parser in JS — but you must sanitize the output yourself and don't need strict CommonMark. | MIT | A (5/6) | [EN](categories/markdown-tools/marked.md) · [中](categories/markdown-tools/marked.zh.md) |
| **remark** | Use it when you need a full mdast AST pipeline for parsing, transforming, linting, and serializing Markdown — but it's a toolchain, not a one-call renderer. | MIT | — | [EN](categories/markdown-tools/remark.md) · [中](categories/markdown-tools/remark.zh.md) |
| **markdown-it** | Use it when you need a strict CommonMark/GFM-compliant, pluggable Markdown→HTML parser in JS — but the plugin ecosystem adds weight and you must still sanitize untrusted input. | MIT | — | [EN](categories/markdown-tools/markdown-it.md) · [中](categories/markdown-tools/markdown-it.zh.md) |
| **micromark** | Use it when you need a low-level, streaming-friendly CommonMark/GFM tokenizer in JS — the engine underneath remark — but you must build the rendering layer yourself. | MIT | — | [EN](categories/markdown-tools/micromark.md) · [中](categories/markdown-tools/micromark.zh.md) |
| **Pandoc** | Universal markup converter | GPL-2.0 | ? (0/6) | [EN](categories/markdown-tools/pandoc.md) · [中](categories/markdown-tools/pandoc.zh.md) |
| **Goldmark** | :trophy: A markdown parser written in Go. Easy to extend, standard(CommonMark) compliant, well structured. | MIT | ? (0/6) | [EN](categories/markdown-tools/goldmark.md) · [中](categories/markdown-tools/goldmark.zh.md) |
| **markdownlint** | A Node.js style checker and lint tool for Markdown/CommonMark files. | MIT | ? (0/6) | [EN](categories/markdown-tools/markdownlint.md) · [中](categories/markdown-tools/markdownlint.zh.md) |

### pdf-tools

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **PDF.js** | Use it when you need to render or read PDFs in the browser/Node (Firefox's engine) — it doesn't create or edit PDFs. | Apache-2.0 | A (6/6) | [EN](categories/pdf-tools/pdfjs.md) · [中](categories/pdf-tools/pdfjs.zh.md) |
| **pdf-lib** | Use it when you need to create or modify PDFs in JS/TS — in the browser, Node, Deno, or React Native — without native dependencies. | MIT | — | [EN](categories/pdf-tools/pdf-lib.md) · [中](categories/pdf-tools/pdf-lib.zh.md) |
| **jsPDF** | Use it when you need client-side PDF generation from HTML, text, and graphics in the browser — it's creation-only, not for editing existing PDFs. | MIT | — | [EN](categories/pdf-tools/jspdf.md) · [中](categories/pdf-tools/jspdf.zh.md) |
| **PyMuPDF** | PyMuPDF is a high performance Python library for data extraction, analysis, conversion & manipulation of PDF (and other) documents. | AGPL-3.0 | ? (0/6) | [EN](categories/pdf-tools/pymupdf.md) · [中](categories/pdf-tools/pymupdf.zh.md) |
| **pdfplumber** | Plumb a PDF for detailed information about each char, rectangle, line, et cetera — and easily extract text and tables. | MIT | ? (0/6) | [EN](categories/pdf-tools/pdfplumber.md) · [中](categories/pdf-tools/pdfplumber.zh.md) |
| **OCRmyPDF** | OCRmyPDF adds an OCR text layer to scanned PDF files, allowing them to be searched | MPL-2.0 | ? (0/6) | [EN](categories/pdf-tools/ocrmypdf.md) · [中](categories/pdf-tools/ocrmypdf.zh.md) |
| **qpdf** | qpdf: A content-preserving PDF document transformer | Apache-2.0 | ? (0/6) | [EN](categories/pdf-tools/qpdf.md) · [中](categories/pdf-tools/qpdf.zh.md) |
| **SAPP** | Use it when a PHP app must append PKCS#12 signatures without destroying existing PDF revisions — coverage is narrow and encrypted PDFs are unsupported. | LGPL-3.0-or-later | B (5/6) | [EN](categories/pdf-tools/sapp.md) · [中](categories/pdf-tools/sapp.zh.md) |

### workflow-orchestration

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Apache Airflow** | Use it when you orchestrate scheduled batch data pipelines as Python DAGs with a UI — not low-latency or event-driven flows. | Apache-2.0 | A (6/6) | [EN](categories/workflow-orchestration/airflow.md) · [中](categories/workflow-orchestration/airflow.zh.md) |
| **Gaia** | Use it when studying the "pipelines-as-compiled-plugins" design as a read-only reference — the repo is archived and abandoned, never pick it for new production work. | Apache-2.0 | D (5/6) | [EN](categories/workflow-orchestration/gaia.md) · [中](categories/workflow-orchestration/gaia.zh.md) |
| **Airflow Maintenance DAGs** | Use it when self-managed Airflow needs proven copy-in DAGs to clean metadata-DB rows and stale logs — they run destructive DELETEs tied to version-specific internals, so dry-run and back up first. | Apache-2.0 | D (4/6) | [EN](categories/workflow-orchestration/airflow-maintenance-dags.md) · [中](categories/workflow-orchestration/airflow-maintenance-dags.zh.md) |
| **n8n** | A fair-code workflow automation platform with native AI capabilities — combine visual building with custom code, self-host or use the cloud, with 400+ integrations. | NOASSERTION (fair-code) | ? (0/6) | [EN](categories/workflow-orchestration/n8n.md) · [中](categories/workflow-orchestration/n8n.zh.md) |
| **Argo Workflows** | Workflow Engine for Kubernetes | Apache-2.0 | ? (0/6) | [EN](categories/workflow-orchestration/argo-workflows.md) · [中](categories/workflow-orchestration/argo-workflows.zh.md) |
| **Prefect** | Prefect is a workflow orchestration framework for building resilient data pipelines in Python. | Apache-2.0 | ? (0/6) | [EN](categories/workflow-orchestration/prefect.md) · [中](categories/workflow-orchestration/prefect.zh.md) |
| **Dagster** | An orchestration platform for the development, production, and observation of data assets. | Apache-2.0 | ? (0/6) | [EN](categories/workflow-orchestration/dagster.md) · [中](categories/workflow-orchestration/dagster.zh.md) |
| **Temporal** | Temporal service | MIT | ? (0/6) | [EN](categories/workflow-orchestration/temporal.md) · [中](categories/workflow-orchestration/temporal.zh.md) |

### llm-inference

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Modular Platform (MAX + Mojo)** | Use it when you want a high-performance GPU/CPU inference platform (MAX) plus the Mojo systems language — accepting single-vendor lock-in and partly non-production licensing. | Apache-2.0 (mixed) | B (5/6) | [EN](categories/llm-inference/modular.md) · [中](categories/llm-inference/modular.zh.md) |
| **omlx** | Use it when you want a Mac (Apple Silicon) local LLM inference server on MLX with SSD-tiered KV caching — a young single-maintainer repo with a suspicious star count. | Apache-2.0 | B (5/6) | [EN](categories/llm-inference/omlx.md) · [中](categories/llm-inference/omlx.zh.md) |
| **TensorRT-LLM** | Use it when you need maximum LLM inference throughput on NVIDIA GPUs and are willing to accept NVIDIA-only lock-in, complex build/engine-compile workflow, and closed-source kernels. | Apache-2.0 | — | [EN](categories/llm-inference/tensorrt-llm.md) · [中](categories/llm-inference/tensorrt-llm.zh.md) |
| **vLLM** | Use it when you want the de-facto open-source LLM serving engine with PagedAttention, continuous batching, and an OpenAI-compatible API — accepting NVIDIA-centric GPU ops and a fast-moving codebase. | Apache-2.0 | — | [EN](categories/llm-inference/vllm.md) · [中](categories/llm-inference/vllm.zh.md) |
| **SGLang** | Use it when you need a fast LLM serving engine with RadixAttention prefix caching and structured generation — ideal for tool-using agents and JSON-mode APIs — accepting a younger, smaller ecosystem than vLLM. | Apache-2.0 | — | [EN](categories/llm-inference/sglang.md) · [中](categories/llm-inference/sglang.zh.md) |
| **Ray Serve** | Use it when you need a general-purpose, scalable Python model-serving framework with multi-model composition and autoscaling — but accept Ray's operational complexity and learning curve. | Apache-2.0 | — | [EN](categories/llm-inference/ray-serve.md) · [中](categories/llm-inference/ray-serve.zh.md) |
| **llama.cpp** | LLM inference in C/C++ | MIT | ? (0/6) | [EN](categories/llm-inference/llama-cpp.md) · [中](categories/llm-inference/llama-cpp.zh.md) |
| **Ollama** | Get up and running with Kimi-K2.6, GLM-5.1, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models. | MIT | ? (0/6) | [EN](categories/llm-inference/ollama.md) · [中](categories/llm-inference/ollama.zh.md) |
| **BentoML** | The easiest way to serve AI apps and models - Build Model Inference APIs, Job queues, LLM apps, Multi-model pipelines, and more! | Apache-2.0 | ? (0/6) | [EN](categories/llm-inference/bentoml.md) · [中](categories/llm-inference/bentoml.zh.md) |
| **LMDeploy** | LMDeploy is a toolkit for compressing, deploying, and serving LLMs. | Apache-2.0 | ? (0/6) | [EN](categories/llm-inference/lmdeploy.md) · [中](categories/llm-inference/lmdeploy.zh.md) |
| **Text Generation Inference (TGI)** | Large Language Model Text Generation Inference | Apache-2.0 | ? (0/6) | [EN](categories/llm-inference/text-generation-inference.md) · [中](categories/llm-inference/text-generation-inference.zh.md) |

### task-queue

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **XXL-JOB** | Use it when a Java/Spring shop needs centrally-managed, visual, sharded scheduled jobs — mind GPL-3.0 and the central-scheduler SPOF. | GPL-3.0 | B (5/6) | [EN](categories/task-queue/xxl-job.md) · [中](categories/task-queue/xxl-job.zh.md) |
| **Celery** | Use it when a Python app must offload async/background jobs at scale — at the cost of running a broker + workers. | BSD-3-Clause | B (5/6) | [EN](categories/task-queue/celery.md) · [中](categories/task-queue/celery.zh.md) |
| **Kombu** | Use it when a Python service must publish/consume messages across swappable brokers (RabbitMQ, Redis, SQS) — virtual transports emulate AMQP imperfectly, so "swap the URL" is not identical behavior. | BSD-3-Clause | B (6/6) | [EN](categories/task-queue/kombu.md) · [中](categories/task-queue/kombu.zh.md) |
| **Flower** | Use it when a production Celery cluster needs a live dashboard to inspect and control workers and export Prometheus metrics — it can revoke tasks, so never expose it unauthenticated. | BSD-3-Clause | B (4/6) | [EN](categories/task-queue/flower.md) · [中](categories/task-queue/flower.zh.md) |
### im-automation

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **ItChat** | Study it only as legacy WeChat-bot code — abandoned, and the web protocol it relies on is defunct, so it mostly doesn't work. | MIT | C (4/6) | [EN](categories/im-automation/itchat.md) · [中](categories/im-automation/itchat.zh.md) |
| **WeChatPlugin-MacOS** | Avoid for current WeChat — a macOS WeChat.app binary tweak that breaks on every WeChat update and is ~2y idle; account-ban & security risk. | MIT | D (3/6) | [EN](categories/im-automation/wechatplugin-macos.md) · [中](categories/im-automation/wechatplugin-macos.zh.md) |
| **wxpy** | Study it only as legacy WeChat-bot code — archived since 2019 and built on the now-defunct WeChat web protocol, so it mostly doesn't work. | MIT | D (5/6) | [EN](categories/im-automation/wxpy.md) · [中](categories/im-automation/wxpy.zh.md) |
| **wxappUnpacker** | Use it when you must decompile a WeChat .wxapkg bundle you own back into readable source — but this exact repo is an empty tombstone, so grab a live fork instead. | GPL-3.0-or-later | E (4/6) | [EN](categories/im-automation/wxappunpacker.md) · [中](categories/im-automation/wxappunpacker.zh.md) |
| **Douyin-Bot** | Use it only as a historical reference for ADB screen-coordinate phone automation — never deploy it, its 2018 coordinates and dead Tencent face API mean it no longer works. | MIT | D (3/6) | [EN](categories/im-automation/douyin-bot.md) · [中](categories/im-automation/douyin-bot.zh.md) |
| **WeChat Bot** | Use it when one Node CLI must bridge WeChat, Lark, Telegram, and WhatsApp to several LLMs — personal WeChat remains unofficial and account-risky. | MIT | B (5/6) | [EN](categories/im-automation/wechat-bot.md) · [中](categories/im-automation/wechat-bot.zh.md) |
| **ChatGPT-wechat-bot** | Use it only as compact 2022–2023 Wechaty and ChatGPT reference code — it is stale, tied to old defaults, and not a production base. | MIT | D (3/6) | [EN](categories/im-automation/chatgpt-wechat-bot.md) · [中](categories/im-automation/chatgpt-wechat-bot.zh.md) |
| **OpeniLink Hub** | Use it when multiple iLink WeChat bots need self-hosted management, tracing, webhooks, and Apps — it is young, unofficial, and widens the auth and registry trust boundary. | MIT | B (5/6) | [EN](categories/im-automation/openilink-hub.md) · [中](categories/im-automation/openilink-hub.zh.md) |
| **Dify Enterprise WeChat Bot** | Use it only to preserve a pinned Windows Enterprise WeChat-to-Dify desktop integration — it is stale, includes a closed helper, and leaves Workflow support unfinished. | NOASSERTION | C (3/6) | [EN](categories/im-automation/dify-enterprise-wechat-bot.md) · [中](categories/im-automation/dify-enterprise-wechat-bot.zh.md) |
### web-ui

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Driver.js** | Use it when you want a tiny, dependency-free product tour / feature-spotlight on a web page — not a full onboarding platform. | MIT | B (6/6) | [EN](categories/web-ui/product-tours/driver-js.md) · [中](categories/web-ui/product-tours/driver-js.zh.md) |
| **Shepherd.js** | Use it when you want a robust, framework-agnostic product tour library with advanced positioning and multi-step onboarding — but you accept a heavier bundle than Driver.js. | MIT | ? (0/6) | [EN](categories/web-ui/product-tours/shepherd-js.md) · [中](categories/web-ui/product-tours/shepherd-js.zh.md) |
| **Intro.js** | Use it when you want a mature, framework-agnostic product tour library with extensive documentation — but you accept AGPL-3.0 for non-commercial use or must purchase a commercial license. | AGPL-3.0 | ? (0/6) | [EN](categories/web-ui/product-tours/intro-js.md) · [中](categories/web-ui/product-tours/intro-js.zh.md) |
| **Vue.js** | Use it when you want a progressive, approachable JavaScript framework with excellent documentation, gentle learning curve, and incrementally adoptable architecture — but you accept a smaller Western job market than React and no mega-corporate backing. | MIT | ? (0/6) | [EN](categories/web-ui/frameworks/vue.md) · [中](categories/web-ui/frameworks/vue.zh.md) |
| **Svelte** | Use it when you want a compile-time frontend framework with small bundles, no virtual DOM, and readable syntax — but you accept a smaller ecosystem and job market than React or Vue. | MIT | ? (0/6) | [EN](categories/web-ui/frameworks/svelte.md) · [中](categories/web-ui/frameworks/svelte.zh.md) |
| **shadcn/ui** | A set of beautifully-designed, accessible React components that you copy into your project and own completely — but it requires React and Tailwind CSS. | MIT | ? (0/6) | [EN](categories/web-ui/component-libraries/shadcn-ui.md) · [中](categories/web-ui/component-libraries/shadcn-ui.zh.md) |
| **Angular** | Use it when you need a mature, opinionated full-stack framework with dependency injection, strong typing, and a large ecosystem for enterprise-scale web apps — but it's heavy and overkill for small projects. | MIT | ? (0/6) | [EN](categories/web-ui/frameworks/angular.md) · [中](categories/web-ui/frameworks/angular.zh.md) |
| **Ant Design** | Use it when you want a comprehensive, production-ready React UI component library with enterprise-grade design patterns, theming, and accessibility — but it's React-only and the design is distinctly "Chinese enterprise". | MIT | ? (0/6) | [EN](categories/web-ui/component-libraries/ant-design.md) · [中](categories/web-ui/component-libraries/ant-design.zh.md) |
| **Lit** | Use it when you need lightweight, standards-based web components that work across any framework — but you accept a smaller ecosystem and the need to learn Web Components. | BSD-3-Clause | ? (0/6) | [EN](categories/web-ui/frameworks/lit.md) · [中](categories/web-ui/frameworks/lit.zh.md) |
| **React** | Use it when you want the most popular UI library with a vast ecosystem, deep hiring pool, and declarative component model — but you accept the need to assemble your own routing, state management, and build pipeline. | MIT | A (6/6) | [EN](categories/web-ui/frameworks/react.md) · [中](categories/web-ui/frameworks/react.zh.md) |
| **Next.js** | Use it when you want a full-stack React framework with SSR, SSG, file-based routing, and API routes built in — but you accept Vercel's influence on the roadmap and a more opinionated architecture than plain React. | MIT | ? (0/6) | [EN](categories/web-ui/frameworks/nextjs.md) · [中](categories/web-ui/frameworks/nextjs.zh.md) |
| **SvelteKit** | web development, streamlined | MIT | ? (0/6) | [EN](categories/web-ui/frameworks/sveltekit.md) · [中](categories/web-ui/frameworks/sveltekit.zh.md) |
| **Reactour** | Tourist Guide into your React Components | MIT | ? (0/6) | [EN](categories/web-ui/product-tours/reactour.md) · [中](categories/web-ui/product-tours/reactour.zh.md) |
| **react-joyride** | Create guided tours in your apps | MIT | ? (0/6) | [EN](categories/web-ui/product-tours/react-joyride.md) · [中](categories/web-ui/product-tours/react-joyride.zh.md) |
| **Material UI (MUI)** | Material UI: Comprehensive React component library that implements Google's Material Design. Free forever. | MIT | ? (0/6) | [EN](categories/web-ui/component-libraries/material-ui.md) · [中](categories/web-ui/component-libraries/material-ui.zh.md) |
| **Chakra UI** | Chakra UI is a component system for building SaaS products with speed ⚡️ | MIT | ? (0/6) | [EN](categories/web-ui/component-libraries/chakra-ui.md) · [中](categories/web-ui/component-libraries/chakra-ui.zh.md) |
| **Radix UI Primitives** | Radix Primitives is an open-source UI component library for building high-quality, accessible design systems and web apps. Maintained by @workos. | MIT | ? (0/6) | [EN](categories/web-ui/component-libraries/radix-ui.md) · [中](categories/web-ui/component-libraries/radix-ui.zh.md) |
| **Nuxt** | the full-stack Vue framework | MIT | ? (0/6) | [EN](categories/web-ui/frameworks/nuxt.md) · [中](categories/web-ui/frameworks/nuxt.zh.md) |
| **Astro** | The web framework for content-driven websites. ⭐️ Star to support our work! | NOASSERTION | ? (0/6) | [EN](categories/web-ui/frameworks/astro.md) · [中](categories/web-ui/frameworks/astro.zh.md) |

### proxy-pool

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **proxy_pool** | Use it when a scraper needs a rotating pool of free proxy IPs behind a simple API — accepting that free proxies are unreliable and insecure. | MIT | A (4/6) | [EN](categories/proxy-pool/proxy-pool.md) · [中](categories/proxy-pool/proxy-pool.zh.md) |
| **ProxyBroker** | Use it when you need a throwaway pool of free public proxies for a low-stakes prototype via a single rotating local endpoint — but it's effectively frozen since ~2018 and widely breaks on modern Python without pinning. | Apache-2.0 | D (4/6) | [EN](categories/proxy-pool/proxybroker.md) · [中](categories/proxy-pool/proxybroker.zh.md) |
| **Scylla** | Use it when you want an always-on, self-hosted free-proxy pool with a JSON API, quality scoring, and dashboard via one Docker command — but its forward proxy can't do HTTPS, and releases stalled since 2022. | Apache-2.0 | C (3/6) | [EN](categories/proxy-pool/scylla.md) · [中](categories/proxy-pool/scylla.zh.md) |
| **haipproxy** | Use it when you genuinely need a distributed, high-availability free-proxy pool for large multi-machine crawls on Scrapy+Redis — but it's dormant since 2022, runs 2018-era Py2/3 code, and is the heaviest pool to operate. | MIT | D (3/6) | [EN](categories/proxy-pool/haipproxy.md) · [中](categories/proxy-pool/haipproxy.zh.md) |
### debugging-proxy

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **whistle** | Use it when a web/mobile dev must capture, inspect, rewrite, and mock HTTP(S)/WebSocket traffic via a rule-based web UI — a dev proxy, not a production gateway or scraping pool. | MIT | B (6/6) | [EN](categories/debugging-proxy/whistle.md) · [中](categories/debugging-proxy/whistle.zh.md) |
| **AnyProxy** | Use it when you want a scriptable Node.js MITM proxy to inspect and rewrite HTTP/HTTPS traffic in plain JS rules — but master is frozen since 2020, so prefer whistle for new work. | Apache-2.0 | C (4/6) | [EN](categories/debugging-proxy/anyproxy.md) · [中](categories/debugging-proxy/anyproxy.zh.md) |
| **mitmproxy** | An interactive TLS-capable intercepting HTTP proxy for penetration testers and software developers. | MIT | ? (0/6) | [EN](categories/debugging-proxy/mitmproxy.md) · [中](categories/debugging-proxy/mitmproxy.zh.md) |

### web-scraping

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **newspaper** | Use it to bulk-extract article text, authors, and metadata from news URLs — but the original (newspaper3k) is stale; the live path is the newspaper4k fork. | MIT | B (5/6) | [EN](categories/web-scraping/article-extraction/newspaper.md) · [中](categories/web-scraping/article-extraction/newspaper.zh.md) |
| **requests-html** | Study it for tiny requests + HTML-parsing scripts — effectively unmaintained (~2y idle), the JS-render path is fragile; prefer Playwright + parsel for new work. | MIT | D (3/6) | [EN](categories/web-scraping/crawling-tools/requests-html.md) · [中](categories/web-scraping/crawling-tools/requests-html.zh.md) |
| **Firecrawl** | The API to search, scrape, and extract clean Markdown or structured data from the web at scale — but AGPL-3.0 may limit commercial use. | AGPL-3.0 | ? (0/6) | [EN](categories/web-scraping/crawling-tools/firecrawl.md) · [中](categories/web-scraping/crawling-tools/firecrawl.zh.md) |
| **trafilatura** | Python & Command-line tool to gather text and metadata on the Web: Crawling, scraping, extraction, output as CSV, JSON, HTML, MD, TXT, XML | Apache-2.0 | ? (0/6) | [EN](categories/web-scraping/article-extraction/trafilatura.md) · [中](categories/web-scraping/article-extraction/trafilatura.zh.md) |

### auth

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Authomatic** | Use it when a framework-agnostic Python app needs thin "sign in with X" via OAuth1/OAuth2/OpenID, leaving session persistence to you — but it's low-velocity and an auth lib's slow fix cadence is a security risk. | MIT | C (5/6) | [EN](categories/auth/authomatic.md) · [中](categories/auth/authomatic.zh.md) |
| **django-rules** | Use it when Django object-level permissions are computed from logic (predicates), not stored grants, with no DB tables — but if admins must assign per-object permissions at runtime you need django-guardian instead. | MIT | B (5/6) | [EN](categories/auth/django-rules.md) · [中](categories/auth/django-rules.zh.md) |
| **Keycloak** | Open Source Identity and Access Management For Modern Applications and Services | Apache-2.0 | ? (0/6) | [EN](categories/auth/keycloak.md) · [中](categories/auth/keycloak.zh.md) |
| **Casbin** | Apache Casbin: an authorization library that supports access control models like ACL, RBAC, ABAC. | Apache-2.0 | ? (0/6) | [EN](categories/auth/casbin.md) · [中](categories/auth/casbin.zh.md) |
| **OpenFGA** | A high performance and flexible authorization/permission engine built for developers and inspired by Google Zanzibar | Apache-2.0 | ? (0/6) | [EN](categories/auth/openfga.md) · [中](categories/auth/openfga.zh.md) |

### databases

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **PikiwiDB** | Use it when a large Redis dataset has blown past RAM and memory cost dominates — RocksDB-backed, Redis-protocol, so one node holds hundreds of GB; but it trades latency for capacity, wrong if every op must be microsecond-fast. | BSD-3-Clause | B (5/6) | [EN](categories/databases/database-engines/pikiwidb.md) · [中](categories/databases/database-engines/pikiwidb.zh.md) |
| **elasticsearch-dsl-py** | Use it when you maintain legacy Python code pinned to the standalone elasticsearch-dsl package — for any new project it's archived, so install elasticsearch>=8.18 and use elasticsearch.dsl instead. | Apache-2.0 | D (4/6) | [EN](categories/databases/database-clients/elasticsearch-dsl-py.md) · [中](categories/databases/database-clients/elasticsearch-dsl-py.zh.md) |
| **elasticsearch-sql** | Use it when a SQL-fluent team needs to query Elasticsearch without learning the JSON Query DSL — but Elastic's first-party SQL/ES\|QL now overlaps it, so prefer the vendor feature when it covers you. | Apache-2.0 | [EN](categories/databases/database-clients/elasticsearch-sql.md) · [中](categories/databases/database-clients/elasticsearch-sql.zh.md) |
| **go-mysql-elasticsearch** | Use it when you want a single Go binary to tail MySQL binlog and sync one direction into Elasticsearch at modest scale — but it's unmaintained since 2023 with no releases, so treat it as fork-and-own. | MIT | D (3/6) | [EN](categories/databases/data-sync/go-mysql-elasticsearch.md) · [中](categories/databases/data-sync/go-mysql-elasticsearch.zh.md) |
| **python-mysql-replication** | Use it when you want a pure-Python primitive to stream MySQL binlog as typed events and build a custom CDC loop with full control — but checkpointing, dedup and exactly-once delivery are entirely on you. | Apache-2.0 | D (5/6) | [EN](categories/databases/data-sync/python-mysql-replication.md) · [中](categories/databases/data-sync/python-mysql-replication.zh.md) |
| **PrettyZoo** | Use it when you need a friendly desktop GUI to browse and lightly edit a ZooKeeper znode tree during dev or incident triage — but it's archived since 2023, so new JDK/macOS may break it with no upstream fix. | Apache-2.0 | D (4/6) | [EN](categories/databases/database-clients/prettyzoo.md) · [中](categories/databases/database-clients/prettyzoo.zh.md) |
| **RDR** | Use it when a Redis instance trips its maxmemory alarm and you need offline, fast per-prefix analysis of an RDB snapshot — but figures are approximate and the tool is coasting (v0.0.1, 2019). | Apache-2.0 | D (3/6) | [EN](categories/databases/database-clients/rdr.md) · [中](categories/databases/database-clients/rdr.zh.md) |
| **Supabase** | The open-source Firebase alternative built on PostgreSQL with auth, auto-generated APIs, realtime, edge functions, and vector storage — but it's deeply tied to Postgres. | Apache-2.0 | ? (0/6) | [EN](categories/databases/database-engines/supabase.md) · [中](categories/databases/database-engines/supabase.zh.md) |
| **DuckDB** | DuckDB is an analytical in-process SQL database management system | MIT | ? (0/6) | [EN](categories/databases/database-engines/duckdb.md) · [中](categories/databases/database-engines/duckdb.zh.md) |
| **ClickHouse** | ClickHouse® is a real-time analytics database management system | Apache-2.0 | ? (0/6) | [EN](categories/databases/database-engines/clickhouse.md) · [中](categories/databases/database-engines/clickhouse.zh.md) |
| **DBeaver** | Free universal database tool and SQL client | Apache-2.0 | ? (0/6) | [EN](categories/databases/database-clients/dbeaver.md) · [中](categories/databases/database-clients/dbeaver.zh.md) |
| **Debezium** | Change data capture for a variety of databases. Please log issues at https://github.com/debezium/dbz/issues. | Apache-2.0 | ? (0/6) | [EN](categories/databases/data-sync/debezium.md) · [中](categories/databases/data-sync/debezium.zh.md) |
| **Valkey** | A flexible distributed key-value database that is optimized for caching and other realtime workloads. | BSD-3-Clause | ? (0/6) | [EN](categories/databases/database-engines/valkey.md) · [中](categories/databases/database-engines/valkey.zh.md) |

### desktop-automation

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **PyAutoGUI** | Use it when you must script a desktop app with no API across Windows/macOS/Linux — but coordinate/pixel automation breaks silently on resolution, DPI, or theme changes, and dev has coasted since 2024. | BSD-3-Clause | C (4/6) | [EN](categories/desktop-automation/pyautogui.md) · [中](categories/desktop-automation/pyautogui.zh.md) |

### game-dev

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **pygame** | Use it when you want to learn or ship a small 2D Python game with a simple loop — but for 3D or performance-critical work it bottlenecks, look elsewhere. | LGPL-2.1 | D (6/6) | [EN](categories/game-dev/pygame.md) · [中](categories/game-dev/pygame.zh.md) |

### kafka-tools

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **UI for Apache Kafka (provectus/kafka-ui)** | Use it when you want a one-`docker run` web dashboard to browse Kafka brokers, topics, and consumer-group lag — but this `provectus` upstream is stalled (last release 2024-04); deploy the maintained `kafbat/kafka-ui` fork instead. | Apache-2.0 | C (4/6) | [EN](categories/kafka-tools/kafka-ui.md) · [中](categories/kafka-tools/kafka-ui.zh.md) |
| **kafka-python** | Use it when you want a pure-Python Kafka client that just `pip install`s with no librdkafka to compile — but a pure-Python client can't match `confluent-kafka`'s throughput and may trail the newest broker features. | Apache-2.0 | A (6/6) | [EN](categories/kafka-tools/kafka-python.md) · [中](categories/kafka-tools/kafka-python.zh.md) |

### networking

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Paramiko** | Use it when Python code must open SSH/SFTP connections and run remote commands programmatically — but it's pure-Python (slower than OpenSSH), threading-only, and LGPL-2.1. | LGPL-2.1 | B (6/6) | [EN](categories/networking/paramiko.md) · [中](categories/networking/paramiko.zh.md) |
| **sshtunnel** | Use it when a Python script needs a clean context-managed SSH port-forward to a service behind a bastion — but it has no auto-reconnect and is low-activity (0.4.0, 2021). | MIT | B (5/6) | [EN](categories/networking/sshtunnel.md) · [中](categories/networking/sshtunnel.zh.md) |
| **dnspython** | Use it when Python needs arbitrary record types, custom resolvers, zone transfers, DNSSEC, or DoH/DoT — but it bypasses /etc/hosts and the OS resolver, requires Python 3.10+, and is a library not a CLI. | ISC | B (5/6) | [EN](categories/networking/dnspython.md) · [中](categories/networking/dnspython.zh.md) |
| **wondershaper** | Use it when one Linux NIC needs a quick up/down bandwidth ceiling without hand-writing tc rules — but it's HTB-era (not bufferbloat-aware like cake/fq_codel) and Linux-only, coasting since 2024-07. | GPL-2.0 | D (4/6) | [EN](categories/networking/wondershaper.md) · [中](categories/networking/wondershaper.zh.md) |
| **ThriftPy** | Use it only to understand a legacy service still importing thriftpy before migrating — the repo is archived and deprecated, so all new Thrift work should go to the maintained thriftpy2. | MIT | D (5/6) | [EN](categories/networking/thriftpy.md) · [中](categories/networking/thriftpy.zh.md) |

### nginx-modules

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **lua-nginx-module (ngx_lua)** | Use it when you need real per-request programmability on NGINX (auth, routing, rate-limit) via LuaJIT cosockets — but one blocking call stalls a worker, and you're bound to OpenResty's version-coupled, founder-concentrated core. | BSD-2-Clause | D (5/6) | [EN](categories/nginx-modules/lua-nginx-module.md) · [中](categories/nginx-modules/lua-nginx-module.zh.md) |
| **lua-resty-redis** | Use it when your OpenResty edge logic must hit Redis non-blocking on the request hot path with pooling and pipelining — but it works only inside ngx_lua and has no built-in Redis Cluster slot-routing. | BSD-2-Clause | D (4/6) | [EN](categories/nginx-modules/lua-resty-redis.md) · [中](categories/nginx-modules/lua-resty-redis.zh.md) |
| **nginx-upload-module** | Use it when you want NGINX to stream large multipart uploads to disk and hand your backend just file metadata — but you're compiling an aging, single-maintainer C fork (last push 2024-07); direct-to-S3 presigned uploads often beat it now. | BSD-3-Clause | ? (2/6) | [EN](categories/nginx-modules/nginx-upload-module.md) · [中](categories/nginx-modules/nginx-upload-module.zh.md) |
| **tusd** | Use it when you need a robust, protocol-based resumable upload server that can stream to local disk or cloud storage — but it's a separate service, not an NGINX module, and may be overkill for small, reliable uploads. | MIT | B (6/6) | [EN](categories/nginx-modules/tusd.md) · [中](categories/nginx-modules/tusd.zh.md) |

### python-tooling

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Cython** | Use it when a profiled hot Python loop needs near-C speed or you must wrap a C/C++ library — but it forces a C compiler and per-platform wheel build pipeline. | Apache-2.0 | A (6/6) | [EN](categories/python-tooling/cython.md) · [中](categories/python-tooling/cython.zh.md) |
| **pyrasite** | Use it when you must inject diagnostic code into a stuck or leaking live Python process you can't restart — but injection can crash the target, treat it as incident-only. | GPL-3.0 | C (4/6) | [EN](categories/python-tooling/pyrasite.md) · [中](categories/python-tooling/pyrasite.zh.md) |
| **gophernotes** | Use it when you want interactive Go cells in a Jupyter notebook for exploration or tutorials — but it's stalled since 2023 and runs an interpreter, not standard Go. | MIT | D (3/6) | [EN](categories/python-tooling/gophernotes.md) · [中](categories/python-tooling/gophernotes.zh.md) |
| **GRequests** | Use it when you want to make existing synchronous `requests` code concurrent with minimal diff via `map()` — but gevent monkeypatches the stdlib and can collide with your stack. | BSD-2-Clause | C (4/6) | [EN](categories/python-tooling/grequests.md) · [中](categories/python-tooling/grequests.zh.md) |
| **memory-analyzer** | Use it when you need a one-shot per-type memory snapshot of a live Python 3 process via GDB — but Meta archived it (last code 2021, targets EOL 3.6/3.7), so prefer a maintained tool like memray/tracemalloc. | MIT | D (5/6) | [EN](categories/python-tooling/memory-analyzer.md) · [中](categories/python-tooling/memory-analyzer.zh.md) |
| **uv** | An extremely fast Python package and project manager written in Rust, replacing pip, poetry, and pyenv with a single tool and universal lockfile — but only ~3 years old with some edge cases still being resolved. | Apache-2.0 | ? (0/6) | [EN](categories/python-tooling/uv.md) · [中](categories/python-tooling/uv.zh.md) |

### reading-tools

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **Read Frog** | Use it when you want a feature-rich open-source immersive/bilingual translation extension with BYOK AI providers, local Ollama/custom endpoints, TTS, and YouTube subtitle translation. | GPL-3.0 | B (6/6) | [EN](categories/reading-tools/read-frog.md) · [中](categories/reading-tools/read-frog.zh.md) |
| **FluentRead** | Use it when you want a Chinese-first open immersive-translation browser extension with many engines, bilingual/full-page translation, and Ollama/custom OpenAI-compatible setup. | GPL-3.0 | C (6/6) | [EN](categories/reading-tools/fluentread.md) · [中](categories/reading-tools/fluentread.zh.md) |
| **Margin Read** | Use it when MIT licensing, explicit BYOK/local endpoint support, and a written privacy threat model matter more than feature completeness. | MIT | C (5/6) | [EN](categories/reading-tools/margin-read.md) · [中](categories/reading-tools/margin-read.zh.md) |
| **Pair Translate** | Use it when you want a lighter bilingual webpage translator with direct provider requests, LLM templates, and Chrome/Firefox/Edge distribution. | GPL-3.0 | C (5/6) | [EN](categories/reading-tools/pair-translate.md) · [中](categories/reading-tools/pair-translate.zh.md) |
| **NetNewsWire** | Use it when you read many feeds on Mac/iPhone and want a fast, ad-free native RSS client you own — but only on Apple platforms, never elsewhere. | MIT | B (5/6) | [EN](categories/reading-tools/netnewswire.md) · [中](categories/reading-tools/netnewswire.zh.md) |
| **Just Read** | Use it when you want to strip ads and clutter from an article in-browser, your way, with per-site selectors — but it's EULA-licensed source, not real OSS. | Unlicensed (EULA) | D (6/6) | [EN](categories/reading-tools/just-read.md) · [中](categories/reading-tools/just-read.zh.md) |
| **FreshRSS** | A free, self-hostable news aggregator… | AGPL-3.0 | ? (0/6) | [EN](categories/reading-tools/freshrss.md) · [中](categories/reading-tools/freshrss.zh.md) |

### speech

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **SpeechBrain** | Use it when you need to train and adapt speech models (ASR, speaker ID, separation) on one coherent PyTorch recipe codebase — but it's research-and-training-first, so production serving and cross-version API stability are your job. | Apache-2.0 | B (5/6) | [EN](categories/speech/speechbrain.md) · [中](categories/speech/speechbrain.zh.md) |

### terminal-ui

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **colorama** | Use it when a Python CLI needs ANSI colored output that also works on legacy Windows consoles — but it's only a color/style shim (no tables, TUI, or guaranteed truecolor) and largely a no-op on modern terminals. | BSD-3-Clause | B (4/6) | [EN](categories/terminal-ui/colorama.md) · [中](categories/terminal-ui/colorama.zh.md) |
| **asciimatics** | Use it when you need a cross-platform full-screen Python TUI plus an ASCII animation engine on Linux/macOS/Windows — but the widget set is spartan, the API older-style, and it's single-maintainer. | Apache-2.0 | C (5/6) | [EN](categories/terminal-ui/asciimatics.md) · [中](categories/terminal-ui/asciimatics.zh.md) |
| **Terminal Markdown Viewer (mdv)** | Use it when you want one-shot read-only Markdown rendered with color/syntax-highlighting in a plain terminal over SSH — but it's low-activity (0.x, 2024-05) and glow/mdcat are the modern defaults. | BSD-3-Clause | ? (2/6) | [EN](categories/terminal-ui/terminal-markdown-viewer.md) · [中](categories/terminal-ui/terminal-markdown-viewer.zh.md) |
| **ART** | Use it when a Python CLI needs pure-Python figlet-style ASCII text banners with no system binaries — but it's text-to-art only (not image-to-ASCII) and won't match figlet's exact fonts. | MIT | C (4/6) | [EN](categories/terminal-ui/art.md) · [中](categories/terminal-ui/art.zh.md) |
| **asciify** | Use it as a minimal, legible copy-paste reference for the image-to-ASCII algorithm — but it ships NO license (all rights reserved), is unmaintained since 2022, so never vendor it into a product. | NONE | E (4/6) | [EN](categories/terminal-ui/asciify.md) · [中](categories/terminal-ui/asciify.zh.md) |
| **Warp** | A modern, AI-powered terminal with command blocks and integrated coding agents — but the GitHub repo is issues-only and the product is proprietary closed-source. | AGPL-3.0 | ? (0/6) | [EN](categories/terminal-ui/warp.md) · [中](categories/terminal-ui/warp.zh.md) |
| **Alacritty** | A fast, GPU-accelerated OpenGL terminal emulator with sensible defaults; lacks tabs, splits, and ligatures by design — use tmux for multiplexing. | Apache-2.0 | ? (0/6) | [EN](categories/terminal-ui/alacritty.md) · [中](categories/terminal-ui/alacritty.zh.md) |

Categories follow the tree in [INDEX.md](INDEX.md).
| **Readability.js** | Use it when you need to strip a web page down to just the article (title, byline, body) using Firefox Reader View's battle-tested engine — but it parses a DOM you supply; it won't fetch URLs or render JS-heavy SPAs. | Apache-2.0 | [EN](categories/web-scraping/article-extraction/readability-js.md) · [中](categories/web-scraping/article-extraction/readability-js.zh.md) |
| **python-readability** | Use it when your Python pipeline needs fast lxml article extraction from already-fetched HTML with no browser or Node — but it's single-maintainer and slow-cadence, and trafilatura often scores better on extraction benchmarks. | Apache-2.0 | [EN](categories/web-scraping/article-extraction/python-readability.md) · [中](categories/web-scraping/article-extraction/python-readability.zh.md) |
| **dragnet** | Use it when you have labeled data and want a trainable ML extractor that also separates article from user comments — but it's near-dormant with aging pins (`scikit-learn<0.21`, `ftfy<5`) that make installing on modern stacks painful. | MIT | [EN](categories/web-scraping/article-extraction/dragnet.md) · [中](categories/web-scraping/article-extraction/dragnet.zh.md) |
| **boilerpipe** | Use it when you specifically need a JVM-native, dependency-light classic-algorithm article extractor — but the repo is effectively abandoned (last push 2018-01) with aged vendored deps and no security fixes coming. | Apache-2.0 | [EN](categories/web-scraping/article-extraction/boilerpipe.md) · [中](categories/web-scraping/article-extraction/boilerpipe.zh.md) |
| **fuck-login** | Use it when you want to read 2016-era examples of how site logins (CSRF/RSA/captcha) were scripted — but it's abandoned since 2018, unlicensed, and the scripts are broken today. | NONE | [EN](categories/web-scraping/crawling-tools/fuck-login.md) · [中](categories/web-scraping/crawling-tools/fuck-login.zh.md) |
| **gopup** | Use it when you need a quick one-line pull of Chinese public data (search indices, CPI, Shibor) into a pandas DataFrame for academic research — but it's coasting since 2023, unlicensed, and scrapers rot as sources change. | NONE | [EN](categories/web-scraping/crawling-tools/gopup.md) · [中](categories/web-scraping/crawling-tools/gopup.zh.md) |
| **PRAW** | Use it when your data source is Reddit and you want the official OAuth-compliant path with rate-limit handling built in — but Reddit's own API terms, quotas, and pricing bound what you can do, not the library. | BSD-2-Clause | [EN](categories/web-scraping/crawling-tools/praw.md) · [中](categories/web-scraping/crawling-tools/praw.zh.md) |
| **Scrapyd** | Use it when you need to deploy local Scrapy spiders to a server and drive scheduled, versioned crawls over an HTTP API — but it only runs Scrapy and ships unauthenticated, so add auth before exposing port 6800. | BSD-3-Clause | [EN](categories/web-scraping/crawling-tools/scrapyd.md) · [中](categories/web-scraping/crawling-tools/scrapyd.zh.md) |
| **SpiderKeeper** | Use it when a small team running Scrapyd wants the simplest browser dashboard to deploy and cron-schedule spiders — but it's stale since 2023 with default admin/admin auth, so don't expose it untrusted. | MIT | [EN](categories/web-scraping/crawling-tools/spiderkeeper.md) · [中](categories/web-scraping/crawling-tools/spiderkeeper.zh.md) |
## Why this exists

Most OSS READMEs are marketing: they tell you what a project does and why it's great. They do
**not** tell you when *not* to use it, how it compares to alternatives, or what it costs to
operate. An agent doing selection needs exactly that negative space. oss-atlas inverts the
README genre into a **decision-support** genre.

The index is deliberately **weak** — no database, no search, no embeddings. Just Markdown that
an agent reads and reasons over. The directory structure *is* the query API.

## Selection signals & heuristics

Choosing OSS is a bet on the future, not just a feature match. Every page carries a
**`Health & viability`** section — a dated, labeled verdict on whether the project is worth betting
on: maintenance cadence, governance & bus factor, backing org, adoption/ecosystem, and risk flags
(relicense history, open-core gating, CVEs). Read it alongside `When NOT to use`.

One prior deserves a name — the **Lindy effect**: for non-perishable things (software, formats,
tools), expected *remaining* life grows with current age. A project **actively maintained** for 12
years is a safer long-term bet than one that exploded in 6 months. Treat it as a prior, not a law,
and always as **age × still-active**: it discounts young-but-hyped repos (suspicious stars, unproven)
and does **not** rescue old **abandoned** ones (age alone ≠ alive); it can also mislead across
paradigm shifts. Pages record the project's **age** so the prior is checkable. [推断: the Lindy
framing is a heuristic, not a guarantee of any specific project's survival.]

## Structure (recursive tree, bilingual)

```
INDEX.md / INDEX.zh.md                        # root: category route (EN / 中)
categories/<cat>/INDEX.md / INDEX.zh.md       # a category node: pages + sub-categories
categories/<cat>/<subcat>/INDEX.md …          # deeper nodes — the tree self-balances as it grows
…/<slug>.md  +  …/<slug>.zh.md                # a leaf: the EN selection page + its 中文 sibling
```

`categories/` is a **recursive, self-balancing tree**: when a category gets too many projects it
splits into sub-categories (the linter WARNs; `refactor-index` does the split). English is the
agent-canonical path; the `.zh.md` sibling is the same content in Chinese.
| **Rich** | Rich is a Python library for rich text and beautiful formatting in the terminal. | MIT | ? (0/6) | [EN](categories/terminal-ui/rich.md) · [中](categories/terminal-ui/rich.zh.md) |
| **Textual** | The lean application framework for Python.  Build sophisticated user interfaces with a simple Python API. Run your apps in the terminal and a web browser. | MIT | ? (0/6) | [EN](categories/terminal-ui/textual.md) · [中](categories/terminal-ui/textual.zh.md) |

### Anatomy of a project page

Each page = **YAML frontmatter (facts, dated)** + **Markdown body (judgment)**. The two are kept
apart on purpose: facts go stale and get re-verified (`last_verified`); judgment is opinion and is
labeled (`[未验证]` / `[推断]`), never asserted as eternal truth.

**Frontmatter** (identical across the EN/中 pair — facts are language-neutral):
`name · slug · repo · category · tags · language · license · maturity` (dated) · `last_verified` · `type`
(`tool | library | app | framework | service | model | skill-pack`).

**Body sections** (the exact set depends on `type`):

| Section (EN / 中) | Required for | What it carries |
|---|---|---|
| `When to use` / `何时使用` | all types | a **User Story** — a concrete second-person scenario, not a feature list |
| `When NOT to use` / `何时不用` | all types | the decisive filter: anti-patterns, scale ceilings, lock-in, maintenance risk |
| `Comparison` / `横向对比` | all types | a table vs real substitutes (`未收录` when an alternative isn't indexed yet) |
| `Tech stack` / `技术栈` | non-`skill-pack` | languages, frameworks, datastores it's built on |
| `Dependencies` / `依赖` | non-`skill-pack` | runtime/infra you must run (db, services, hardware) |
| `Ops difficulty` / `运维难度` | non-`skill-pack` | low / medium / high + why |
| `Health & viability` / `健康度与可持续性` | all types | dated viability verdict — maintenance, governance/bus-factor, backing, **age × Lindy**, adoption, risk flags |
| `Caveats (unverified)` / `存疑（未验证）` | all types | the uncertainty ledger — one `[未验证]`/`[推断]` bullet per unverified fact |

The full contract is [tools/schema.md](tools/schema.md); the linter ([tools/lint.py](tools/lint.py))
enforces this shape (sections, bilingual parity, fullwidth Chinese punctuation, README parity).

## Freshness

Facts go stale. Every page records `last_verified`. The linter warns when an entry is older
than 90 days; the `sync-entry` skill re-verifies it against the live repo. Treat any fact as a
**point-in-time** snapshot, labeled per the truth discipline (`[未验证]` / `[推断]`).

## Contributing

The unit of inclusion is a **git repository** — any real open-source repo, across any domain. Not
added: non-repos (hosted SaaS, landing pages, articles), exact duplicates, empty repos. See
[CONTRIBUTING.md](CONTRIBUTING.md) and [tools/schema.md](tools/schema.md).

```bash
python3 tools/lint.py    # the structural gate; no unit tests (it's a content repo)
```

Lint is a **structural** gate (frontmatter keys + bilingual parity, required/forbidden sections per
`type`, H1, links, Caveats ledger, fanout) — not a **semantic** one. `lint clean` means the shape is
right, not that the prose was reviewed for accuracy or selection quality.

## License

- **Tooling** (code, e.g. `tools/lint.py`): MIT — see [LICENSE](LICENSE).
- **Content** (prose under `categories/`, routing pages, docs): CC BY 4.0 — see
  [LICENSE-CONTENT](LICENSE-CONTENT).

Profiles describe third-party projects owned by their respective authors and governed by their
own licenses; the CC BY 4.0 grant covers only the original analysis here.

### investment-finance

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **awesome-deep-trading** | List of awesome resources for machine learning-based algorithmic trading | NOASSERTION | ? (0/6) | [EN](categories/investment-finance/awesome-deep-trading.md) · [中](categories/investment-finance/awesome-deep-trading.zh.md) |
| **OpenBB** | Open Data Platform for analysts, quants and AI agents. | NOASSERTION | ? (0/6) | [EN](categories/investment-finance/openbb.md) · [中](categories/investment-finance/openbb.zh.md) |
| **FinRL** | FinRL®:  Financial Reinforcement Learning. 🔥 | NOASSERTION | ? (0/6) | [EN](categories/investment-finance/finrl.md) · [中](categories/investment-finance/finrl.zh.md) |
| **qlib** | Qlib is an AI-oriented Quant investment platform that aims to use AI tech to empower Quant Research, from exploring ideas to implementing productions. Qlib supports diverse ML modeling paradigms, including supervised learning, market dynamics modeling, and RL, and is now equipped with https://github.com/microsoft/RD-Agent to automate R&D process. | NOASSERTION | ? (0/6) | [EN](categories/investment-finance/qlib.md) · [中](categories/investment-finance/qlib.zh.md) |
| **backtrader** | Python Backtesting library for trading strategies | NOASSERTION | ? (0/6) | [EN](categories/investment-finance/backtrader.md) · [中](categories/investment-finance/backtrader.zh.md) |
| **yfinance** | Download market data from Yahoo! Finance's API | NOASSERTION | ? (0/6) | [EN](categories/investment-finance/yfinance.md) · [中](categories/investment-finance/yfinance.zh.md) |

### education-tutoring

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **DeepTutor** | DeepTutor: Lifelong Personalized Tutoring. https://deeptutor.info/. | NOASSERTION | ? (0/6) | [EN](categories/education-tutoring/deeptutor.md) · [中](categories/education-tutoring/deeptutor.zh.md) |

### agent-governance

| Project | Use when | License | Health | Page |
| --- | --- | --- | --- | --- |
| **agent-governance-toolkit** | Microsoft's public-preview governance toolkit for production AI agents: policy-gated tool calls, identity/trust, audit/compliance, MCP security gateway, SRE controls, and multi-language SDKs around agent frameworks. | MIT | B (6/6) | [EN](categories/agent-governance/agent-governance-toolkit.md) · [中](categories/agent-governance/agent-governance-toolkit.zh.md) |
| **SkillSpector** | NVIDIA's security scanner for AI agent skills: pre-install CLI/MCP scanning for prompt injection, exfiltration, dangerous scripts, MCP poisoning, dependencies, and SARIF/JSON evidence. | Apache-2.0 | B (6/6) | [EN](categories/agent-governance/skillspector.md) · [中](categories/agent-governance/skillspector.zh.md) |
