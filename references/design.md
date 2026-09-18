# DESIGN workflow

Use for `$yollox design: <objective>`. Apply the PLAN and DESIGN boundaries in the skill. Do not load the execution contract or another mode merely to produce a design.

## Responsibility

Resolve material technical decisions and define a coherent solution, its contracts and how it can be verified, without implementing it. The result must be concrete enough for implementation to proceed without reopening the central design decisions; routine coding choices need not be fixed in advance.

DESIGN does not require a PLAN document or a prior planning phase. It can address interfaces, data, state transitions, error behavior, responsibility boundaries, interaction, persistence, compatibility, deployment or recovery according to the actual objective. Do not impose a DB/API/UI template, frontend architecture or mandatory component tree on unrelated work.

## Establish the problem and evidence

Resolve the objective, constraints, applicable acceptance criteria, target and decisions already made. If the problem is materially underdefined, ask for what is needed to make the affected decision; do not invent an architecture to substitute for missing product intent. Continue independent analysis without making dependent assumptions look settled.

Inspect the relevant current implementation, contracts and consumers. Prefer nearby evidence and targeted searches over repository-wide scans. Depth follows the decisions at issue, not an obligation to redesign the surrounding system. Use an identified applicable plan or canonical documentation without treating arbitrary prose as authority.

Consult Project Context only when it helps locate constraints, conventions, boundaries or validation evidence. Before consuming `.yollox/`, read [project-context.md](project-context.md) and establish its full existing-context compatibility once using safe data-only YAML interpretation. Do not audit the entire index, install tooling to parse it, or require context to exist. Fall back to bounded repository discovery if it is absent, incompatible or cannot be safely interpreted; never repair it.

Use `project.yaml` and architecture/convention evidence pointers for navigation, `validation.yaml` for candidate checks, and `state.yaml` with evidence sources and topology watches to assess consulted knowledge against the current target, including relevant local changes. Differences mean possibly stale, not automatic regeneration. Missing baselines or non-reproducible inputs leave uncertainty where provenance cannot isolate it; a clean tree cannot reconstruct dirty generation inputs. No detected change certifies truth. Verify material claims in current applicable evidence and preserve their demonstrated environment/scope.

Separate three things throughout the proposal:

- **Observed evidence:** what the repository currently implements or guarantees.
- **Proposed decisions:** what should change to achieve the requested result.
- **Assumptions or unknowns:** premises not yet established and how they affect the recommendation.

The repository establishes current behavior; the request and applicable accepted decisions establish the intended change. An index of existing architecture cannot veto a legitimate redesign or prove that it is safe. Explain the transition and affected contracts instead. Never write proposed architecture into `.yollox/` as if already implemented, or infer live operational state from Git freshness.

## Resolve the material decisions

Identify choices that change behavior, compatibility, security, data integrity, operational risk, or meaningful implementation scope. Compare alternatives when there is a real tradeoff, including reuse or a smaller change where viable. Recommend a solution with its rationale and material costs; do not invent a quota of alternatives or treat personal architectural preferences as requirements.

Specify only the dimensions needed for this objective, such as:

- interfaces, data shapes, ownership and invariants;
- flows, states, failure behavior and relevant side-effect ordering;
- trust boundaries, authorization and sensitive-data handling;
- interaction states, accessibility or presentation when the requested design includes them;
- compatibility, migration, publication or recovery when the change affects existing consumers or operations.

Check consistency across the actual affected boundaries. A proposed client/API contract must agree on behavior; authorization must be enforceable at the identified boundary; a data transition must account for consumers that coexist during rollout. This is joint reasoning, not a requirement for parallel workers or a universal security checklist.

Use examples, diagrams, interface sketches or pseudocode when they clarify a decision, labeling future elements as proposed. These are explanatory proposal content, not authorization to write product code, schemas, prototypes, migrations or external design assets. Creating an executable prototype or running an effectful experiment requires that work to be included in the user's authorization; do not perform it silently under DESIGN.

Do not prescribe every helper, filename or implementation line unless that detail is material. Conversely, do not leave a core contract undecided merely to shorten the proposal.

## Verification and unresolved hypotheses

Connect the solution to acceptance criteria and a practical validation strategy. Existing checks are candidates, not proof of future correctness. Distinguish consistency demonstrated by inspection from properties requiring execution or operational evidence. Do not claim unmeasured performance, successful migration, or deployed behavior from a design alone.

When an experiment is needed to choose a solution, state the hypothesis, smallest useful test, relevant prerequisites/effects, and what result would change the decision. Keep dependent decisions conditional. Do not install dependencies, generate a prototype, execute uncertain checks, or start another mode merely to make the design appear complete. Follow the read-only boundary for any justified executable inquiry.

## Output and completion

Deliver a proportionate proposal in the conversation containing:

- the recommended solution and scope;
- relevant contracts, invariants and structure or flow;
- changes from current behavior and their rationale;
- meaningful rejected alternatives and tradeoffs, when they aid assessment;
- compatibility, transition and material risks where relevant;
- validation strategy and remaining decisions or unverified hypotheses.

No fixed template or separate document per technical layer is required. Persist only a document requested under the skill's narrow exception. Its existence or polished form does not imply acceptance.

The design is resolved when decisions that materially change the result or risk are settled and the affected contracts are coherent enough to implement. State what remains unverified even when the design decision is sound. If a core choice depends on missing evidence or a user decision, report that limitation rather than declaring the whole design implementation-ready.

Do not force a subsequent PLAN or BUILD. Approval of the design alone grants no execution permission; an already authorized combined design-and-implementation request may continue under the relevant execution mode without redundant confirmation. Later consumers must verify material assumptions against their current target and revisit only decisions actually invalidated by new evidence.
