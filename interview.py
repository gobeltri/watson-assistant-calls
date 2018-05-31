from watson_developer_cloud import AssistantV1
import os
import json

WATSON_USERNAME = os.environ['WATSON_USERNAME']
WATSON_PASSWORD = os.environ['WATSON_PASSWORD']
INTERVIEW_WORKSPACE = '18f5f0dc-f7e5-4bea-bac1-c009c59e1649'

print("Connecting to Watson Assistant with username: ", WATSON_USERNAME, "...")

watson_assistant = AssistantV1(
    version = '2018-02-16',
    username = WATSON_USERNAME,
    password = WATSON_PASSWORD
)

response = watson_assistant.list_workspaces()
print("Listing all workspaces...")
print(json.dumps(response, indent=2))

response = watson_assistant.get_workspace(INTERVIEW_WORKSPACE)
print("Printing Interview Workspace details...")
print(json.dumps(response, indent=2))

response = watson_assistant.list_entities(INTERVIEW_WORKSPACE)
print("Listing entities on Interview Workspace...")
print(json.dumps(response, indent=2))


response = watson_assistant.create_entity(
    workspace_id = INTERVIEW_WORKSPACE,
    entity = 'beverage',
    values = [
        {'value': 'water'},
        {'value': 'orange juice'},
        {'value': 'soda'}
    ]
)

response = watson_assistant.list_entities(INTERVIEW_WORKSPACE)
print("Listing entities on Interview Workspace after adding a new entity...")
print(json.dumps(response, indent=2))


response = watson_assistant.delete_entity(
    workspace_id = INTERVIEW_WORKSPACE,
    entity = 'beverage'
)

response = watson_assistant.list_entities(INTERVIEW_WORKSPACE)
print("Listing entities on Interview Workspace after removing beverage entities...")
print(json.dumps(response, indent=2))

response = watson_assistant.list_dialog_nodes(
    workspace_id = INTERVIEW_WORKSPACE
)
print("Listing dialog nodes...")
print(json.dumps(response, indent=2))