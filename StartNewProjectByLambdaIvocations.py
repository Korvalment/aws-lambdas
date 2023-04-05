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

# key 1 = name of Cognito UserPool
# key 2 = admin's email adres for new UserPool

def lambda_handler(event, context):
    lambda_client = boto3.client('lambda')
    #enter your lambdas' ARNs !!!
    user_pool_name = event['key1']
    user_mail = event['key2']
    
    #enter your ID's and ARN's
    amplify_user_pool_id = "xxxxxx"
    arn_dict = {
    "create_user_pool_arn": "xxxxxx"
    "create_client_arn": "xxxxxx"
    "create_policy_arn": "xxxxxx"
    "create_user_arn": "xxxxxx"
    "attach_policy_arn": "xxxxxx"
    }
    
    invocation_type = "RequestResponse"
    
    new_user_pool = RunLambda(arn_dict["create_user_pool_arn"], invocation_type,user_pool_name )
    client1_id = RunLambda(arn_dict["create_client_arn"], invocation_type, new_user_pool["id"], "client1")
    client2_id = RunLambda(arn_dict["create_client_arn"], invocation_type, new_user_pool["id"], "client2")
    policy_arn = RunLambda(arn_dict["create_policy_arn"], invocation_type, new_user_pool["arn"], user_pool_name+"_IntegrationManagement_policy")
    user_id = RunLambda(arn_dict["create_user_arn"], invocation_type, amplify_user_pool_id, user_mail)
    RunLambda(arn_dict["attach_policy_arn"], invocation_type, user_id, policy_arn)
    
    #save resoults to DynamoDB
    
def RunLambda(lambda_name, invo_type, key1=" ", key2=" "):
    client = boto3.client('lambda')

    payload = {
        "key1": key1,
        "key2": key2
    }
    
    response = client.invoke(
        FunctionName=lambda_name,
        InvocationType=invo_type,
        Payload=json.dumps(payload)
    )

    # Obsługa odpowiedzi z innej funkcji Lambda
    response_payload = json.loads(response['Payload'].read().decode())
    return response_payload
