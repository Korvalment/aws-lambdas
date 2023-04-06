import boto3
import json

def lambda_handler(event, context):
    amplify_user_pool_id = event['key1']
    user_name = event['key2'] 
    group_name = event['key3'] #'TechUser'

    cognito = boto3.client("cognito-idp")
    response = cognito.admin_add_user_to_group(
        UserPoolId=amplify_user_pool_id,
        Username=user_name,
        GroupName=group_name
)


   # Convert datetime objects to strings
    response = json.loads(json.dumps(response, default=str))

    return response