import boto3
import json

def lambda_handler(event, context):
    # Set the Cognito User Pool settings
    user_pool_id = event['key1'] #getting user pool id
    user_name = event['key2'] #the user name is the email

    cognito = boto3.client("cognito-idp")
    response = cognito.admin_create_user(
        UserPoolId=user_pool_id,
        Username=user_name,
        UserAttributes=[
            {
                "Name": "email",
                "Value": user_name #the user name is the email
            },
            {
                "Name": "phone_number_verified",
                "Value": "false"
            }
        ],
        DesiredDeliveryMediums=[
            'EMAIL',
        ]
    )



    # Convert datetime objects to strings
    #response = json.loads(json.dumps(response, default=str))
    
    #return response 
    
     return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({"UserID": response["User"]["Username"]})
    }
