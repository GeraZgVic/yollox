# BUILD workflow

Use for `$yollox build: <objective>` with [execution.md](execution.md).

## Responsibility and discovery

Implement the requested capability or behavior change completely within the smallest coherent repository scope. BUILD means implementing behavior; running a compilation command does not by itself constitute this workflow.

Before editing, establish the behavior and acceptance criteria, existing reusable implementation, affected contracts/consumers, and how the requested result will be validated. Resolve routine decisions from current repository evidence; ask only for material unresolved product, compatibility, data or technical choices.

Project Context describes known architecture, not an immutable design. The user may authorize changing it. Confirm the relevant implementation and constraints before following a context convention or deciding a new abstraction is necessary.

## Implementation boundary

- Implement all required layers and consumers for the requested behavior, without adjacent features, speculative layers or broad redesign. Order multi-part work by real dependencies; no mandatory planning artifact is required.
- Reuse compatible existing helpers, components, services, schemas and patterns. Do not impose a generic framework recipe, state library, abstraction rule or file-size limit.
- Preserve unrelated behavior. When the task requires changing a contract, propagate it coherently to affected consumers and validate compatibility within the authorized scope. Do not silently normalize inputs, broaden behavior or introduce breaking changes not required by the request.
- Include source, configuration, documentation, schemas and migration files when necessary for the capability. Writing a migration does not authorize running it on shared or production data. Implementing an integration does not authorize provisioning an external account or publishing the product.
- Add a dependency only when the repository lacks a suitable existing capability and the requested behavior requires it. Use native package/version conventions and avoid unrelated upgrades or tooling replacement.
- Preserve and verify concrete security contracts when the feature touches trust boundaries, permissions, sensitive data or dangerous sinks. Do not add generic security infrastructure by routine.

Do not leave required consumers, error paths or configuration incoherent merely to reduce the diff. Conversely, a possible future consumer is not a reason to build an unrequested abstraction now.

## Validation and completion

Use existing targeted tests where suitable; add focused coverage when needed to demonstrate new or changed behavior, then relevant module checks. Do not inflate coverage with redundant tests or rewrite expectations to conceal regressions. Follow applicable validation requirements and the shared effect policy; broad builds or integration are conditional on the behavior and risk.

Complete when acceptance criteria are implemented, required dependencies and consumers are coherent, unrelated behavior is preserved, and validation evidence and limitations are accurate. Compilation alone is insufficient for behavior it does not exercise. Correct in-scope defects introduced during implementation without automatically invoking FIX.

Distinguish implemented from operational: a feature requiring a pending migration, configuration, feature-flag activation or external provisioning may be implemented but not yet available in that environment. If activation is part of the requested outcome, the task remains incomplete until it is performed or its concrete blocker is reported. Do not publish or mutate shared state implicitly to close that gap.

Report the substantive behavior, changed files, checks and results, and only material blockers or residual risks. Do not automatically launch REVIEW, CLEAN or DEPLOY.
