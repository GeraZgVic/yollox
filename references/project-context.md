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

All recorded paths are normalized relative to the Git root and contain no `..` traversal. Before INIT reads an existing path or records a `working_directory`, its canonical target must remain inside the Git root; do not follow or accept a symlink that resolves outside it. `validation.yaml` records each command's working directory separately instead of encoding it with `cd`. Keep every file compact, evidence-based, and useful for future navigation. Do not duplicate the same narrative across files.

## General evidence rules

- Record only durable knowledge that changes future navigation, scoping, or technical decisions.
- Cite concise repository-relative evidence paths for architectural and convention claims.
- Prefer current source, manifests, configuration, schema, and tests over non-canonical prose.
- Keep each fact within the environment or scope its evidence demonstrates. Evidence limited to local, development, test, staging, production, CI, container-only, or optional tooling does not establish a project-wide fact unless repository evidence demonstrates that broader scope. This applies to runtime, database, and service versions; deployment configuration; environment-specific integrations; feature flags; validation prerequisites; and provider configuration.
- Prefer a compact scoped fact, `UNKNOWN` when the broader value is material, or omission over promoting narrower evidence into a global claim. Do not require verbose environment sections when omission is equally correct and useful.
- Omit optional fields or sections lacking useful evidence. Use the literal string `UNKNOWN` for a material unknown that should remain explicit.
- Never store secret values, absolute machine-specific paths, source dumps, exhaustive file lists, or transient working notes.

Generated YAML files use integer `schema_version: 1`. This format version is independent of the Yollox release version and changes only for an incompatible structural or semantic change.

## Existing-context compatibility

An existing `.yollox/` is compatible only when all of these checks pass:

- its direct contents are exactly the five required regular files shown above, with no missing or extra entry;
- `project.yaml`, `validation.yaml`, and `state.yaml` parse as YAML mappings and each contains integer `schema_version: 1`;
- `project.yaml` contains the top-level mappings `project` and `freshness`; its `freshness` contains an `evidence_sources` mapping and a `topology_watch` list;
- `validation.yaml` contains the top-level `checks` list;
- `state.yaml` contains `context_revision`, `generated_at`, `baseline_commit`, `reproducible`, and a `freshness` mapping with the applicable required fields defined below;
- `architecture.md` and `conventions.md` are readable regular files containing at least one non-whitespace character.

Optional subject areas may be omitted as described below, but required containers remain present and may be empty where the contract permits it. A parseable document with the right version but missing a required field is incompatible. INIT reports the concrete failure and does not repair or overwrite it.

## `project.yaml`

Purpose: a compact, machine-readable technical index.

Use schema version `1`. The following shape defines allowed subject areas, not a requirement to fill every field:

```yaml
schema_version: 1
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
  evidence_sources:
    project:
      - package.json
    architecture:
      - src/middleware.ts
      - src/actions/index.ts
    conventions:
      - .gitattributes
    validation:
      - package.json
      - vitest.config.ts
  topology_watch:
    - path: src/domain
      reason: domain additions, removals, or moves
    - path: src/application
      reason: application additions, removals, or moves
```

Allowed content, only with sufficient evidence:

- project identity and repository shape;
- languages, runtime, package manager, frameworks, and principal stack;
- major modules and their navigation roles;
- relevant documentation, status, and material conflicts;
- exact evidence sources grouped compactly by artifact or knowledge category, plus topology watch paths used by freshness when a Git baseline exists.

Every concrete file used to support persisted knowledge whose content could invalidate that knowledge belongs in `evidence_sources`, including source and test files. This is compact provenance by artifact or category, not per-field provenance. Record exact files; do not add whole source directories as evidence sources by default. Do not turn dependency lists, directory listings, endpoints, classes, or implementation details into index entries. Topology watches concern structural additions, deletions, renames, and moves, not every edit beneath a directory.

Preserve semantic types when classifying project context. `languages` may contain programming, query, stylesheet, or shell languages such as TypeScript, JavaScript, Python, Go, Rust, SQL, CSS, or Bash. Frameworks, tools, and formats remain in their appropriate categories; do not classify Astro, React, Vue, Svelte, Next.js, NestJS, Markdown, Docker, Drizzle, or TipTap as languages solely because corresponding files or usage exist. When classification is ambiguous, prefer the category directly demonstrated by manifests or configuration, omission, or `UNKNOWN` when the category is materially useful rather than a confident misclassification.

For example, when Compose establishes MySQL 8.4 only for local and test environments, preserve that scope:

```yaml
database:
  engine: mysql
  production_version: UNKNOWN
  local_test_version: "8.4"
```

If the detailed version adds little decision value, recording only `database.engine: mysql` is also correct; a global `version: "8.4"` is not.

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

Use schema version `1`:

```yaml
schema_version: 1
checks:
  - id: unit
    command: exact repository-native command
    working_directory: .
    scope: concise target or repository scope
    cost: low
    effects:
      tracked_files: none
      generated_outputs: []
      external_state:
        effect: none
        targets: []
    evidence:
      - path/to/manifest
```

