---
name: yollox
description: Use Yollox in Codex for bounded engineering work in a Git repository, from a natural-language objective or an explicit planning, design, review, cleanup, fix, build, deployment, or project-context request.
---

# Yollox

Yollox v0.1-alpha9 is a Codex-native skill for project context and scoped engineering work. The intent entry selects and composes existing capabilities to fulfill an authorized objective. INIT creates a compact project index. PLAN structures proposed work; DESIGN resolves technical decisions. REVIEW reports evidenced defects without editing; CLEAN, FIX, BUILD, and DEPLOY use relevant context to complete their distinct requested outcomes.

Principles:

- Correctness and requested scope outrank token reduction.
- Compact project context + complete target understanding + repository on demand.
- Persist durable knowledge only. `.yollox/` is an index, not an encyclopedia.
- Current applicable repository evidence outranks `.yollox/` whenever they conflict.

## Invocation and routing

- `$yollox: <objective>`: read [references/intent.md](references/intent.md) completely, then select only the capabilities needed for the requested outcome. The user need not name modes; permissions follow the request, not the selection.
- `$yollox init`: read [references/init.md](references/init.md) completely, then follow it. Read [references/project-context.md](references/project-context.md) when preparing or interpreting the generated files.
- `$yollox init --dry-run`: read the same references and perform the same discovery reasoning without writing anything.
- `$yollox plan: <objective>`: propose bounded, verifiable work; read [references/plan.md](references/plan.md) completely.
- `$yollox design: <objective>`: resolve material technical decisions without implementation; read [references/design.md](references/design.md) completely.
- `$yollox review: <objective>`: read [references/review.md](references/review.md) completely, then follow it. Read [references/project-context.md](references/project-context.md) when consuming `.yollox/`; do not load or execute INIT for REVIEW.
- `$yollox clean: <objective>`: improve maintainability while preserving observable behavior; read [references/clean.md](references/clean.md).
- `$yollox fix: <objective>`: correct an evidenced defect; read [references/fix.md](references/fix.md).
- `$yollox build: <objective>`: implement requested behavior; read [references/build.md](references/build.md).
- `$yollox deploy: <objective>`: prepare a deployment path or publish a resolved release; read [references/deploy.md](references/deploy.md).
- Any other Yollox command or mode is not implemented. Say so without approximating it through another workflow.

For CLEAN, FIX, BUILD, and DEPLOY, read [references/execution.md](references/execution.md) and the selected mode reference completely once. Read the Project Context contract when consuming `.yollox/`. Do not load unrelated modes or INIT. Modes do not invoke each other automatically; an explicitly combined request or the intent entry may select the capabilities necessary for the authorized outcome without a mandatory mode sequence. The same mode contracts apply whether selected by name or through intent. Completing one capability does not authorize another.

PLAN and DESIGN are optional, independent capabilities, not prerequisites for other modes. Load only the requested or needed proposal references, plus [references/project-context.md](references/project-context.md) when consuming `.yollox/`; proposal work does not inherit editing permissions from `execution.md` or run INIT. A combined planning-and-design request can receive one coherent proposal without duplicate documents.

Explicit modes retain their boundaries. Do not reinterpret a pure PLAN, DESIGN, REVIEW, CLEAN, or deployment-preparation request as broader execution, or an unsupported command as an intent request. The intent entry never initializes or maintains Project Context implicitly; INIT remains an explicitly requested lifecycle operation.

## Global constraints

