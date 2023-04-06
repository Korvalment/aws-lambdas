import boto3
import json

def lambda_handler(event, context):
    
    client = boto3.client('iam')
    
    cognit_pool_arn = "\"" + event['key1'] + "\""
    tech_grup_name = event['key2']
    role_name = tech_grup_name + "_role"
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
            "Resource": '''+cognit_pool_arn+'''
        }
    ]
}'''
    #error:
    #"errorMessage": "An error occurred (MalformedPolicyDocument) when calling the CreateRole operation: Has prohibited field Resource",
    # needs fix
    
    response = client.create_role(
        RoleName='string',
        AssumeRolePolicyDocument=policy_document
    )

    #response = json.loads(json.dumps(response, default=str))
    return response["Role"]["Arn"]
