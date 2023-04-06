import boto3
import json

cognito = boto3.client('cognito-idp')

def lambda_handler(event, context):
    amplify_user_pool_id = event['key1']
    managed_user_pool_id = event['key2']
    group_name = "TechUser_"+managed_user_pool_id
    description = "Technical user with permitions to manage integration"
    precedence = 1
    #role_arn = event['key3']
    
    response = cognito.create_group(
        GroupName=group_name,
        UserPoolId=amplify_user_pool_id,
        Description=description,
        #RoleArn=reole_arn
        Precedence=precedence
    )


    #response = json.loads(json.dumps(response, default=str))
    return response["Group"]["GroupName"]