# Mr Code CLI

A local terminal coding agent using the existing Mr Aegis brain. This implementation is isolated to this folder; no existing files outside `cli/` are changed.

## Install and build

```bash
cd cli
npm install
npm run build
npm link
mr-code
```

Requires Node.js 20+ and the existing Mr Aegis inference server running at `http://127.0.0.1:8000`. Override with `AEGIS_BASE_URL`.

Modes: Ask, Plan, Build, Debug, Agent. Use `/mode build` inside the terminal to switch modes and `/exit` to quit. Tool calls require approval. Tools operate only inside the current working directory; shell commands run with the current user's OS permissions and are not sandboxed.

The CLI calls only the existing Mr Aegis `/v1/chat/completions` endpoint using its legacy `functions` format. It does not include KnightCode's multi-provider/API adapter package or connect to external AI providers.

## Design research

The CLI/agent/TUI separation is informed by the public KnightCode project: https://github.com/KnightCodeAI/knightcode. Its source is MIT licensed and includes third-party notices. This folder is a fresh Mr Code implementation, not a wholesale copy of KnightCode source.
