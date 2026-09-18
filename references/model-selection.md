# Advisory model and reasoning selection

Apply across the intent entry and explicit modes when a material configuration recommendation is warranted or the user requests this advice. Select sufficient capability for the remaining work at proportionate total cost. This is a shared decision policy, not a new mode, mandatory phase or runtime router. Preserve the active mode's scope, effects, evidence and completion requirements, including INIT's static discovery and read-only boundaries where applicable.

## Recommendation versus effective configuration

The current model already performs this assessment. A recommendation can benefit subsequent work; it cannot retroactively select the model that processed the initial request.

Distinguish the configuration requested by the user, the configuration known to be effective, and the recommended configuration. Use reliable session/client information when available; a default in a configuration file does not establish the active model or effort. If effective settings or available alternatives are unknown, state that only when material to the advice. Do not infer them from response style, apparent difficulty or a model's self-description, or demand configuration details for every task.

This policy only recommends. Do not switch models or effort, edit configuration, manipulate the client or session, start a nested Codex process, call another model, or spawn an agent to apply or simulate a change. Telling a model to think more carefully does not establish that its configured reasoning effort changed. An exposed control or user acceptance of advice is not evidence that the change actually took effect; never claim it did without reliable confirmation.

## Separate model from reasoning effort

- **Model:** consider suitability and demonstrated reliability for the work, necessary tools and input modalities, relevant context handling, availability, latency and cost within the user's constraints.
- **Reasoning effort:** consider the deliberation needed to resolve the pending decisions with that model. Verify supported levels for a concrete recommendation; labels and defaults are model-dependent.

Consider an effort adjustment on the current model when it appears suitable but the work needs deeper analysis. Consider another model when a relevant capability or reliability mismatch makes it a better candidate. Assess that model's effort separately. More reasoning does not establish equivalence to another model or guarantee correctness; a more capable model does not automatically require maximum effort.

Do not require a ladder through every cheaper model or effort level before recommending a clearly justified alternative. Equally, do not treat the most expensive configuration as the default answer to uncertainty.

## Use evidence already needed for the task

Evaluate a coherent portion of remaining work, such as resolving a contract, diagnosing a cause, implementing an established solution or verifying a transition. Do not select a configuration per command, file or capability name.

Relevant signals are the clarity of the intended result and contracts; interacting invariants and consumers; technical uncertainty or competing causal explanations; consequences and reversibility of error; strength of available validation; observed contradictions or failed approaches; and how much substantive work remains. A small authorization change can require more analysis than a large mechanical edit. File count, prompt length, repository size, elapsed time and mode name are insufficient selection rules.

Higher risk increases the evidence and control needed. It does not automatically require maximum effort, and a stronger model cannot replace missing evidence, authorization or verification. Express difficulty through concrete unresolved contracts or hypotheses, not unsupported confidence scores or declarations that the current model is incapable.

Project Context may help locate relevant boundaries and checks under the existing compatibility and freshness rules. It is optional and does not prove task difficulty. Do not initialize, refresh or audit it to classify work. Use `validation.yaml` for applicable candidate checks under the active mode's policy, not to benchmark models or infer that higher reasoning removes a validation requirement.

## Reassess when the understanding changes

Treat the initial assessment as provisional. Reconsider after enough normal discovery when scope or dependencies differ materially from the initial understanding, or later when evidence reveals a difficult contradiction, a reasoning obstacle or a substantial simplification. Do not reassess after every tool call or merely because another capability is selected.

Before escalating, identify the actual missing prerequisite:

| Observed obstacle | Appropriate response |
|---|---|
| Missing product intent or an unresolved user tradeoff | Ask the specific material question. |
| Relevant evidence not yet inspected | Perform bounded discovery or permitted validation. |
| Missing credentials, permissions, services or tooling | Resolve the authorized prerequisite or report the concrete limitation. |
| Relevant facts obscured by unrelated context | Improve evidence selection without silently narrowing the requested scope. |
| Available evidence requires difficult causal or cross-contract reasoning | Consider more effort or a more suitable model for that analysis. |

Escalation can be justified before failure when the evidence already shows the mismatch. Otherwise, use what attempts demonstrated: for example, an explanation refuted by another consumer's invariant or a proposed correction that still violates an inspected contract. A failed command, environment problem or arbitrary number of retries is not a model-quality diagnosis. Do not manufacture attempts to justify escalation or retry the same hypothesis blindly after changing configuration.

Recommend a less costly configuration when evidence shows the remaining work is settled, bounded and sufficiently verifiable, and the expected benefit exceeds switching and context-reconstruction overhead. Do not interrupt a nearly completed task for hypothetical savings. Avoid oscillation; repeating or reversing a recommendation requires new material evidence or a changed user preference.

## Respect constraints and total cost

Honor fixed model/effort choices, allowed alternatives, spending limits and latency priorities already supplied. Selecting a model before invocation is not by itself a prohibition on advice, but does not authorize changing it either. Ask about an unknown constraint only when it materially affects a useful recommendation; do not introduce an initial preferences questionnaire.

Consider total completion cost, including validation, rework, latency, switching overhead and user intervention. Do not always start with the cheapest model, prescribe maximum effort by mode, or reduce target coverage, checks or completion criteria to fit a cheaper configuration. If the user retains a choice, continue within it where correctness can be established; disclose concrete limitations rather than silently exceeding a limit or presenting incomplete work as complete.

Recommend an exact model and effort only when current, reliable client/catalog information or official documentation supports that combination. Separate documented support from actual account availability. If availability or effective settings are unknown, qualify the advice rather than inventing names, prices, supported levels or an asserted mismatch with the current configuration. Consult current official documentation only when necessary for the concrete advice; do not conduct model research for every task or maintain a private catalog. Price per API token alone does not establish the user's actual cost or quota consumption. Savings claims require measurements of comparable completed work.

## Communicate and continue

When no material adjustment is warranted, continue without a routine model-selection report, unless the user requested advice. When advice is requested or an adjustment is warranted, give one concise recommendation: the observed reason, the proposed model/effort change or retention, the portion of remaining work it serves, and any material tradeoff or availability uncertainty. Do not ask the user to choose from an unexplained menu or expose private reasoning traces.

If applying the recommendation requires a user action, identify the known native client control when useful without pretending to operate it or promising when it takes effect. Continue independent authorized work. Pause dependent work only for an actual unresolved requirement, capability or evidence limitation, not solely because a recommendation is pending or a preferred model is unavailable.

If the user changes configuration, reuse the conversation's objective, restrictions, relevant evidence and pending question. Preserve version attribution and recheck assumptions affected by intervening changes; do not restart discovery by routine. Keep recommended, user-reported and reliably confirmed effective settings distinct when describing the result.

Keep advice and continuation information in the conversation. Do not persist model preferences, difficulty labels, prices, recommendations or escalation history in `.yollox/`, or create handoff files, task state, approval registries, session controllers or routing infrastructure. Existing mode deliverables remain sufficient. Model choice never replaces their evidence or authorizes additional effects.
