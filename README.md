# Quala

Quala is a Codex skill for qualitative analysis of interview transcripts.

It begins in a mandatory `/plan` phase. The agent inspects all data, identifies the unit of analysis, checks the sub-agent concurrency limit, and presents a processing plan before any edits or analysis begin. After approval, every data point is processed by its own sub-agent in both analysis passes.

First, separate agents examine individual transcripts and identify research-relevant ideas with exact supporting quotes. The main agent then builds an emergent codebook. Each code includes a definition, inclusion criteria, exclusion criteria, and examples. In the second pass, separate agents apply only that active codebook to each transcript.

The skill verifies every quote against its source transcript. It can produce a Markdown codebook, a spreadsheet showing code presence by transcript, JSON transcript-level coding records, and an analysis manifest.

## Skill files

The complete skill is in the [`skill`](skill) folder.

- [`SKILL.md`](skill/SKILL.md) contains the workflow and operating rules
- [`verify_quotes.py`](skill/scripts/verify_quotes.py) checks exact quote matches
- [`quote_is_in_source.py`](skill/scripts/quote_is_in_source.py) returns a required boolean exact-match result
- [`output-schema.md`](skill/references/output-schema.md) defines stable output fields
- [`openai.yaml`](skill/agents/openai.yaml) contains the Codex interface metadata

## Current scope

The first version focuses on interview transcripts. The workflow keeps input discovery separate from analysis so future versions can support other qualitative data types.

If required libraries are missing, Quala uses an isolated virtual environment rather than changing the global Python installation. The final report states when this fallback was used.
