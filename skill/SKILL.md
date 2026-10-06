---
name: quala
description: Run evidence-focused qualitative analysis on interview transcripts using a two-pass delegated workflow, an emergent codebook, exact quote verification, and Markdown, JSON, and spreadsheet outputs.
metadata:
  short-description: Analyze interview transcripts with traceable qualitative codes
---

# Quala

Use Quala when a user provides interview transcripts and a research objective, question, aim, or related study goal. Treat this as the first input adapter in an extensible qualitative analysis system. Keep transcript discovery and normalization separate from analysis so future adapters can support other qualitative data types.

## Mandatory planning phase

Start every Quala run in `/plan` mode. Planning is a hard gate. During this phase, do not edit files, transform data, launch analysis sub-agents, or produce coding results.

In the plan, inspect all available input data, determine the unit of analysis, assign stable data point IDs, identify the research objective and question, and describe the planned outputs. For the current interview adapter, the default unit is one complete interview transcript. If a file contains multiple interviews or a transcript is split across files, resolve that structure before processing.

The plan must also identify the available sub-agent concurrency limit and state how many data points will run at once and how the remaining data points will be queued. The main agent must not process a data point itself. The user must be shown the plan and the agent must receive approval before leaving planning mode and beginning analysis.

## Required inputs

Identify each individual data point before analysis. For the current interview adapter, one data point is one transcript. Preserve a stable data point ID and the original file path. Ask only for missing information that would change the analysis, such as which field contains the transcript or the study question.

Record the research objective and research question exactly as supplied, then use them to focus analysis. Do not invent a codebook before the first pass.

## Delegation and queueing

Every data point must be processed by exactly one sub-agent in each analysis pass. This protects the main agent's context window and reduces confirmation bias from a single central reading. Delegate as many sub-agents as the runtime safely allows, and queue the rest. Never silently drop a transcript because the concurrency limit was reached. Continue dispatching queued items as earlier agents finish. Keep the transcript ID in every prompt and result.

After first-pass synthesis, stop or terminate the first-pass agents before starting the second pass. Run one second-pass sub-agent per transcript with the active codebook. Use the same concurrency limit and queueing behavior.

## First pass, open coding

Tell each sub-agent to analyze only its assigned transcript against the study objective and question. It must identify meaningful ideas, tensions, patterns, exceptions, and details that help answer the study question. It must not be given a proposed codebook and must not force data into predetermined categories.

For every proposed idea, require a concise analytic label, a short explanation grounded in the transcript, and one or more rich supporting quotes. A quote should stand on its own when possible. Include the interviewer question and enough surrounding turns when the participant response would otherwise lose its meaning, reasoning, or relevant detail. Prefer complete thoughts over short fragments.

Every quote must be an exact, contiguous substring of the assigned transcript. Do not paraphrase, normalize, correct, truncate with ellipses, or change spelling, punctuation, capitalization, spacing, or wording. Before accepting a result, run `scripts/quote_is_in_source.py` for every quote. The script receives a source string and a quote string and must return `true` or `false`. This check is a required pass. You may also run `scripts/verify_quotes.py` against a JSON result to collect offsets and a batch report. Reject or repair any quote that fails exact matching. Store the verified quote and its character offsets when available.

## Codebook synthesis

The main agent reviews all first-pass ideas and verified quotes. For each idea, classify its status as `novel`, `known`, `descriptive`, or `uncertain`. `Novel` means it adds a useful insight for this study. `Known` means it is already represented or too generic to add analytic value. Do not call an idea novel only because it appears in one transcript.

Create an active codebook with a stable code ID, code name, definition, mandatory inclusion criteria, mandatory exclusion criteria, status, and supporting examples. The Markdown codebook must show both criteria for every code. Merge ideas only when their meaning, use case, and evidence type are the same and one clearer definition results. Keep separate codes when merging would hide a meaningful difference. Keep the source transcript ID and exact quote for every example.

The codebook is an analytic artifact, not a count of mentions. Preserve minority, contradictory, and negative cases when they are relevant to the research question. Mark decisions and unresolved uncertainty in the synthesis notes.

## Second pass, code application

Give each second-pass sub-agent exactly one transcript and the active codebook. Tell it to apply only existing active codes. It must not create, rename, split, or merge codes. It may report that a code has no instance in the transcript.

For each applied code, return the code ID, a brief evidence note, and rich exact quotes. Use the same quote rules as the first pass. Include the interviewer question and surrounding turns when needed for meaning. Verify every quote against the original transcript with `scripts/verify_quotes.py` before synthesis.

The main agent combines the second-pass results without changing code definitions. Preserve multiple examples when they show different forms or important variation. Distinguish absence of evidence from evidence of absence, and represent a code with no instance explicitly.

## Deliverables

Unless the user requests another format, create an output directory containing

- `codebook.md`, with the study context, method notes, code definitions, status, and verified examples
- `code_presence.xlsx`, with one row per transcript, one column per active code, and binary presence values plus transcript metadata
- `transcript_coding.json`, with one record per transcript and its applied codes, evidence notes, verified quotes, offsets, and no-instance codes
- `analysis_manifest.json`, with input files, stable IDs, research question, codebook version, verification results, and warnings

Use stable IDs so later runs can update the codebook and compare versions. Do not overwrite prior outputs without the user's request. If a spreadsheet library or spreadsheet skill is available, use it for the workbook. Otherwise create a valid workbook with the available local tooling and report any limitation.

## Safe dependency fallback

Before running a script, check whether its required libraries are available. If a required library is missing, create an isolated virtual environment inside a clearly named temporary or project-local directory, install only the required packages, and run the script through that environment. Do not modify the user's global Python installation. Keep input paths explicit, avoid destructive commands, and preserve the original data. Record the environment path and packages in the manifest, and tell the user in the final report that a virtual environment was used.

## Quality checks

Before returning results, confirm that every input transcript has a result, every code has a definition, every quote is an exact contiguous substring of its source, every binary value is `0` or `1`, and every JSON record names its source transcript. Report queued work, failed agents, missing transcripts, ambiguous parsing, and quote verification failures. Never conceal a failed or incomplete analysis behind a polished summary.

For detailed output fields and versioning guidance, read [references/output-schema.md](references/output-schema.md). For the required boolean quote check, use [scripts/quote_is_in_source.py](scripts/quote_is_in_source.py). For batch quote verification, use [scripts/verify_quotes.py](scripts/verify_quotes.py).
