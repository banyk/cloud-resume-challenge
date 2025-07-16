import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('resume-views')

def lambda_handler(event, context):
    response = table.get_item(Key={'id': 'home'})
    views = response.get('Item', {}).get('views', 0)

    new_views = views + 1

    table.put_item(Item={'id': 'home', 'views': new_views})

    # TODO implement
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
        },
        'body': json.dumps({'views': int(new_views)})
    }
