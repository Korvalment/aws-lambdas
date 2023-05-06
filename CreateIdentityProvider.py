import boto3

def lambda_handler(event, context):
    client = boto3.client('cognito-idp')
    try:
        with open('metadata.xml') as f:
            metadata_file = f.read()
            provider_details = {'MetadataFile': metadata_file}
    except FileNotFoundError:
        try:
            metadata_url = 'https://example.com/metadata'
            provider_details = {'MetadataURL': metadata_url}
        except:
            raise Exception('metadata does not exist')
    response = client.create_identity_provider(
        UserPoolId='eu-central-1_qIrMsVE3U', # user pool id, change this
        ProviderName='TestProvider',
        ProviderType='SAML',
        ProviderDetails=provider_details,
        AttributeMapping={
            'email': 'email', # email, chage this 
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
