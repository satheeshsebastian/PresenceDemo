"""
name: create_action_plan
description: Create fictional follow-up tasks for a confirmed issue plan.
is_enabled: true
escalates_to_human: false
input_schema:
  additionalProperties: false
  properties:
    case_id: {type: string}
    issue_summary: {type: string}
  required: [case_id, issue_summary]
  type: object
output_schema:
  type: object
  additionalProperties: false
  properties:
    plan_id: {type: string}
    tasks: {type: array}
  required: [plan_id, tasks]
playground_input: '{"case_id":"CASE-1004","issue_summary":"Order processing delay"}'
"""
from pydantic import BaseModel, ConfigDict
class ActionInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    case_id: str
    issue_summary: str
class ActionOutput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    plan_id: str
    tasks: list[dict]
def handler(inputs: ActionInput) -> ActionOutput:
    return ActionOutput(plan_id="PLAN-3001",tasks=[{"title":"Validate order queue health","owner":"Operations","status":"Not started"},{"title":"Confirm test order recovery","owner":"Account team","status":"Not started"},{"title":"Publish resolution summary","owner":"Service manager","status":"Not started"}])
