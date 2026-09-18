# DEPLOY workflow

Use for `$yollox deploy: <objective>` with [execution.md](execution.md).

## Resolve intent, candidate, and destination

DEPLOY has two internal intents, inferred from the user's request without mandatory flags:

- **PREPARE:** configure or improve the requested deployment path.
- **EXECUTE:** publish a concrete release through that path.

Never convert PREPARE into EXECUTE automatically. An explicit combined preparation-and-deployment request can authorize both. Resolve ambiguity before dependent mutations; do useful independent preparation while a material answer is missing.

Establish the component, candidate identity, target environment and concrete account/project/cluster/region where relevant, native deployment mechanism, and observable success condition. A candidate may be a commit, existing artifact or requested worktree content. Use native commit IDs, artifact versions/digests and deployment IDs rather than inventing a release manifest or Yollox state.

Prefer explicit user intent and current repository deployment configuration, scripts, CI/CD and canonical operational instructions. Do not infer provider from framework, assume production, or treat an active CLI context as proof of the intended destination. Project Context helps locate this evidence; Git freshness cannot establish live release, credential, account or database state.

Inspect only the necessary build/output, environment, deployment and recovery contracts. Inspect migrations when the release changes persistent data/schema, depends on a migration, or invokes migrations through its deployment path. Do not add provider, container, IaC, CI, GitOps or observability machinery unless the actual task requires it.

## PREPARE

Modify the smallest coherent set of scripts, configuration, packaging, pipelines or documentation needed for the requested path. Extend existing architecture; do not build a parallel mechanism or change provider for convenience. Derive runtime, ports, regions, outputs, variables and checks from repository evidence or explicit decisions.

No routine `.env.example`, Dockerfile, infrastructure template or generic service variables. Add these only when necessary. Preserve secret-store architecture and existing configured values; never commit real secrets or replace working secrets with placeholders. Inspect variable names and sources without dumping expanded credentials. Do not rotate credentials unless explicitly authorized.

Validate configuration, affected behavior or packaging proportionally. A command called `plan`, `validate` or `dry-run` is not automatically local or effect-free; inspect its actual effects under the shared policy. PREPARE does not implicitly authorize creating remote resources.

PREPARE is complete when the requested configuration is coherent and complete, relevant validation is performed to the stated extent, and any real external prerequisite is identified. Configuration readiness does not imply a release was deployed or that remote prerequisites are already satisfied.

## EXECUTE preconditions

Before publishing, establish:

- The destination and requested operation are unambiguous and authorized, with available credentials and verified relevant tool context.
- The candidate is the requested version, and the mechanism will actually publish it. Verify packaging inputs and output scope; do not accidentally include unrelated worktree changes, ignored content or secrets.
- Applicable artifact/configuration and release-gate checks passed for that candidate. Later relevant edits invalidate earlier results where affected. Do not silently bypass a required gate because its failure is pre-existing.
- Material data, compatibility, availability and infrastructure effects are understood and covered by authorization. No known material blocker, including secret exposure in the release, is being published.
- Recovery is understood to the extent required by the release risk, especially for production, stateful workloads and infrastructure.

When the native pipeline builds and validates the artifact as part of execution, verify that its required gates precede publication and follow their actual results. Do not require a duplicate local pipeline or bypass those gates; preserve the link between the requested source, validated artifact and published release.

Do not silently modify source to deploy a different version when a specific commit or artifact was requested. Application defects independent of deployment are not implicit FIX work. In an explicitly combined preparation-and-deployment request, perform the authorized local changes, establish the resulting candidate, and validate it before publication.

An unambiguous request to deploy a particular version to a resolved destination does not require a redundant final confirmation. If specific authorization is missing, complete all authorized independent preparation first, then describe the exact remaining operation, destination and material effects when asking. Do not infer production intent or data-risk acceptance from the word `deploy` alone.

Deployment does not grant Git permission. A push-triggered pipeline does not authorize commit/push automatically; an explicitly authorized Git operation should not be re-confirmed by routine. Do not replace the established path merely to avoid an unresolved prerequisite, rebuild an existing pipeline unnecessarily, or install global provider tooling by default.

## Data and recovery boundaries

For relevant migrations, establish what runs, ordering, old/new-version compatibility, data/availability consequences and supported recovery. Creating or finding a migration is not authorization to apply it. A generic deployment instruction does not resolve a destructive, irreversible or otherwise material data-risk decision hidden in a script. Resolve that decision before executing it.

Do not assume transactional migrations, reversible schema changes, or safe database rollback. Derive guarantees and recovery from the actual database/framework/platform and repository procedures. Do not invent rollback SQL, backups or infrastructure to satisfy a generic checklist.

## Execute and verify

Use the repository/provider-native deployment mechanism for the resolved candidate and destination. Run only scoped packaging, publication, rollout or infrastructure operations covered by the task. Account for material effects of invoked scripts and pipelines, not merely the top-level command name.

After execution, verify observable state through the real provider/pipeline status, release identity, rollout, readiness or focused project-defined smoke mechanism. A job accepted, upload completed or CLI exit code zero is not by itself proof the release is available and functional. Do not invent health endpoints or broad smoke suites; use the smallest meaningful verification with permitted effects.

Follow an asynchronous operation through its native status when practical. If it remains pending or inaccessible, report that state and the known identifier; do not call it a completed deployment. No persistent polling machinery or background Yollox monitoring is required.

## Failure handling

- Before publication, correct failures caused by your own in-scope preparation and rerun affected checks. Do not repair unrelated application failures or bypass required release gates automatically.
- If a remote action fails or times out, determine actual remote state before retrying. Retry only when new evidence establishes that it is safe and useful; stop blind retries or further rollout when state is uncertain.
- Do not automatically roll back through an additional remote mutation unless explicitly authorized. Native atomic/automatic recovery already included in the authorized mechanism may run as part of it.
- If additional recovery is not authorized, inspect the failure and report concrete status plus the supported recovery direction. Never use destructive Git operations as deployment rollback.
- Successful recovery means service was recovered, not that the requested new release succeeded. Report partial rollout, reverted releases, failed verification and unknown state explicitly.

## Completion and output

For PREPARE, report configuration prepared, changed files, actual validation and external prerequisites.

For EXECUTE, report component, candidate identity, destination, actual deployment outcome and post-deploy verification, plus only material blockers or recovery concerns. Claim success only when the requested release was actually applied and the relevant observable verification supports that conclusion. If applied but unverified, pending, failed, partially rolled out or recovered to the old release, say so accurately.

Account for expected data/infrastructure effects and any unexpected effect; never conceal incomplete rollout or missing required verification. Do not print secrets, persist deployment history in `.yollox/`, refresh context, or invoke another mode automatically.
