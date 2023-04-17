import json
import boto3

def lambda_handler(event, context):
    # Create a DynamoDB resource
    dynamodb = boto3.resource('dynamodb')

    # Get the table
    table = dynamodb.Table('tech_user_list')

    # Scan the table to get all the items
    response = table.scan()

    # Extract the items from the response
    items = response['Items']

    # Continue scanning until we've retrieved all items
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        items.extend(response['Items'])

    # Return the items in a JSON response
    return {
        'statusCode': 200,
        'body': json.dumps(items)
    }