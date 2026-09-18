# CLEAN workflow

Use for `$yollox clean: <objective>` with [execution.md](execution.md).

## Responsibility

Improve maintainability across the complete requested target while preserving observable behavior. CLEAN is neither formatting alone nor a review that opportunistically fixes defects.

Resolve an explicit or clearly implied target. Use bounded search to locate a described area; ask when the scope remains materially ambiguous rather than cleaning the repository by default. Exclude generated, vendored, minified and build outputs unless explicitly targeted; do not hand-edit generated content when its maintained source is the appropriate target.

## Complete, bounded inspection

Read the complete target before editing, using coherent ranges for large files or areas. Inspect nearest contracts and consumers needed to establish equivalence. Cover the target rather than sampling it, but do not search exhaustively for every possible transformation.

Consider material, evidenced opportunities such as dead code, redundant control flow or indirection, semantically equivalent duplication, unclear local names, and poor cohesion. These are judgment aids, not quotas or a checklist requiring edits in every category. Do not stop after the first improvement merely to minimize the diff when other material, well-supported improvements remain in the agreed target.

## Equivalence and changes

For each change, establish what remains equivalent and why. Preserve public APIs, data shapes, errors, effect ordering, persistence and security semantics, plus operational logging, performance, accessibility and visual behavior where relevant.

- Missing textual references do not prove code is dead when dynamic registration, reflection, generated consumers or external callers may use it.
- Similar-looking logic is not necessarily equivalent; check conditions, evaluation order and side effects before consolidating it.
- A debug-looking log or apparently redundant guard may be part of a real operational or defensive contract. Do not remove it on appearance alone.
- Extract helpers or constants when they reduce demonstrated complexity and remain local unless broader reuse is justified. Split files only for material cohesion or maintainability benefit, never a line-count target.
- Do not add dependencies or speculative abstractions to manufacture a cleanup benefit. No unrelated modernization, broad style normalization, architecture rewrite or security remediation.

If a discovered defect is independent of cleanup, report it briefly when material but do not fix it automatically. If it prevents establishing safe equivalence, leave the affected transformation unapplied and explain the limitation. When the user explicitly requests both cleanup and a behavior change, honor the combined scope and distinguish preservation work from the authorized behavioral change; do not silently broaden a pure CLEAN request.

## Validation and completion

Use equivalence reasoning plus relevant native checks under the shared effect policy. Run useful affected tests and analysis; add coverage only when it materially establishes a delicate contract. Simple cleanup does not require new tests that mirror the transformation. Syntax, lint or diff sanity alone cannot establish a behavioral equivalence they do not check.

Complete when the target has received a full bounded pass, material justified improvements have been applied, unrelated behavior is preserved to the stated evidence level, and the final diff is within scope. Report substantive cleanup, changed files, validation and any material equivalence or coverage limitation.

No material safe improvement is a valid no-change result. Incomplete target coverage must be reported as partial; it must not be disguised as a completed cleanup or used to justify speculative edits.
