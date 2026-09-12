# Project context contract

INIT creates exactly:

```text
.yollox/
|-- project.yaml
|-- architecture.md
|-- conventions.md
|-- validation.yaml
`-- state.yaml
```

All recorded paths and commands are relative to the Git root unless the command itself requires another working directory. Keep every file compact, evidence-based, and useful for future navigation. Do not duplicate the same narrative across files.

## General evidence rules

- Record only durable knowledge that changes future navigation, scoping, or technical decisions.
- Cite concise repository-relative evidence paths for architectural and convention claims.
- Prefer current source, manifests, configuration, schema, and tests over non-canonical prose.
- Omit optional fields or sections lacking useful evidence. Use the literal string `UNKNOWN` for a material unknown that should remain explicit.
- Never store secret values, absolute machine-specific paths, source dumps, exhaustive file lists, or transient working notes.

## `project.yaml`

Purpose: a compact, machine-readable technical index.

Use schema version `"0.1"`. The following shape defines allowed subject areas, not a requirement to fill every field:

```yaml
schema_version: "0.1"
project:
  name: example
  identity: compact evidence-based description
  repository_shape: monorepo
languages:
  - name: TypeScript
    role: primary
runtime:
  name: Node.js
  version: "UNKNOWN"
package_manager:
  name: pnpm
  evidence: pnpm-lock.yaml
frameworks:
  - name: example-framework
    role: application
    evidence: path/to/manifest
stack:
  - compact, decision-relevant stack fact
modules:
  - name: api
    path: apps/api
    role: public service boundary
documentation:
  status: mixed
  sources:
    - path: README.md
      status: current
      role: developer entrypoint
  conflicts:
    - compact conflict with evidence paths
freshness:
  structural_sources:
    - path: path/to/manifest
      reason: defines workspace topology
  topology_watch:
    - path: apps
      reason: application additions, removals, or moves
```

Allowed content, only with sufficient evidence:

- project identity and repository shape;
- languages, runtime, package manager, frameworks, and principal stack;
- major modules and their navigation roles;
- relevant documentation, status, and material conflicts;
- structural sources and topology watch paths used by `git-path-diff` freshness.

Do not turn dependency lists, directory listings, endpoints, classes, or implementation details into index entries. Topology watches concern structural path changes, not every edit beneath a directory.

## `architecture.md`

Purpose: durable, global architectural knowledge that cannot be expressed well as the compact index.

Include only evidenced sections that are material:

- system shape and main boundaries;
- major module relationships;
- persistence model;
- auth/authz model;
- important external boundaries;
- deployment shape;
- critical global invariants.

Use short prose or bullets and attach repository-relative evidence paths to claims. Omit inapplicable sections. Do not catalog classes, functions, endpoints, local constants, detailed module implementations, or speculative future design.

## `conventions.md`

Purpose: repository-specific conventions demonstrated by repeated current evidence or an authoritative repository configuration.

For each convention, state the rule compactly and cite its evidence path. Record only conventions that future edits need to follow. Do not include generic clean-code advice, personal preferences, unverified formatting rules, or framework practices that the repository does not demonstrate.

When evidence is mixed, record the mixed pattern only if knowing it prevents an incorrect edit; do not invent a unifying rule.

## `validation.yaml`

Purpose: statically discovered, real validation commands. INIT never runs these commands.

Use schema version `"0.1"`:

```yaml
schema_version: "0.1"
checks:
  - id: unit
    command: exact repository-native command
    scope: concise target or repository scope
    cost: low
    effects:
      tracked_files: none
      generated_outputs: []
      external_state: none
    evidence:
      - path/to/manifest
```

Requirements:

- `id` is short and unique.
- `command` preserves the repository-declared package manager, task runner, flags, and working-directory assumptions.
- `scope` identifies what the command validates.
- `cost` is `low`, `medium`, or `high`, inferred relatively within this repository.
- `effects.tracked_files` is `none`, `possible`, `expected`, or `UNKNOWN`.
- `effects.generated_outputs` is an empty list, a list of known repository-relative output paths, or `UNKNOWN`.
- `effects.external_state` is `none`, `possible`, `expected`, or `UNKNOWN`.
- `evidence` lists the repository-relative declarations supporting the command.

An empty `checks: []` is valid when no real validation command can be established. Do not include commands primarily for production mutation, database changes, migrations, releases, or deployment.

## `state.yaml`

Purpose: minimal lifecycle and Git freshness state, not agent or conversation state.

Use this shape:

```yaml
schema_version: "0.1"
context_revision: 1
generated_at: "2026-01-01T00:00:00Z"
baseline_commit: full-git-object-id-or-UNKNOWN
branch: branch-name
reproducible: true
freshness:
  strategy: git-path-diff
  comparison_base: baseline_commit
  relevant_change_means: possibly_stale
```

Rules:

- `generated_at` is the actual UTC RFC 3339 generation time.
- `baseline_commit` is the resolved HEAD object ID; use `UNKNOWN` when HEAD does not resolve.
- Include `branch` only when Git reports one. A detached HEAD needs no invented branch.
- `reproducible` is false when HEAD is unavailable or any selected relevant input differs from HEAD.
- When false because of dirty inputs, add only:

```yaml
non_reproducible_inputs:
  - path: repo/relative/path
    status: concise-git-status
```

Do not add repository-wide hashes, ConfigHash, per-file hashes, fingerprints, snapshots, runtime state, agent state, conversation state, history, or learning data.
