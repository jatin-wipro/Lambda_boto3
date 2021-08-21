import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    
  data = client.get_item(
    TableName='CUSTOMERS',
    Key={
        'CUSTOMER_ID': {
          'S': '1234'
        }
    }
  )

  response = {
      'statusCode': 200,
      'body': json.dumps(data),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response
  
  
