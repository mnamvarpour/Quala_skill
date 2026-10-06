# Quala

Quala is a Codex skill for qualitative analysis of interview transcripts.

It uses a two-pass workflow. First, separate agents examine individual transcripts and identify research-relevant ideas with exact supporting quotes. The main agent then builds an emergent codebook. In the second pass, separate agents apply only that active codebook to each transcript.

The skill verifies every quote against its source transcript. It can produce a Markdown codebook, a spreadsheet showing code presence by transcript, JSON transcript-level coding records, and an analysis manifest.

## Skill files

The complete skill is in the [`skill`](skill) folder.

- [`SKILL.md`](skill/SKILL.md) contains the workflow and operating rules
- [`verify_quotes.py`](skill/scripts/verify_quotes.py) checks exact quote matches
- [`output-schema.md`](skill/references/output-schema.md) defines stable output fields
- [`openai.yaml`](skill/agents/openai.yaml) contains the Codex interface metadata

## Current scope

The first version focuses on interview transcripts. The workflow keeps input discovery separate from analysis so future versions can support other qualitative data types.
