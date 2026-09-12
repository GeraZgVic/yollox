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

INIT is a project lifecycle operation, not an execution mode. Its only durable writable output is the required `.yollox/` context described in [project-context.md](project-context.md); one reserved temporary sibling staging directory is permitted solely for atomic publication.

## Preconditions and existing context

1. Resolve the repository root with Git and operate relative to that root. If the current location is not inside a Git worktree, stop without writing and report that INIT requires a Git repository.
2. Check for `.yollox/` before discovery.
   - Treat it as initialized only when it satisfies every compatibility check in [project-context.md](project-context.md): exactly the five required regular files, three conforming schema-version-1 YAML documents, and two non-empty Markdown documents.
   - If `.yollox/` exists but any compatibility check fails, stop without writing and report the concrete missing, extra, unreadable, unparsable, unsupported, or structurally invalid item.
   - Never overwrite, regenerate, repair, or delete an existing `.yollox/`. There is no `sync` in v0.1.
   - Reserved sibling staging directories named `.yollox.tmp-*` are temporary artifacts, never initialized context. A stale one does not block INIT and must not be reused as evidence or as the next staging directory.
3. Resolve HEAD, the current branch when one exists, and worktree status. A Git repository without a resolvable HEAD may still be inspected, but its baseline is `UNKNOWN`, the result is not reproducible, and Git-path-diff freshness is unavailable.

These checks are read-only in both normal and dry-run operation.

Use only read-only Git subcommands for discovery. Invoke every Git query that can take optional locks or refresh the index with `GIT_OPTIONAL_LOCKS=0` or the equivalent `git --no-optional-locks`. This requirement applies to both modes and is mandatory for the completely read-only dry-run; do not rely on a final intent check to excuse incidental `.git/index` or other Git metadata writes.

## Filesystem boundary

Resolve the Git root canonically. Before reading a repository-relative discovery path, canonicalize its existing target and confirm that it remains within that root. Do not follow absolute paths, `..` traversal, or symlinks whose resolved targets escape the root.

Apply the same containment check before recording a validation `working_directory`: it must be an existing directory whose canonical target remains inside the Git root. Persist normalized repository-relative paths without `..`. If critical evidence is available only through an escaping path, omit it or record the affected material conclusion as `UNKNOWN`; ask the user only when that prevents a useful INIT.

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
9. For each conclusion, retain a repository-relative evidence pointer and preserve the scope that evidence demonstrates. Prefer current executable/configuration evidence over prose when they conflict.
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

Use `git-path-diff` when HEAD resolves; do not compute repository-wide, configuration, or per-file hashes.

Separate:

- `evidence_sources`: exact files actually used to support persisted project, architecture, convention, or validation knowledge. Record every concrete file whose content change could invalidate that knowledge, whether it is source, test, configuration, schema, entrypoint, manifest, or documentation;
- `topology_watch`: directories where additions, deletions, renames, or moves matter, while ordinary internal edits do not by themselves imply architectural staleness.

Group `evidence_sources` compactly by artifact or knowledge category rather than recording provenance per field. Record exact files, not whole source directories by default. A normal content edit beneath `topology_watch` matters only when that file is also an evidence source; the watch itself detects structural additions, deletions, renames, and moves.

A relevant change means `possibly stale`, not `regenerate everything`. Do not implement reconciliation or sync.

After selecting the evidence used for generated context, compare the evidence sources and relevant topology changes with HEAD. If an evidence source is modified, deleted, renamed, or untracked, or if `topology_watch` contains a relevant structural change relative to HEAD, set `reproducible: false` and record only the repository-relative path and concise Git status as a non-reproducible input. Otherwise, when HEAD resolves, set `reproducible: true`. Ordinary internal edits under a watched directory do not count unless the edited file is an evidence source. Do not fingerprint dirty content.

When HEAD does not resolve, do not attempt this comparison and do not declare `git-path-diff`. Use the explicit unavailable freshness state from [project-context.md](project-context.md). A future maintenance capability may establish a baseline after one exists; INIT does not implement that capability.

## Generate or preview

Prepare exactly the five files defined in [project-context.md](project-context.md). Check their contents for internal consistency before writing.

For `$yollox init`:

1. Complete discovery and construct all five artifacts in memory before creating staging or `.yollox/`.
2. Recheck that `.yollox/` does not exist.
3. Create one uniquely named reserved staging directory matching `.yollox.tmp-*` as a sibling of `.yollox` in the Git root. Do not reuse a stale staging directory.
4. Write exactly the five required artifacts into staging and validate them completely against [project-context.md](project-context.md), including internal consistency.
5. Recheck that `.yollox/` does not exist, then publish with a same-filesystem atomic no-clobber rename or move from staging to `.yollox`. The publication operation must fail rather than replace any target that appeared concurrently. If the platform cannot guarantee no-clobber publication, stop without publishing.
6. On a handled failure before publication, make a best effort to remove only the staging directory created by this invocation; `.yollox/` must remain absent. An interruption may leave a reserved staging directory, but it is never context and does not block a later INIT using a different unique staging name.
7. Report a compact summary of generated context, visible unknowns/conflicts, and reproducibility.

The reserved staging directory is temporary and is the only write exception outside `.yollox/**`. Successful publication leaves exactly `.yollox/` with its five required files and no staging directory from that invocation. Do not add permanent artifacts or a recovery/sync mechanism.

For `$yollox init --dry-run`:

- perform the same discovery and context construction in memory;
- do not create staging, directories, files, caches, reports, or temporary repository artifacts;
- preview the planned five-file tree and compact summaries/key records for each file;
- call out `UNKNOWN` values, documentation conflicts, material ambiguities, and reproducibility;
- do not print large inventories or repository dumps.

Before finishing, verify that no path outside `.yollox/**` or the one permitted staging directory was changed, that dry-run changed no path at all, and that no validation or prohibited command was executed.
