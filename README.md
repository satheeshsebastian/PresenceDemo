# AI Digital Issue Manager

Hackathon Presence configuration and a browser-only Salesforce-style dummy CRM.

## Demo scope

The agent captures an account issue, assesses severity, searches fictional case and knowledge data, recommends next actions, drafts a stakeholder update, and creates a case/action plan after confirmation.

## Run the dummy CRM

Open `crm/index.html` directly in a browser, or serve this folder with any static file server. The app uses local browser state only and contains fictional data.

## Presence resources

- `config.yaml` defines Chat and Phone channels.
- `sops/` contains the root workflow and specialist procedures.
- `actions/` contains fictional CRM, knowledge, and planning actions.
- `guardrails/` contains high-risk and unsupported-claim controls.
- `scenarios/` contains the hackathon regression scenarios.
- `labels/` and `app/dashboard/` provide evaluation and demo metrics.

The action layer is deliberately mock-backed for the hackathon. Replace the action handlers with Salesforce and Azure AI Search connectors when moving beyond the demo.
