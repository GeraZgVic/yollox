---
name: yollox
description: Build a compact, persistent repository context for Codex. Use for `$yollox init` and `$yollox init --dry-run` in a Git repository; no build, fix, review, deploy, sync, or other execution modes are implemented.
---

# Yollox

Yollox v0.1-alpha4 is a Codex-native project lifecycle skill. It creates a compact project index so later work can navigate from durable knowledge to current repository evidence without rereading the whole repository.

Principles:

- Compact project context + complete target understanding + repository on demand.
- Persist durable knowledge only. `.yollox/` is an index, not an encyclopedia.
- Current applicable repository evidence outranks `.yollox/` whenever they conflict.

## Invocation and routing

- `$yollox init`: read [references/init.md](references/init.md) completely, then follow it. Read [references/project-context.md](references/project-context.md) when preparing or interpreting the generated files.
- `$yollox init --dry-run`: read the same references and perform the same discovery reasoning without writing anything.
- Any other Yollox command or mode is not implemented. Say so without approximating it through another workflow.

## Global constraints

- Yollox v0.1 requires a Git repository.
- INIT may write only under `.yollox/**` plus one reserved, temporary sibling staging directory named `.yollox.tmp-*` during atomic publication. Dry-run is completely read-only and never creates staging.
- Git discovery must use read-only queries. For any query that can take optional locks or refresh Git metadata, invoke Git with `GIT_OPTIONAL_LOCKS=0` or the equivalent `git --no-optional-locks`; this is mandatory during dry-run.
- Never treat `.yollox/` as absolute authority; verify applicable behavior against current source, configuration, schema, tests, or genuinely canonical documentation.
- Do not modify project source, tests, existing documentation, manifests, lockfiles, migrations, CI, container configuration, or other existing project files.
- Do not install dependencies or run tests, builds, integration suites, containers, migrations, audits, deployment, or validation commands during INIT.
- Do not perform Git mutations, including add, commit, push, merge, reset, checkout, stash, branch creation, or branch deletion.
- Do not create agent state, memory, snapshots, worktrees, histories, specs, orchestration artifacts, repo-wide hashes, per-file hashes, or fingerprints used as context machinery. Git object IDs such as `baseline_commit` are allowed.
- Never persist credentials, secret values, or sensitive environment contents.
