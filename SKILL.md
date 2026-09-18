---
name: yollox
description: Use Yollox in Codex to create compact project context, review scoped targets, clean code, fix defects, build requested capabilities, or prepare and execute deployments in a Git repository.
---

# Yollox

Yollox v0.1-alpha7 is a Codex-native skill for project context and scoped engineering work. INIT creates a compact project index. REVIEW reports evidenced defects without editing; CLEAN, FIX, BUILD, and DEPLOY use relevant context to complete their distinct requested outcomes.

Principles:

- Correctness and requested scope outrank token reduction.
- Compact project context + complete target understanding + repository on demand.
- Persist durable knowledge only. `.yollox/` is an index, not an encyclopedia.
- Current applicable repository evidence outranks `.yollox/` whenever they conflict.

## Invocation and routing

- `$yollox init`: read [references/init.md](references/init.md) completely, then follow it. Read [references/project-context.md](references/project-context.md) when preparing or interpreting the generated files.
- `$yollox init --dry-run`: read the same references and perform the same discovery reasoning without writing anything.
- `$yollox review: <objective>`: read [references/review.md](references/review.md) completely, then follow it. Read [references/project-context.md](references/project-context.md) when consuming `.yollox/`; do not load or execute INIT for REVIEW.
- `$yollox clean: <objective>`: improve maintainability while preserving observable behavior; read [references/clean.md](references/clean.md).
- `$yollox fix: <objective>`: correct an evidenced defect; read [references/fix.md](references/fix.md).
- `$yollox build: <objective>`: implement requested behavior; read [references/build.md](references/build.md).
- `$yollox deploy: <objective>`: prepare a deployment path or publish a resolved release; read [references/deploy.md](references/deploy.md).
- Any other Yollox command or mode is not implemented. Say so without approximating it through another workflow.

For CLEAN, FIX, BUILD, and DEPLOY, read [references/execution.md](references/execution.md) and the selected mode reference completely once. Read the Project Context contract when consuming `.yollox/`. Do not load unrelated modes or INIT. Modes do not invoke each other automatically; an explicitly combined request may use the necessary references without a mandatory mode sequence.

## Global constraints

- Yollox v0.1 requires a Git repository.
- Git discovery must use read-only queries. For any query that can take optional locks or refresh Git metadata, invoke Git with `GIT_OPTIONAL_LOCKS=0` or the equivalent `git --no-optional-locks`; this is mandatory during dry-run.
- Never treat `.yollox/` as absolute authority; verify applicable behavior against current source, configuration, schema, tests, or genuinely canonical documentation.
- No mode invocation grants implicit Git mutation permission. During INIT and REVIEW, do not perform Git mutations, including add, commit, push, merge, reset, checkout, stash, branch creation, or branch deletion. During CLEAN, FIX, BUILD, and DEPLOY, a concrete Git operation requires explicit user authorization and must preserve unrelated user work.
- Do not create agent state, memory, snapshots, worktrees, histories, specs, orchestration artifacts, repo-wide hashes, per-file hashes, or fingerprints used as context machinery. Git object IDs such as `baseline_commit` are allowed.
- Never persist credentials, secret values, or sensitive environment contents.

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