Requirements:

- `id` is short and unique.
- `command` preserves the repository-declared package manager, task runner, and flags; do not prefix it with `cd`.
- `working_directory` is `.` or the repository-relative directory from which the command must run.
- `scope` identifies what the command validates.
- `cost` is `low`, `medium`, or `high`, inferred relatively within this repository.
- `effects.tracked_files` is `none`, `possible`, `expected`, or `UNKNOWN`.
- `effects.generated_outputs` is an empty list, a list of known repository-relative output paths, or `UNKNOWN`.
- `effects.external_state.effect` is `none`, `possible`, `expected`, or `UNKNOWN`.
- `effects.external_state.targets` is a list of compact, evidence-based labels for external state the check could touch. If `effect` is `none`, it must be `[]`. If an effect exists or may exist but no concrete target can be established, it must be the reserved list `[UNKNOWN]`; do not invent a target.
- `evidence` lists the repository-relative declarations supporting the command.

Emit `effects.external_state.effect: none` only when static repository evidence reasonably demonstrates that the relevant execution neither depends on nor accesses external state. Absence of evidence of an external effect is not evidence of absence. A validation that consumes a service URL, depends on credentials, loads database configuration, has a concrete path that can contact a database, network or container service, cloud provider, external API, or external process, or depends on tool behavior that cannot be determined statically with sufficient confidence must not be classified as `none`.

Apply the categories conservatively and independently of cost, tracked-file effects, generated outputs, or the apparent strength of the validation: use `expected` when evidence demonstrates interaction with external state, `possible` when a concrete path or configuration can produce the interaction but it need not occur on every execution, and `UNKNOWN` when proportional static discovery cannot determine the effect safely. Use `none` only for reasonably demonstrated absence. Future consumers must interpret `UNKNOWN` in `external_state.targets` conservatively: it does not mean that no external target exists. An empty target list is invalid when `effect` is `possible`, `expected`, or `UNKNOWN`; when the effect is not `none` and no target is established, use `[UNKNOWN]` and do not invent a target.

Build the `checks` list by first preserving the minimum demonstrated validation set identified by the discovery workflow. A current, coherent command that current evidence explicitly establishes as a normal, required, or baseline project check must remain in that set; do not omit it merely because another validation appears broader or stronger. Distinct properties remain distinct: E2E does not automatically replace build, a full test suite does not automatically replace typecheck, and build does not automatically replace tests. Canonicalize aliases only when current evidence demonstrates equivalence. Clearly stale or `historical` documentation does not create a requirement; apply the documented `current`, `mixed`, `historical`, and `conflicting` classifications when deciding whether prose is current evidence. After preserving this minimum, additional materially useful, compact, evidence-backed checks may be included.

For example, a check known to touch a test database records:

```yaml
external_state:
  effect: expected
  targets:
    - test_database
```

When the effect is possible but its target is not established:

```yaml
external_state:
  effect: possible
  targets:
    - UNKNOWN
```

An empty `checks: []` is valid when no real validation command can be established. Do not include commands primarily for production mutation, database changes, migrations, releases, or deployment.

## `state.yaml`

Purpose: minimal lifecycle and Git freshness state, not agent or conversation state.

When HEAD resolves, use this shape:

```yaml
schema_version: 1
context_revision: 1
generated_at: "2026-01-01T00:00:00Z"
baseline_commit: full-git-object-id
branch: branch-name
reproducible: true
freshness:
  strategy: git-path-diff
  comparison_base: baseline_commit
  relevant_change_means: possibly_stale
```

When HEAD does not resolve, use this shape instead:

```yaml
schema_version: 1
context_revision: 1
generated_at: "2026-01-01T00:00:00Z"
baseline_commit: UNKNOWN
reproducible: false
freshness:
  strategy: unavailable
  status: possibly_stale
  reason: no_baseline_commit
```

Rules:

- `generated_at` is the actual UTC RFC 3339 generation time.
- `baseline_commit` is the resolved HEAD object ID; use `UNKNOWN` when HEAD does not resolve.
- Include `branch` only when Git reports one. A detached HEAD needs no invented branch.
- `reproducible` is false when HEAD is unavailable or any selected relevant input differs from HEAD.
- When HEAD resolves, `freshness` requires `strategy: git-path-diff`, `comparison_base: baseline_commit`, and `relevant_change_means: possibly_stale`.
- When HEAD does not resolve, `freshness` requires `strategy: unavailable`, `status: possibly_stale`, and `reason: no_baseline_commit`; do not include `comparison_base` or declare `git-path-diff`.
- When false because of dirty inputs, add only:

```yaml
non_reproducible_inputs:
  - path: repo/relative/path
    status: concise-git-status
```

Do not add repository-wide hashes, ConfigHash, per-file hashes, fingerprints, snapshots, runtime state, agent state, conversation state, history, or learning data.
