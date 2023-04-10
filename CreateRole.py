import boto3
import json

def lambda_handler(event, context):
    
    client = boto3.client('iam')
    
    cognit_pool_arn = event['key1']
    new_pool_id = event['key2']
    role_name = "TechUser_" + new_pool_id + "_role"
    policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cognito-idp:DeleteIdentityProvider",
                "cognito-idp:UpdateIdentityProvider",
                "cognito-idp:CreateIdentityProvider"
            ],
            "Resource": cognit_pool_arn
        }
    ]
}
   #"errorMessage": "An error occurred (MalformedPolicyDocument) when calling the CreateRole operation: Has prohibited field Resource"
    
    response = client.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(policy_document)
    )

    #response = json.loads(json.dumps(response, default=str))
    return response["Role"]["Arn"]