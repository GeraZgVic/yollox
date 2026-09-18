---
name: yollox
description: Create a compact, persistent project index and review explicit targets with current repository evidence in Codex. Use for Yollox init, init --dry-run, and review requests in a Git repository.
---

# Yollox

Yollox v0.1-alpha6 is a Codex-native skill for project context and scoped review. INIT creates a compact project index; REVIEW uses useful context to navigate to repository evidence and report material defects without editing.

Principles:

- Correctness and requested scope outrank token reduction.
- Compact project context + complete target understanding + repository on demand.
- Persist durable knowledge only. `.yollox/` is an index, not an encyclopedia.
- Current applicable repository evidence outranks `.yollox/` whenever they conflict.

## Invocation and routing

- `$yollox init`: read [references/init.md](references/init.md) completely, then follow it. Read [references/project-context.md](references/project-context.md) when preparing or interpreting the generated files.
- `$yollox init --dry-run`: read the same references and perform the same discovery reasoning without writing anything.
- `$yollox review: <objective>`: read [references/review.md](references/review.md) completely, then follow it. Read [references/project-context.md](references/project-context.md) when consuming `.yollox/`; do not load or execute INIT for REVIEW.
- Any other Yollox command or mode is not implemented. Say so without approximating it through another workflow.

## Global constraints

- Yollox v0.1 requires a Git repository.
- Git discovery must use read-only queries. For any query that can take optional locks or refresh Git metadata, invoke Git with `GIT_OPTIONAL_LOCKS=0` or the equivalent `git --no-optional-locks`; this is mandatory during dry-run.
- Never treat `.yollox/` as absolute authority; verify applicable behavior against current source, configuration, schema, tests, or genuinely canonical documentation.
- Do not perform Git mutations, including add, commit, push, merge, reset, checkout, stash, branch creation, or branch deletion.
- Do not create agent state, memory, snapshots, worktrees, histories, specs, orchestration artifacts, repo-wide hashes, per-file hashes, or fingerprints used as context machinery. Git object IDs such as `baseline_commit` are allowed.
- Never persist credentials, secret values, or sensitive environment contents.

## INIT constraints

- INIT may write only under `.yollox/**` plus one reserved, temporary sibling staging directory named `.yollox.tmp-*` during atomic publication. Dry-run is completely read-only and never creates staging.
- Do not modify project source, tests, existing documentation, manifests, lockfiles, migrations, CI, container configuration, or other existing project files.
- Do not install dependencies or run tests, builds, integration suites, containers, migrations, audits, deployment, or validation commands during INIT.

## REVIEW constraints

- REVIEW is READ-ONLY by default, including untracked and ignored files, `.yollox/`, Git metadata, and external state. Apply the validation and explicit-authorization rules in [references/review.md](references/review.md).
- REVIEW never initializes, repairs, refreshes, or persists Project Context and never transitions automatically into editing or another mode.
