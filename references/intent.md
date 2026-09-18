# Intent entry

Use for `$yollox: <objective>`. Select and compose existing capabilities to fulfill the user's bounded engineering objective, without requiring the user to choose mode names. This is an instruction workflow, not a new execution engine or a mandatory pipeline.

## Understand the assignment

Interpret the whole request with applicable conversation decisions and explicit restrictions. Establish the observable result, target, contracts to preserve or change, authorized effects, and evidence of completion. Keep this understanding in working context; do not require a task specification, fixed template, or approval of the selected modes.

Resolve the Git root and applicable instructions. Outside a Git worktree, report the prerequisite without creating a repository. Use bounded, read-only discovery while resolving intent: canonicalize pointers and working directories, do not silently cross repository boundaries or escaping symlinks, disable Git optional locks and external diff helpers/textconv, and protect secrets. Do not execute uncertain effects to determine what the user meant.

An unambiguous request to implement or correct behavior authorizes work within the relevant execution contract; proceed without asking whether the user wants BUILD or FIX. A request for a proposal, explanation, diagnosis, or review alone does not authorize product edits. Read requests in context rather than treating an isolated verb as permission. If missing intent materially changes the outcome or permitted effects, ask the specific question and continue independent authorized work without acting on a guessed answer.

Briefly communicate the intended result and material scope when useful. Do not turn this into a mandatory plan document, mode-selection report, or confirmation gate. If the objective is already satisfied, explain the evidence and make no unnecessary changes.

## Make decisions at the right boundary

- Resolve technical choices from current evidence, existing compatible capabilities and the user's constraints. A choice being technically important does not by itself require user approval.
- Investigate technical uncertainty through proportionate inspection and permitted validation. If evidence remains insufficient for a material decision, keep dependent work conditional; do not replace uncertainty with invented requirements or guarantees.
- Ask when a missing user choice changes the intended behavior, priorities, compatibility, data consequences, scope or authorized effects and cannot be established from available evidence. Give a recommendation and the material tradeoff when supported, rather than asking the user to select an internal mode.
- Honor decisions and authorization already supplied. Approval of a proposal alone does not order implementation. A request that already includes implementation need not pause after its planning or design reasoning unless a material unresolved decision prevents progress.

When discovery or later evidence materially changes the difficulty of the remaining work, apply the skill's shared model and reasoning suitability policy. Follow [model-selection.md](model-selection.md) before recommending a change; capability selection itself neither requires a new configuration nor changes the effective one.

## Select only necessary capabilities

Select by the result and obligations, not by keyword matching. Read each selected mode reference completely once, plus [execution.md](execution.md) for CLEAN, FIX, BUILD or DEPLOY. Use the links in the skill; do not load every reference to classify a request.

| Needed result | Capability |
|---|---|
| Bounded work proposal with dependencies and completion evidence | PLAN |
| Resolved material technical decisions and coherent contracts | DESIGN |
| Evidenced defects in a specified target/version | REVIEW |
| Maintainability improvements with preserved observable behavior | CLEAN |
| Correction of an evidenced defect | FIX |
| Implemented requested behavior or capability | BUILD |
| Prepared deployment path or an applied, verified release | DEPLOY, preserving PREPARE versus EXECUTE |

These are available contracts, not compulsory stages. Understanding dependencies during BUILD is ordinary implementation reasoning; it need not produce a PLAN. A routine coding choice does not require DESIGN. Inspecting one's own patch is not a separate REVIEW, and correcting one's own in-scope defect is not a new FIX task. Use additional capabilities when their distinct obligations or deliverables are necessary to the requested outcome.

A bounded explanation or diagnosis may be completed through read-only repository reasoning without forcing it into a findings report or an implementation workflow. If no existing capability covers a required action, explain that concrete limitation rather than inventing a mode or stretching another contract. An explicitly unsupported command remains unsupported.

Examples of consequential distinctions:

- “Fix the failing build” calls for causal correction, not feature implementation because the word “build” appears.
- “Propose scheduled exports; do not implement yet” may combine PLAN and DESIGN into one proposal, with no product edits.
- “Review these changes” ends with review conclusions. “Review these changes and correct the defects” also authorizes scoped corrections, subject to FIX evidence and current applicability.
- “Configure deployment” requests PREPARE. “Implement this and publish it to staging” includes execution, subject to resolved candidate, destination, effects and release gates.

