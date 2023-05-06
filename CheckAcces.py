import json
import boto3

def lambda_handler(event, context):
    # Obtaining the authorization token from the request headers
    auth_token = event['headers']['Authorization']
    
    # Getting the ARN of the API Gateway resource
    resource_arn = event['methodArn']
    
    # Obtaining the user ID from the authorization token
    cognito = boto3.client('cognito-idp')
    jwt = auth_token.split(' ')[1]
    jwt_decoded = cognito.decode_auth_token(AccessToken=jwt)
    user_id = jwt_decoded['sub']
    
    # Check if the user belongs to the techUser group
    user_groups = cognito.admin_list_groups_for_user(UserPoolId='USER_POOL_ID', Username=user_id)
    authorized = False
    for group in user_groups['Groups']:
        if group['GroupName'] == 'techUser':
            authorized = True
    
    # Check if the user has access to the requested resource
    if authorized:
        # Create permission to execute a request to the API Gateway resource
        policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": "Allow",
                    "Resource": resource_arn
                }
            ]
        }
        return {
            "principalId": user_id,
            "policyDocument": policy
        }
    else:
        # Create a denial of access to the requested API Gateway resource
        policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": "Deny",
                    "Resource": resource_arn
                }
            ]
        }
        return {
            "principalId": user_id,
            "policyDocument": policy
        }
