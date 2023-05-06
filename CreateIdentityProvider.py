import boto3

def lambda_handler(event, context):
    client = boto3.client('cognito-idp')
    response = client.create_identity_provider(
        UserPoolId='eu-central-1_qIrMsVE3U',
        ProviderName='TestProvider',
        ProviderType='SAML',
        ProviderDetails={
            'MetadataFile': 'metadata.xml'
        },
        AttributeMapping={
            'email': 'email',
            'ATTRIBUTE_NAME': 'YOUR_PROVIDER_ATTRIBUTE'
        },
        IdpIdentifiers=[
            'YOUR_PROVIDER_IDENTIFIER'
        ]
    )
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
