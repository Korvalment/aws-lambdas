import boto3
import json
import base64
from urllib.parse import unquote


def lambda_handler(event, context):
    user_pool_id = event['key1'] #getting user pool id
    email  = event['key2'] #the user name is the email


 
    client = boto3.client('cognito-idp')

   # Get a list of all users in the given User Pool
    response = client.list_users(
        UserPoolId=user_pool_id,
        AttributesToGet=['email']
    )
    
    
   # Check if a user with the given email exists
    for user in response['Users']:
        if user['Attributes'][0]['Value'] == email:
            return {
                'statusCode': 200,
                'body': 'A user with this email already exists in the User Pool'
            }

    # If the user with the specified email does not exist, return a message about this
    return {
        'statusCode': 404,
        'body': 'The user with this email was not found in the User Pool'
    }
