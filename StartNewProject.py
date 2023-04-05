# StartNewProject is the main fuction

# This lambda will:
#  1) Create new Cognito User Pool with 2 clients:
#       1a) Create User Pool
#       1b) Create SSO integration
#       1c) Create SSO integration example
#  2) Create new IAM policy for that Cognito Pool to integrate (SAML) SSO (integration management)
#  3) Create user in (!!!)Amplify User Pool(!!!)
#  4) Attach policy to user
#  5) Save: user_id, coognito_pool_id, clients_id to DynamoDB

# This will be implemented by:
#  function CreateUserPool(user_pool_name) that returns [user_pool_id, user_pool_arn]
#  function CreateClient(user_pool_id, client_name) that will return client_id
#  function CreatePolicy(user_pool_arn, policy_name) that returns policy_arn
#  function CreteUser(amplify_pool_id, user_mail) that returns user_id
#  function AttachPolicy(user_id, policy_arn)
#  [user_pool_id, cient1_id, client2_id, user_id] >> DynamoDB

import boto3
import json


def CreateUserPool(user_pool_name):
    policies = {
    "PasswordPolicy": { # pass pol is weak for testing reason
            "MinimumLength": 6,
            "RequireLowercase": False,
            "RequireNumbers": False,
            "RequireSymbols": False,
            "RequireUppercase": False
        }
    }
    username_attributes = ["email"]
    
    # Create a Cognito User Pool
    cognito_idp = boto3.client("cognito-idp")
    response = cognito_idp.create_user_pool(
        PoolName=user_pool_name,
        Policies=policies,
        UsernameAttributes=username_attributes
    )

   # Convert datetime objects to strings
    response = json.loads(json.dumps(response, default=str))
    user_pool_id = response["UserPool"]["Id"]
    #user_pool_arn = respone[   ][   ]
  
    return {
        "id": user_pool_id, 
        "arn": user_pool_arn
        }
  
def CreateClient(user_pool_id, client_name):
    pass
    #return client_id

def CreateUser(amplify_pool_id, user_mail):
    cognito = boto3.client("cognito-idp")
    response = cognito.admin_create_user(
        UserPoolId=amplify_pool_id,
        Username=user_mail,
        UserAttributes=[
            {
                "Name": "email",
                "Value": user_mail #the user name is the email
            },
            {
                "Name": "phone_number_verified",
                "Value": "false" #no phone number verification
            }
        ],
        DesiredDeliveryMediums=[
            'EMAIL',
        ]
    )
    # Convert datetime objects to strings
    response = json.loads(json.dumps(response, default=str))
    return response
    #retur user_id !!!

def CreatePolicy(cognit_pool_arn, policy_name):
    client = boto3.client('iam')
    cognit_pool_arn = "\"" + cognit_pool_arn + "\""
    policy_document = '''{
    "Version": "2012-10-17",
    "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": [
                    "cognito-idp:DeleteIdentityProvider",
                    "cognito-idp:UpdateIdentityProvider",
                    "cognito-idp:CreateIdentityProvider"
                ],
                "Resource": ''' + cognit_pool_arn + '''
            }
        ]   
    }'''
    response = client.create_policy(
    PolicyName=policy_name,
    PolicyDocument = policy_document
    )
    response = json.loads(json.dumps(response, default=str))
    return response
    #return arn
    
def AttachPolicy(user_id, policy_arn):
    pass
    #return raport
    
def lambda_handler(event, context):
    #event['key1'] is new UserPool name
    new_user_pool_name = event['key1']
    #event['key2'] is TechUser email
    tech_user_mail = event['key2']

    amplify_pool_id = 'XYZ' #copy-paste your amplify userpool id from AWS
    new_user_pool = CreateUserPool(new_user_pool_name)
    
    client1_id = CreateClient(new_user_pool['id'], 'client1')
    client2_id = CreateClient(new_user_pool['id'], 'client2')
    
    policy_arn = CreatePolicy(new_user_pool["arn"], new_user_pool_name+"_IntegrationManagement_policy")
    tech_user_id = CreateUser(amplify_pool_id, tech_user_mail)
    AttachPolicy(tech_user_id, policy_arn)

    return {
        "user pool id": new_user_pool['id'], 
        "client1 id": client1_id, # ADD THIS
        "client2 id": client2_id, 
        "techuser id": tech_user_id
        }
