# Hermes Memory

Obsidian vault rules: (1) Don't regex-thrash — revert with git, redo correctly.
Root: /home/dzack/notes, paths need `Obsidian/` prefix.
(2) Don't discard data without investigating — ask first.
(3) Links are provenance: create missing targets, don't delete links.
(4) No blind aliasing — review semantic overlap.
(5) Categorize before acting.
(6) `[[x]]` etc. inside LaTeX math is inert — Obsidian ignores wikilinks in math blocks.
Never try to escape or fix math-variable wikilinks.
§
Before creating new scripts/tooling, check what exists: vault root
(/home/dzack/notes/Obsidian/), .hermes/scripts/, and ~/ai/opencode/skills/.
The vault has Python scripts at root for atomization/OCR pipelines; .hermes/scripts/
has graph analysis, link repair, and classification tools; ~/ai/opencode/skills/ has
git-guidelines (PR review w/ extract_unresolved_issues) and jules (Jules AI delegation).
Check these first before writing anything new from scratch.
§
When scanning PR review feedback, thread resolution requires a separate GraphQL
mutation:
`mutation { resolveReviewThread(input: {threadId: "PRRT_xxx"}) { thread { isResolved } } }`.
Comment replies use the REST API:
`gh api repos/OWNER/REPO/pulls/PR_NUM/comments/COMMENT_ID/replies -f body='...' --method POST`.
These are two different operations — replying to a comment does NOT resolve the thread.
§
Nvidia NIM (integrate.api.nvidia.com, key: NVIDIA_NIM_API_KEY) for vision:
meta/llama-3.2-90b-vision-instruct reliable for math diagrams (read `content`, not
`reasoning`). atomize_images.py has --transcribe flag. Hermes vision_analyze uses
nemotron-30b via OpenRouter (~60% reliable). Critical: inspect ONE raw response before
batch, read `content` not `reasoning`, and verify field structure before coding
extraction.
§
Transcription pipeline complete: 311/311 diagram crops transcribed via
atomize_images.py --transcribe using Nvidia NIM llama-3.2-90b-vision-instruct.
All transcription.md files have clean content (no reasoning field contamination).
Process ~1-2 crops/min.
§
Debugging browser PTY: 3-stream model (PTY→WS→xterm.js, RPC polling, resize).
fontFamily must include Nerd Font (jetbrainsmono etc); serve via @font-face.
page.evaluate callbacks break with tsx (__name) — use string eval. opencode
transcripts: `export <id>` + Python parser, NOT jq/grep; `ocm transcript` needs
server on :4096.
§
garza-academic-hub: .academic-card-grid/.gallery-grid need display:grid CSS.
Pandoc filter (components.lua) emits these classes w/o Tailwind. Visual regression
routes from .generated/site-manifest.json type='page'. `just test` = vitest +
playwright.
