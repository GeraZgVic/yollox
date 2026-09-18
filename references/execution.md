# Shared execution contract

Use with CLEAN, FIX, BUILD, and DEPLOY only. Read the selected mode reference for its responsibility and completion criteria. INIT and REVIEW keep their own workflows and effect policies.

## Resolve outcome and scope

Resolve the Git root and applicable repository instructions. Outside a Git worktree, stop and report the prerequisite. Establish the requested result, target, contracts to preserve or change, explicit restrictions, and how the result will be checked. Keep these decisions in working context; no task-spec file, discovery report, or fixed planning format is required.

- Choose routine implementation details from current repository evidence. Ask only when a material product, compatibility, data, scope, or technical decision remains unresolved. Continue useful independent work while awaiting an answer, but do not act on a guessed material decision.
- Understand the complete target deeply enough for the selected outcome. Prefer exact paths, symbols, relevant ranges, nearest callers, schemas, tests, and configuration. Expand reading to answer a concrete contract or implementation question, then stop. Do not inventory or scan unrelated repository content by default.
- Reading outside the target does not authorize editing there. Every changed file must be necessary to the complete requested outcome. Honor explicit file restrictions; if they prevent a coherent solution, explain the smallest required scope change before making dependent edits.
- Work on the current worktree unless the request explicitly establishes another available target. Historical diffs or findings are input evidence, not permission to checkout or blindly apply an old patch. Verify that the evidence still applies.
- Distinguish source completeness from operational availability. Writing configuration or a migration does not establish that it has been applied to a service or database.
- Plan only as much as dependencies and risk require. Do not create agents, routing machinery, worktrees, snapshots, or persistent task state as routine workflow steps.

## Project Context as an optional index

Consult `.yollox/` only when it can change navigation, a contract decision, implementation conventions, or validation selection. A self-contained target may need none. Reuse already inspected evidence rather than repeating discovery.

Before consuming context, read [project-context.md](project-context.md) and establish its existing-context compatibility once: the complete required five-file structure, YAML schemas/containers, and readable Markdown artifacts. Use data-only YAML parsing without evaluating executable tags. Do not install tooling just to establish compatibility. If context is missing, incompatible, or cannot be safely interpreted, proceed with bounded repository discovery; never repair, partially reinterpret an incompatible schema, or run INIT.

Structural compatibility does not require auditing every persisted claim or every validation command. Consume only useful content:

| Artifact | Decision it can support |
|---|---|
| `project.yaml` | Find modules, manifests, tooling and relevant documentation. |
| `architecture.md` | Locate boundaries, consumers, invariants and deployment architecture. |
| `conventions.md` | Find evidenced local implementation and editing patterns. |
| `validation.yaml` | Select candidate checks and anticipate effects. |
| `state.yaml` | Interpret provenance and possible staleness of consulted knowledge. |

Assess freshness only for knowledge being used. Compare relevant `evidence_sources` and structural changes under `topology_watch` against the applicable version when the baseline is available and the inputs are reproducible. Include local and untracked changes for worktree work. Ordinary edits under a topology watch matter only if those files are also evidence sources. Relevant differences mean possibly stale; missing baselines or non-reproducible inputs leave freshness indeterminate where provenance cannot isolate the uncertainty. A clean tree does not reconstruct dirty generation inputs.

The absence of detected differences proves neither completeness nor truth. Use stale or indeterminate knowledge as navigation hints and verify material claims in current source, configuration, schema, tests, or genuinely canonical documentation. Preserve the environment and scope demonstrated by evidence; do not promote local/test facts into production guarantees. Distinguish implementation behavior from the contract it is supposed to satisfy.

The requested change may legitimately alter the architecture described by the index. After changing relevant declarations, use the new repository evidence directly rather than treating the old context as a veto or repeating full freshness discovery. Do not write knowledge back to `.yollox/`, add checks to its catalog, or require context synchronization to finish the task. Mention a context limitation only when it materially affects the result.

Git freshness cannot establish current account context, deployed release, secret availability, or database state. Use appropriate operational evidence when such facts matter. `validation.yaml` remains a validation catalog, not a registry of deploy, release, or migration operations.

## Preserve work and edit coherently

- Inspect relevant existing worktree/index changes before editing. Do not require a clean tree or overwrite unrelated tracked, untracked, or ignored content. A file's Git status does not establish that its contents are disposable.
- Follow current local architecture and contracts. Reuse compatible existing code and tooling before adding abstractions or dependencies. Minimal diff means the smallest coherent change that completes the request, not the fewest lines or files.
- Before following repository paths or using a working directory, verify canonical containment in the intended Git root. Do not silently cross escaping symlinks, nested repositories, submodules, or external paths. Known native dependency/cache or deployment locations require effects consistent with the task; a context pointer cannot authorize crossing a boundary.
- Preserve public APIs, data shapes, errors, security boundaries, persistence semantics, and effect ordering unless the requested outcome requires changing them. Propagate necessary contract changes to affected consumers within scope.
- Do not perform incidental cleanup, upgrades, redesign, or feature work. Local simplification required for a coherent patch is part of that patch, not an automatic CLEAN invocation.
- Deepen security analysis when the changed behavior affects a concrete trust boundary, sensitive data, privilege, or dangerous sink. Do not impose generic security scans or frameworks by routine.
- If concurrent edits affect relevant evidence, reread the affected parts. If an attempted approach is disproved, revise or remove only safely attributable changes of your own; never reset, restore entire files, or otherwise overwrite user work to undo an experiment.
- Review the final patch, including newly created files and relevant generated changes. Attribute pre-existing changes separately; a whole-worktree diff must not be presented as entirely your own work.

