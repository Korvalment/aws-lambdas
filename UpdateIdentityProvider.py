import json
import boto3

def lambda_handler(event, context):
    
    user_pool_id = 'eu-central-1_k1w0SQpMa'
    provider_name = 'PROVIDER'
    
    client = boto3.client('cognito-idp')
    
    list_response = client.list_identity_providers(
    UserPoolId=user_pool_id
    )
    
    if list_response['Providers'] == []:
        #create
        create_response = client.create_identity_provider(
            UserPoolId=user_pool_id,                # REQUESTED
            ProviderName=provider_name,             # REQUESTED
            ProviderType='SAML',                    # REQUESTED
            ProviderDetails={                       # REQUESTED: MetadataFile OR MetadataURL, 
                'MetadataFile': 'string',           # IDPSignout OPTIONAL
                'MetadataURL': 'string',
                'IDPSignout': 'string'
            },
            AttributeMapping={
                'string': 'string'
            },
            IdpIdentifiers=[
                'string',
            ]
        )

    else:
        #update
        response = client.update_identity_provider(
            UserPoolId=user_pool_id,                # REQUESTED
            ProviderName=provider_name,             # REQUESTED 
            ProviderDetails={
                'MetadataURL': 'string',
                'MetadataFile': 'string'
            },
            AttributeMapping={
                'string': 'string'
            },
            IdpIdentifiers=[
                'string',
            ]
        )
        
    
    return {
        'statusCode': 200
    }
