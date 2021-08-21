import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CUSTOMERS')


def lambda_handler(event, context):
    table.get_item(Item=event)
    return {"code":200 , "message":"done"}