INIT remains an explicitly requested lifecycle operation under its own contract. Missing or stale Project Context does not select INIT or authorize maintenance.

## Compose without broadening authorization

Organize necessary work by actual dependencies. A single authorized outcome may require multiple capabilities even when the user did not enumerate them. Each retains its scope, effect policy, evidence requirements and completion criteria. Selection is not permission, and permissions do not become the union of everything the selected modes could do.

For a review-and-correction request, complete the requested review coverage under REVIEW's boundary, then correct applicable evidenced defects under FIX. Preserve the distinction between the reviewed version and the corrected candidate. Do not edit during review, replace complete coverage with the first finding, or repeatedly restart a full review after each fix. Relevant regression checks and final patch inspection serve correction; additional review is needed only when the request or changed evidence warrants it.

For implementation-and-deployment, complete the authorized implementation and establish the candidate before publication. Follow DEPLOY's native pipeline, validation and operational checks; do not bypass a gate or silently substitute a candidate. A source change does not authorize applying a migration, provisioning resources, publishing to an unresolved destination, or performing a Git mutation. Honor existing concrete authorization without redundant confirmation; finish authorized independent preparation before asking for missing permission.

Retain any explicit read-only, file, version, environment or effect restriction throughout the assignment. If restrictions prevent a coherent result, explain the smallest necessary change and resolve it before dependent action. Do not route around a restriction through a more permissive mode. Requested proposal persistence remains the skill's narrow document exception.

Adapt the approach when new evidence invalidates a premise, but do not silently change the intended result. Preserve unrelated and concurrent work, reread affected evidence, and follow the selected mode's retry and recovery rules. Incidental defects or improvement opportunities do not expand the assignment. Stop blind retries; continue independent authorized work when a dependent portion is blocked.

## Reuse evidence and Project Context

Use Project Context only when it changes navigation from the user's functional objective to relevant modules, contracts, conventions or validation. Before consuming it, read [project-context.md](project-context.md) and establish full existing-context compatibility with safe data-only parsing. Apply the selected mode's freshness and evidence rules; for a read-only explanation or diagnosis, use the PLAN and DESIGN boundaries in the skill and verify material claims against the applicable repository version. Missing, incompatible or safely uninterpretable context falls back to bounded discovery without installation, repair or generation.

Reuse inspected evidence and the compatibility check across selected capabilities while their inputs remain applicable. Do not repeat discovery because a different capability is now needed. Reassess relevant facts when inputs change, including concurrent edits; index or historical review evidence cannot automatically establish current worktree behavior. Verify material claims in the repository and retain their environment and version scope. Possible staleness or indeterminate freshness is not permission to treat the index as truth or rebuild it.

Use `validation.yaml` only to discover candidate checks and anticipate their costs and effects. Verify selected declarations and applicability under the active capability's policy. It is neither an execution queue nor authorization; do not rerun an unchanged applicable check merely for another mode, or reuse a result invalidated by relevant changes.

Never persist assignment state, permissions, plans, future architecture or findings in `.yollox/`. Reuse proposals only when identified by the user, established by the conversation or genuinely canonical, under the skill's existing rules. No hidden cross-session memory, task IDs, approval registry, scheduler, agents, background execution or automatic next-task generation is required.

## Complete the whole objective

Evaluate completion against the user's requested result and every selected capability's obligations. Completing one part is insufficient when another required part remains. Preserve the distinction between implementation completeness, validation evidence and operational availability.

Deliver one coherent response proportionate to the assignment: what was achieved, what evidence supports it, and what materially remains unverified, conditional or blocked. Include required mode-specific information without duplicate reports. For review-and-correction, distinguish findings from corrections and their verification. No findings does not establish every feature acceptance criterion, and an implemented feature is not necessarily deployed.

A no-change result is valid when supported by evidence. An incomplete review, unresolved cause or blocked deployment must remain explicitly incomplete. End when the requested result is fulfilled or no further authorized progress is possible; do not create work to traverse remaining modes or claim completion merely because a selected capability finished.
