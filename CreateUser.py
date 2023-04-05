import boto3
import json

def lambda_handler(event, context):
    user_pool_id = event['key1'] #getting user pool id
    user_mail = event['key2']

    cognito = boto3.client("cognito-idp")
    response = cognito.admin_create_user(
        UserPoolId=user_pool_id,
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
   # response = json.loads(json.dumps(response, default=str))

    return response["User"]["Username"]
