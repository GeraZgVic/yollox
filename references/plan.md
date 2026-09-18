# PLAN workflow

Use for `$yollox plan: <objective>`. Apply the PLAN and DESIGN boundaries in the skill. Do not load the execution contract or another mode merely to produce a plan.

## Responsibility

Turn the requested intention into the smallest coherent set of bounded, verifiable work. Establish the result, scope, dependencies, uncertainties and evidence of completion so the user can evaluate the work before execution.

PLAN is not a mandatory preamble to BUILD and is not limited to new features. It can organize a correction, cleanup, review, migration or deployment preparation. Technical feasibility matters, but PLAN need not resolve every implementation decision or produce a detailed technical design.

## Understand the intention

Start from the user's objective, observed problem, existing design and explicit constraints. Establish what observable result would satisfy the request and what must remain unchanged. Distinguish user decisions from recommendations and assumptions; do not invent business priorities or expand into product research by routine.

Ask only when a material product, compatibility, scope, data or technical decision changes the proposed work and cannot be established from available evidence. Continue useful independent analysis while awaiting an answer. Do not fill the gap with a guessed requirement or claim dependent work is ready.

## Bounded repository discovery

Inspect enough current repository evidence to identify existing capabilities, affected areas, real constraints, dependencies that change the work order, and practical validation options. Prefer exact paths, symbols, relevant ranges and nearest contracts. Do not complete the entire implementation investigation in advance or inventory unrelated code.

Use Project Context only when it changes navigation, scoping or validation selection. Before consuming `.yollox/`, read [project-context.md](project-context.md) and establish its full existing-context compatibility once with safe data-only YAML interpretation. Structural checking does not require auditing every claim. If context is absent, incompatible or cannot be safely interpreted, proceed with bounded repository discovery; do not install tooling or repair context.

Use `project.yaml` for module/tool/document pointers, `architecture.md` for boundaries, `conventions.md` for relevant patterns, and `validation.yaml` for candidate checks and their effects. `state.yaml`, evidence sources and topology watches help assess the consulted knowledge against the current target, including relevant local changes. Relevant differences mean possibly stale; unavailable baselines or non-reproducible inputs can leave freshness indeterminate. No detected difference guarantees truth, and a clean tree does not reconstruct dirty generation inputs. Verify claims material to the plan against current evidence instead of treating the index as authority.

Keep environment-specific facts scoped. A Git baseline does not establish live service state. Existing architecture describes what is present, not a veto on a requested change; identify necessary transitions rather than silently assuming the proposed state already exists. Never persist a future design as current Project Context.

## Construct the work proposal

Adapt the level of detail to the task. Make the following clear without requiring a fixed template:

- **Outcome:** the observable behavior or result to achieve.
- **Scope:** included work, material exclusions, and constraints to preserve.
- **Established decisions:** relevant user choices and repository evidence, separated from proposed choices.
- **Work units:** coherent results, their affected areas, and real dependency order.
- **Completion evidence:** how to recognize and verify the result of each material unit and the overall objective.
- **Uncertainty:** unresolved material decisions, risks, prerequisites and what would resolve them.

Describe units as results, not merely commands or file edits. For example, a consumer accepting both formats during a transition is a verifiable result; changing three files is not a success condition. Break work down only enough to expose scope, dependencies and verification, not into speculative microtasks.

Cite concrete files when their roles are established. Otherwise identify the module or contract and mark exact locations as unresolved; do not invent filenames or precise file counts. Do not require time estimates, priority labels, Must/Should/Nice categories, or a future backlog. Include them only when the request and evidence make them useful.

If an architectural choice controls later work, resolve only what is needed to make the plan sound or identify that decision explicitly. A bounded investigation may be the first unit, with its question and completion evidence specified. Its dependent work remains conditional; listing an investigation does not make the entire implementation ready. Do not automatically invoke DESIGN.

## Validation and readiness

Use existing validation declarations to propose checks when useful; distinguish planned checks from checks actually run. A catalog entry does not prove a command will validate new behavior or permit its effects. Identify needed coverage when existing checks are insufficient. Do not execute suites merely to validate the plan, promise benchmark results, or claim a command passed without execution.

A plan is sufficiently resolved when an executor can understand the objective, boundaries, dependencies and completion evidence without redefining the intended result. Routine implementation choices may remain open. Material unresolved choices must leave dependent work explicitly conditional rather than apparently ready.

It is valid to conclude that the capability already exists, a smaller configuration change suffices, no new implementation is justified, or a concrete user decision is missing. Do not invent work to populate a plan.

## Output and handoff

Deliver the proposal in the conversation by default. State whether the work is ready to execute within its defined scope or which portions remain conditional, and why. Being ready is not execution authorization. Do not create a document unless requested under the skill's narrow persistence exception; do not label an unaccepted recommendation as an accepted decision.

The proposal may be an input to DESIGN or an execution mode when explicitly applicable, not a mandatory next step. A technically settled request may need only PLAN; a small clear implementation may need neither PLAN nor DESIGN. End with the requested result and material open decisions, without automatic mode transitions, task state, or prescribed next-mode ceremonies.
