import boto3

def lambda_handler(event, context):
    
    user_pool_id = 'eu-central-1_JpCVzF1l2'
    
    attribute_name = event['user_pool_id']
    
    attribute_value = user_pool_id
    
    cognito_client = boto3.client('cognito-idp')
    cognito_client.delete_user_pool(UserPoolId=user_pool_id)
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tech_user_list')
    response = table.delete_item(
        Key={
            'ID': attribute_value
        }
    )
    
    return {
        'statusCode': 200,
        'body': 'User Pool deleted'
    }
