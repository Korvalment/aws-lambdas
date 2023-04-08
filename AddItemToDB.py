import json
import boto3


def lambda_handler(event, context):
    
    client = boto3.client('dynamodb')
    
    response = client.put_item(
    TableName='tech_user_list',
    Item = {
        "tech_user_id": {
            "S": str(event["key1"])
        },
        "tech_user_pool_id": {
            "S": str(event["key2"])
        }
    })
    
    response = json.loads(json.dumps(response, default=str))
    return response
