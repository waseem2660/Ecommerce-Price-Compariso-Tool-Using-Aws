import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ProductPrices')

# Helper function to convert Decimal to float or int
def convert_decimal(obj):
    if isinstance(obj, list):
        return [convert_decimal(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: convert_decimal(v) for k, v in obj.items()}
    elif isinstance(obj, Decimal):
        return float(obj) if obj % 1 else int(obj)
    return obj

def lambda_handler(event, context):
    product_name = event.get('queryStringParameters', {}).get('productName')
    
    if not product_name:
        return {
            "statusCode": 400,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"message": "Missing productName parameter"})
        }

    try:
        response = table.get_item(Key={"productName": product_name})
        item = response.get("Item")
        
        if not item:
            return {
                "statusCode": 404,
                "headers": {
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({"message": "Product not found"})
            }

        # Convert Decimal to native types
        clean_item = convert_decimal(item)

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps(clean_item)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"message": "Internal Server Error", "error": str(e)})
        }
