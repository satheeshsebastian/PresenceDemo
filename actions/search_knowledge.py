"""
name: search_knowledge
description: Search the fictional historical case and knowledge catalog.
is_enabled: true
escalates_to_human: false
input_schema:
  additionalProperties: false
  properties:
    query: {type: string}
  required: [query]
  type: object
output_schema:
  type: object
  additionalProperties: false
  properties:
    results: {type: array}
  required: [results]
  type: object
playground_input: '{"query":"order processing delay"}'
"""
from pydantic import BaseModel, ConfigDict
class ActionInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    query: str
class ActionOutput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    results: list[dict]
def handler(inputs: ActionInput) -> ActionOutput:
    return ActionOutput(results=[
        {"title":"Order processing delays - API queue saturation","source":"Historical case CASE-0921","relevance":0.94,"resolution":"Clear queued jobs, validate downstream API capacity, and monitor for 30 minutes."},
        {"title":"Order operations incident playbook","source":"Approved playbook","relevance":0.89,"resolution":"Notify the service owner, open an incident bridge, and confirm recovery with a test order."},
    ])
