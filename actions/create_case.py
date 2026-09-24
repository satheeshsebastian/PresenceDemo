"""
name: create_case
description: Create a fictional Salesforce case after user confirmation.
is_enabled: true
escalates_to_human: false
input_schema:
  additionalProperties: false
  properties:
    account_name: {type: string}
    subject: {type: string}
    description: {type: string}
    severity: {type: string, enum: [low, medium, high]}
  required: [account_name, subject, description, severity]
  type: object
output_schema:
  type: object
  additionalProperties: false
  properties:
    case_id: {type: string}
    status: {type: string}
  required: [case_id, status]
  type: object
playground_input: '{"account_name":"Northwind Traders","subject":"Order processing delay","description":"Orders are delayed for the account.","severity":"high"}'
"""
from pydantic import BaseModel, ConfigDict
class ActionInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    account_name: str
    subject: str
    description: str
    severity: str
class ActionOutput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    case_id: str
    status: str
def handler(inputs: ActionInput) -> ActionOutput:
    return ActionOutput(case_id="CASE-1004", status="created")
