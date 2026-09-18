# FIX workflow

Use for `$yollox fix: <objective>` with [execution.md](execution.md).

## Responsibility and evidence

Correct an evidenced defect by addressing its cause while preserving unrelated behavior and contracts. Accept symptoms, errors, stack traces, failing tests, reproduction steps, observed input/output, or a prior REVIEW finding as starting evidence.

Establish expected versus observed behavior. Start at an exact symbol or failure location when supplied; otherwise locate the smallest relevant execution path. A prior finding or historical patch must be checked against the current version before editing. Project Context may locate the responsible boundary and its tests, but cannot prove causality.

Reproduce before editing when an existing safe, proportionate test or command can do so. Unavailable credentials, data, services or reproduction tooling need not block a correction established by concrete source and contract evidence; disclose the limitation. Do not execute uncertain effects merely to reproduce a failure.

## Causal correction

Before patching, establish an inspected causal explanation:

`cause -> invalid state or behavior -> observed failure`

Trace only the callers, inputs, boundaries and configuration needed to support or refute it. No mandatory root-cause report or fixed questioning ritual is required.

Prefer correcting the boundary that creates or violates the invalid state over hiding a downstream symptom. Defaults, optional chaining, catches, retries or broader accepted input are not fixes merely because an exception disappears. Defensive handling is appropriate when the actual contract makes the value or error optional or expected.

- Change only the defect and dependencies needed for a complete correction. Preserve APIs, error semantics, data shape, transactions, side-effect order, compatibility and security boundaries except where the stated correction requires a change.
- Search for analogous occurrences only when evidence indicates a shared cause or another occurrence would leave the fix incomplete. Do not perform a repository-wide pattern hunt by routine.
- No opportunistic cleanup, feature addition, performance work or unrelated dependency upgrade. A dependency correction is appropriate when it addresses the demonstrated cause.
- If evidence disproves the hypothesis, reconsider and safely revise your own attempt rather than layering patches until checks pass. Follow the shared preservation rules; no destructive Git restoration.

If the defect is absent in the current version, a no-change result is valid. If evidence cannot distinguish a defect from legitimate behavior, request the specific missing information when necessary and do not invent a patch.

## Validation and completion

Add or update focused regression coverage when it materially prevents recurrence and fits the permitted file scope; otherwise use existing coverage. Do not change assertions to hide the reported failure. Validate the original scenario and affected contracts, not merely compilation. Distinguish inability to reproduce, inability to execute a check, and a failed correction.

Complete when the causal explanation justifies the coherent patch, unrelated behavior remains intact, and the original failure and affected contracts have the stated validation evidence. If verification is blocked, state what was corrected and what remains unverified without claiming the scenario passed. If the cause is unresolved or required correction is missing, report the work as incomplete.

Report the root cause, substantive fix, changed files, validation actually performed and any material remaining limitation. Do not automatically clean, review, deploy or pursue independent findings.
