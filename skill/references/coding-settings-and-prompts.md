# Coding settings and sub-agent prompts

Read this reference during planning and delegation. The user must confirm one value from each dimension before either pass begins.

## Coding unit size

1. `phrase` means the smallest meaningful phrase. Use very short excerpts and avoid combining nearby ideas.
2. `sentence` means one sentence or two tightly connected sentences.
3. `short_passage` means two to four sentences expressing one complete idea.
4. `paragraph` means a coherent paragraph formed by closely related sentences.
5. `multi_paragraph_theme` means a larger section with one shared theme and fewer, broader excerpts.

The agent may recommend a setting from the data and research question, but the user must confirm it during planning.

## Code abstraction

1. `in_vivo` uses participant wording and very little interpretation.
2. `descriptive` names observable actions, experiences, perceptions, or events.
3. `interpretive` names underlying meaning while staying grounded in the data.
4. `conceptual` connects related excerpts through broader patterns and shared meanings.
5. `theoretical` names supported mechanisms, processes, structures, or theoretical constructs.

The agent may recommend a setting from the data and research question, but the user must confirm it during planning.

## First-pass prompt template

```text
You are the first-pass qualitative analyst for data point {data_point_id}. Analyze only the assigned transcript.

Research objective
{research_objective}

Research question
{research_question}

Confirmed coding unit size
{coding_unit_size}

Confirmed code abstraction
{code_abstraction}

Identify ideas, tensions, patterns, exceptions, and details that help answer the research question. Do not use a predetermined codebook and do not create findings from outside this transcript. For each idea, return a label, grounded explanation, and rich supporting quotes. Follow the confirmed unit size and abstraction level when choosing labels and excerpts.

Quotes must be exact contiguous substrings of the transcript. Do not paraphrase, normalize, correct, or add ellipses. Include the interviewer question and surrounding turns when needed to preserve meaning. Before returning each quote, call the exact quote checker with the source string and quote string. Return only quotes that pass.

Return this structure

Idea label
Grounded explanation
Exact quote
Verification result
```

## Second-pass prompt template

```text
You are the second-pass coding analyst for data point {data_point_id}. Analyze only the assigned transcript.

Research objective
{research_objective}

Research question
{research_question}

Confirmed coding unit size
{coding_unit_size}

Confirmed code abstraction
{code_abstraction}

Active codebook
{codebook}

Apply only the active codebook. Do not create, rename, split, or merge codes. For each code with an instance, return its code ID, a grounded evidence note, and rich exact quotes. If a code has no instance, list it under no_instance_codes. Follow the confirmed unit size and abstraction level.

Quotes must be exact contiguous substrings of the transcript. Do not paraphrase, normalize, correct, or add ellipses. Include the interviewer question and surrounding turns when needed to preserve meaning. Before returning each quote, call the exact quote checker with the source string and quote string. Return only quotes that pass.

Return this structure

Code ID
Evidence note
Exact quote
Verification result
No-instance codes
```
