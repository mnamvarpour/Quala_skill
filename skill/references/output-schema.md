# Quala output schema

Use these fields as a stable baseline. Add fields only when they improve traceability or support a new input adapter.

## Codebook

Each code has `code_id`, `name`, `definition`, `inclusion`, `exclusion`, `status`, `examples`, and `version`. Each example has `data_point_id`, `quote`, `start`, and `end`.

Use IDs such as `C001` and do not recycle an ID for a different meaning. If a code changes substantially, create a new version and document the change in the manifest.

## Transcript coding JSON

Each record has `data_point_id`, `source_path`, `codes`, and `no_instance_codes`. Each applied code has `code_id`, `evidence_note`, and `quotes`. Each quote has `text`, `start`, `end`, and `verification`.

## Presence workbook

Include a metadata sheet with the data point ID and source path. Include a presence sheet with one row per data point, one column per active code, and integer values of `0` or `1`. A `1` means at least one verified instance was coded. Do not use blank cells for no instance.

## Manifest

Record the research objective, research question, input inventory, adapter name, codebook version, agent status, quote verification counts, warnings, and output paths. This makes later iteration auditable.