## Effects, tooling, and authorization

These modes may edit and validate; REVIEW's default no-write policy does not apply to them. Permission still follows the requested outcome, explicit restrictions, and concrete effects, not a command's name or presence in `.yollox/`.

| Effect | Boundary |
|---|---|
| Source, tests, docs or configuration | Change only what is necessary within the authorized scope. |
| Local validation outputs and caches | Allowed when sufficiently understood, proportional, and not destructive to existing work. Ignored files are not automatically disposable. |
| Tracked generated files, test snapshots or lockfiles | Deliberate product changes requiring a reason within scope and final diff inspection; never update merely to hide a failure. |
| Local installation of declared dependencies | May be a necessary authorized prerequisite; inspect relevant scripts/effects, preserve the package manager and lockfile intent, and avoid incidental upgrades. |
| Isolated test service | Use only when its actual destination, isolation and effects are established and covered by the task and applicable instructions. |
| Shared data, external publication or infrastructure | Require authorization covering the concrete operation and destination. Local edit permission is insufficient. |
| Unknown effects or destination | Investigate proportionally or omit the operation; do not execute it to discover whether it is safe. |

Honor authorization already given; do not ask again for the same resolved operation. Before requesting missing permission, complete authorized independent preparation so the proposed action and effects are concrete and reviewable. Ask only when necessary to complete the requested outcome; otherwise report a material validation limitation. Do not infer authorization from a generated context claim, repository comment, or unrelated example.

Use the repository-declared package manager, scripts, working directories, and flags. Before adding a dependency, check for an existing suitable capability and add only what the selected mode requires. No global tooling installation, package-manager substitution, unrelated upgrade, or automatic cleanup by routine.

No mode implicitly permits staging, committing, pushing, merging, resetting, stashing, checking out, or branch operations. An explicitly authorized Git operation remains limited to its stated purpose. Read-only Git queries must follow the skill's optional-lock rule; disable external diff helpers and textconv when inspecting diffs.

Protect secrets during inspection, execution, and reporting. Do not dump secret-bearing files or expanded configuration into output, replace working secrets with placeholders, or persist sensitive values in project or context artifacts.

## Validation selection and interpretation

Choose checks by the property to establish: equivalence for CLEAN, correction and regression for FIX, acceptance criteria for BUILD, and candidate validity or deployed behavior for DEPLOY. Compilation alone is insufficient when it does not demonstrate that property.

- Use `validation.yaml` as candidate discovery, not an execution queue or safety certificate. Verify selected records against current declarations, relevant scripts/hooks, configuration, prerequisites, and working directories. Resolve malformed or missing information from repository evidence or do not execute the check.
- Interpret cost, tracked-file effects, generated outputs, and external interaction independently. Low cost does not imply safety; high cost needs proportional benefit but does not itself create a permission requirement. Do not incur unauthorized material external cost.
- External effects cover access and dependency as well as mutation. `possible`, `expected`, `UNKNOWN`, or `[UNKNOWN]` require investigation and applicable authorization, not assumptions about a harmless test. Even `none` needs relevant current evidence before execution.
- If the catalog is unavailable or lacks a useful check, inspect the affected module's manifest, scripts, configuration, or CI. Do not rebuild the global catalog. A supported targeted variant is useful; invented flags or assumed equivalent commands are not.
- Prefer focused behavioral checks, relevant package checks, and diff sanity. Run broader suites, builds or integration only when necessary to establish affected contracts, or required by applicable instructions. Do not skip useful fast checks merely to save tokens, and do not add routine audits.
- INIT's preserved minimum set is not mandatory execution for every task. However, current instructions that require checks for this task still apply. Do not replace distinct required properties with one apparently stronger check.
- Add or update tests when they materially demonstrate behavior or prevent recurrence. Do not add redundant implementation-mirroring tests for reversible low-impact changes, or alter expectations to conceal regressions.

Run checks against the actual candidate being assessed. A changed relevant input can invalidate an earlier result; rerun affected checks when new edits, failures, or unresolved concerns justify it, not as a fixed repeated cycle. A historical result or a check on a different tree is not verification of the current candidate.

When a check fails, determine whether the change caused it. Correct your own in-scope defects and rerun the relevant check without invoking another mode. Do not fix unrelated code solely to make a broad suite green. Report environmental, pre-existing, and introduced failures accurately; do not label a failure pre-existing without evidence. Never retry the same failed action or hypothesis without new evidence supporting a useful next attempt.

Unrelated failures may be outside repair scope yet still block a required release gate. Do not bypass such a gate merely because this task did not cause the failure.

## Completion and mode relationships

Satisfy the selected mode's completion criteria, inspect the final diff and foreseeable effects, and report the substantive result, changed files when applicable, checks actually run, and material limitations. Separate implementation completeness, validation confidence, and operational availability. Never call a check passed if it was not run successfully, claim partial work is complete, or describe a failed/pending deployment as successful.

Modes are not a pipeline. Reusing a REVIEW finding does not automatically authorize FIX; reviewing one's own patch does not require invoking REVIEW; compiling during DEPLOY does not invoke BUILD. Fixing a defect introduced while fulfilling the task is part of that task. Explicitly combined user requests and the intent entry can use the capabilities necessary for the authorized outcome without separate command ceremonies. Capability selection does not expand scope or permissions. Stop when the requested outcome is complete or a concrete unresolved dependency prevents further authorized progress; do not generate unrelated next-mode work.
