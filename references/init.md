# INIT workflow

Use this workflow only for `$yollox init` and `$yollox init --dry-run`.

## Outcome

Construct a small, evidence-based repository index:

```text
repository
  -> cheap structural discovery
  -> selective evidence inspection
  -> durable knowledge extraction
  -> .yollox/
```

INIT is a project lifecycle operation, not an execution mode. Its only writable output is the required `.yollox/` context described in [project-context.md](project-context.md).

## Preconditions and existing context

1. Resolve the repository root with Git and operate relative to that root. If the current location is not inside a Git worktree, stop without writing and report that INIT requires a Git repository.
2. Check for `.yollox/` before discovery.
   - If all five required files exist and their YAML files are parseable with a supported schema, stop without writing and report `already initialized`.
   - If `.yollox/` exists but required files are missing, unreadable, or use an unsupported schema, stop without writing and report the concrete incompatibility.
   - Never overwrite, regenerate, repair, or delete an existing `.yollox/`. There is no `sync` in v0.1.
3. Resolve HEAD, the current branch when one exists, and worktree status. A Git repository without a resolvable HEAD may still be inspected, but its baseline is `UNKNOWN` and the result is not reproducible.

These checks are read-only in both normal and dry-run operation.

## Discovery cost order

Start with cheap evidence:

- Git metadata and tracked/untracked path inventory;
- repository-relative file and shallow directory listings;
- manifests, workspace declarations, lockfiles, and small runtime/tooling configuration.

Use medium-cost evidence only when it answers a material unresolved question:

- relevant README or documentation sections;
- entrypoints and module indexes;
- schemas and concise deployment configuration.

Use expensive evidence only as a last resort for a material question:

- service implementations;
- large routers or test files;
- migration history;
- deep data-flow tracing.

Path enumeration is acceptable. Do not perform mandatory repo-wide content reads. Prefer exact files, headings, symbols, and narrow ranges over bulk reads.

Ignore these as product-knowledge sources by default:

- `.git/` and an existing `.yollox/` beyond the precondition check;
- dependency, build, distribution, cache, coverage, and binary output directories;
- generated media;
- `.aura/`, `.autopus/`, and context or memory directories belonging to other agents.

Do not read or persist secret values. Secret-bearing filenames may establish only that a configuration boundary exists when that fact is material.

## Discovery pipeline

1. Resolve Git root, HEAD, branch, and worktree state.
2. Build a cheap Git/filesystem inventory with the exclusions above.
3. Identify manifests, workspace files, lockfiles, runtime configuration, and tooling configuration.
4. Inspect the smallest relevant parts of those files to establish project identity, repository shape, languages, runtime, package manager, frameworks, stack, and validation entrypoints.
5. Inventory potentially relevant documentation by path and title. Read only sections needed to establish architectural facts or assess documentation status.
6. Identify major modules, entrypoints, persistence boundaries, auth/authz boundaries, external boundaries, and deployment shape only when material to the repository.
7. List unresolved material questions. Do not pursue details that would not change future navigation or a durable global conclusion.
8. Inspect source, tests, schemas, or deeper configuration only for those unresolved questions.
9. For each conclusion, retain a repository-relative evidence pointer. Prefer current executable/configuration evidence over prose when they conflict.
10. Stop exploring each subject as soon as sufficient high-confidence evidence can populate a compact context.

Incomplete but correct is better than complete but invented. Omit optional trivia. Use `UNKNOWN` only for a material field whose absence should remain visible.

## Documentation conflicts

When documentation is useful, classify its overall or per-document status as `current`, `mixed`, `historical`, or `conflicting`. A `docs/` directory is not automatically authoritative.

If prose conflicts with current implementation or configuration:

- do not repair the documentation during INIT;
- record the conflict compactly when it affects navigation or interpretation;
- derive the generated context from the strongest current applicable evidence;
- ask the user only if the ambiguity materially prevents a useful INIT.

## Validation discovery

Discover validation commands statically from real repository declarations such as package scripts, task runners, CI configuration, or documented developer commands. Do not execute them.

Include a command only when its primary purpose is validation. Exclude commands primarily intended to mutate production, databases, migrations, releases, or deployments. Prefer a non-mutating validation variant when the repository provides one. Record possible file, generated-output, and external-state effects rather than assuming commands are pure.

## Freshness and dirty inputs

Use `git-path-diff`; do not compute repository-wide, configuration, or per-file hashes.

Separate:

- `structural_sources`: exact manifests, configuration, schemas, entrypoints, or canonical documents whose content changes could make persisted knowledge stale;
- `topology_watch`: directories where additions, deletions, renames, or moves matter, while ordinary internal edits do not by themselves imply architectural staleness.

A relevant change means `possibly stale`, not `regenerate everything`. Do not implement reconciliation or sync.

After selecting the evidence used for generated context, compare those relevant inputs with HEAD. If any is modified, deleted, renamed, or untracked relative to HEAD, set `reproducible: false` and record only its repository-relative path and Git status as a non-reproducible input. Otherwise, when HEAD resolves, set `reproducible: true`. Do not fingerprint dirty content.

## Generate or preview

Prepare exactly the five files defined in [project-context.md](project-context.md). Check their contents for internal consistency before writing.

For `$yollox init`:

1. Complete discovery before creating `.yollox/`.
2. Recheck that `.yollox/` does not exist.
3. Create only `.yollox/` and its five required files. Do not write temporary artifacts outside it.
4. Report a compact summary of generated context, visible unknowns/conflicts, and reproducibility.

For `$yollox init --dry-run`:

- perform the same discovery and context construction in memory;
- do not create directories, files, caches, reports, or temporary repository artifacts;
- preview the planned five-file tree and compact summaries/key records for each file;
- call out `UNKNOWN` values, documentation conflicts, material ambiguities, and reproducibility;
- do not print large inventories or repository dumps.

Before finishing, verify that no path outside `.yollox/**` was intentionally changed and that no validation or prohibited command was executed.
