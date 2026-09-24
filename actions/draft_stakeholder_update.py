"""
name: draft_stakeholder_update
description: Draft an approval-gated internal issue update.
is_enabled: true
escalates_to_human: false
input_schema:
  additionalProperties: false
  properties:
    account_name: {type: string}
    issue_summary: {type: string}
    severity: {type: string}
    next_step: {type: string}
  required: [account_name, issue_summary, severity, next_step]
  type: object
output_schema:
  type: object
  additionalProperties: false
  properties:
    draft: {type: string}
  required: [draft]
playground_input: '{"account_name":"Northwind Traders","issue_summary":"Order processing is delayed","severity":"high","next_step":"Validate queue health and escalate to the incident lead"}'
"""
from pydantic import BaseModel, ConfigDict
class ActionInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    account_name: str
    issue_summary: str
    severity: str
    next_step: str
class ActionOutput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    draft: str
def handler(inputs: ActionInput) -> ActionOutput:
    return ActionOutput(draft=f"Issue update - {inputs.account_name}\n\nWe are investigating: {inputs.issue_summary}. Severity is {inputs.severity}. Next step: {inputs.next_step}. This update is a draft and requires owner approval.")
