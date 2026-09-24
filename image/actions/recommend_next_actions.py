"""
name: recommend_next_actions
description: Generate fictional next actions for a business issue.
is_enabled: true
escalates_to_human: false
input_schema:
  additionalProperties: false
  properties:
    severity: {type: string, enum: [low, medium, high]}
    issue_summary: {type: string}
  required: [severity, issue_summary]
  type: object
output_schema:
  type: object
  additionalProperties: false
  properties:
    actions: {type: array}
  required: [actions]
playground_input: '{"severity":"high","issue_summary":"Orders are delayed for a strategic account"}'
"""
from pydantic import BaseModel, ConfigDict
class ActionInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    severity: str
    issue_summary: str
class ActionOutput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    actions: list[dict]
def handler(inputs: ActionInput) -> ActionOutput:
    actions=[{"title":"Validate queue and downstream API health","owner":"Operations","due":"Today","approval_required":False},{"title":"Notify account and service owners","owner":"Account team","due":"Within 30 minutes","approval_required":True}]
    if inputs.severity == "high": actions.insert(0,{"title":"Escalate to incident lead","owner":"Service manager","due":"Immediately","approval_required":True})
    return ActionOutput(actions=actions)
