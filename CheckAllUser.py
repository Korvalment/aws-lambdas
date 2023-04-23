import json
import boto3

def lambda_handler(event, context):
    user_pool_id = 'eu-central-1_qIrMsVE3U'
    cognito_client = boto3.client('cognito-idp')
    users = cognito_client.list_users(UserPoolId=user_pool_id)['Users']
    user_list = []
    for user in users:
        user_obj = {
            'userID': user['Username'],
            'email': next((attr['Value'] for attr in user['Attributes'] if attr['Name'] == 'email'), ''),
        }
        user_list.append(user_obj)
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(user_list)
    }