- Yollox v0.1 requires a Git repository.
- Git discovery must use read-only queries. For any query that can take optional locks or refresh Git metadata, invoke Git with `GIT_OPTIONAL_LOCKS=0` or the equivalent `git --no-optional-locks`; this is mandatory during dry-run.
- Never treat `.yollox/` as absolute authority; verify applicable behavior against current source, configuration, schema, tests, or genuinely canonical documentation.
- Neither the intent entry nor a mode invocation grants implicit Git mutation permission. During INIT, REVIEW, PLAN, and DESIGN, do not perform Git mutations, including add, commit, push, merge, reset, checkout, stash, branch creation, or branch deletion. During CLEAN, FIX, BUILD, and DEPLOY, a concrete Git operation requires explicit user authorization and must preserve unrelated user work.
- Do not create agent state, memory, snapshots, worktrees, histories, specs, orchestration artifacts, repo-wide hashes, per-file hashes, or fingerprints used as context machinery. Git object IDs such as `baseline_commit` are allowed.
- Never persist credentials, secret values, or sensitive environment contents.

## PLAN and DESIGN boundaries

- Deliver in the conversation and remain READ-ONLY by default: no product edits, installations, experiments, caches, generated outputs, Git mutations, or implicit external effects. A command is justified only if it resolves a material question and its foreseeable effects satisfy this boundary. Do not execute checks merely to decorate a proposal with validation.
- Resolve the Git root and applicable instructions; outside a Git worktree, report the prerequisite without creating one. Canonicalize repository pointers and working directories before following them; do not silently cross escaping symlinks or repository boundaries. Use read-only Git queries without external diff helpers or textconv, and protect secret values.
- Write a proposal document only when the user requests persistence or document editing as a deliverable. Use the requested location or an unambiguous existing repository convention, preserve unrelated content, and resolve material destination or overwrite ambiguity before writing. This narrow document permission does not authorize implementation, execution, Git mutations, or other artifacts; a requested project document is not auxiliary agent state.
- Never initialize, repair, refresh, or store proposals in `.yollox/`. Do not create task IDs, approval registries, lifecycle state, histories, or an automatic document store. Mark recommendations and unresolved decisions honestly; document existence does not mean approval. Cross-session reuse requires the conversation or an identified document, not hidden memory.

## Using plans and designs

- Consume a proposal when the user identifies it, the conversation establishes its applicability, or it is genuinely canonical project documentation. Do not automatically load the newest plan or infer authority from a feature filename. Verify material assumptions against the current target; resolve routine implementation differences without redesigning everything, and revisit decisions when new evidence materially invalidates them.
- Plans and designs do not replace mode obligations: FIX still establishes causality, CLEAN preserves equivalence, BUILD satisfies applicable acceptance criteria, DEPLOY verifies the candidate and authorized effects, and REVIEW reports evidenced violations rather than architectural preferences or match scores.
- Approval of a proposal alone does not authorize implementation or deployment. When the request already includes designing/planning and executing, continue within that authorization without redundant confirmation; unresolved material decisions or effects still need resolution. No automatic PLAN-to-DESIGN-to-BUILD sequence is required.

## INIT constraints

- INIT may write only under `.yollox/**` plus one reserved, temporary sibling staging directory named `.yollox.tmp-*` during atomic publication. Dry-run is completely read-only and never creates staging.
- Do not modify project source, tests, existing documentation, manifests, lockfiles, migrations, CI, container configuration, or other existing project files.
- Do not install dependencies or run tests, builds, integration suites, containers, migrations, audits, deployment, or validation commands during INIT.

## REVIEW constraints

- REVIEW is READ-ONLY by default, including untracked and ignored files, `.yollox/`, Git metadata, and external state. Apply the validation and explicit-authorization rules in [references/review.md](references/review.md).
- REVIEW never initializes, repairs, refreshes, or persists Project Context and never transitions automatically into editing or another mode.

## CLEAN, FIX, BUILD, and DEPLOY constraints

- Apply the shared execution contract and selected mode's boundaries. Local changes and validation effects must serve the requested outcome; remote effects require authorization for the concrete operation and target.
- Never initialize, repair, refresh, or persist `.yollox/` as a side effect of these modes.
- The prohibition on auxiliary context machinery does not prohibit justified project-native test fixtures/snapshots, dependency lockfiles, deployment artifacts/identifiers, or native tool state required by an authorized operation. INIT and REVIEW retain their stricter boundaries.
