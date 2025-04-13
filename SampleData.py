import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ProductPrices')

def lambda_handler(event, context):
    products = [
        {
            "productName": "iPhone 14",
            "storePrices": [
                {"store": "Amazon", "price": 799},
                {"store": "Flipkart", "price": 789},
                {"store": "Walmart", "price": 810}
            ]
        },
        {
            "productName": "Samsung Galaxy S22",
            "storePrices": [
                {"store": "Amazon", "price": 699},
                {"store": "Flipkart", "price": 685},
                {"store": "BestBuy", "price": 710}
            ]
        },
        {
            "productName": "MacBook Pro 14",
            "storePrices": [
                {"store": "Amazon", "price": 1999},
                {"store": "Apple Store", "price": 1999},
                {"store": "Flipkart", "price": 1980}
            ]
        },
        {
            "productName": "Dell XPS 13",
            "storePrices": [
                {"store": "Amazon", "price": 999},
                {"store": "Dell Store", "price": 980},
                {"store": "BestBuy", "price": 995}
            ]
        },
        {
            "productName": "OnePlus 12",
            "storePrices": [
                {"store": "Amazon", "price": 599},
                {"store": "Flipkart", "price": 590},
                {"store": "Croma", "price": 610}
            ]
        },
        {
            "productName": "Sony WH-1000XM5",
            "storePrices": [
                {"store": "Amazon", "price": 349},
                {"store": "Sony Store", "price": 359},
                {"store": "BestBuy", "price": 355}
            ]
        },
        {
            "productName": "iPad Air 5",
            "storePrices": [
                {"store": "Amazon", "price": 599},
                {"store": "Apple Store", "price": 599},
                {"store": "Flipkart", "price": 585}
            ]
        },
        {
            "productName": "Lenovo Yoga 9i",
            "storePrices": [
                {"store": "Amazon", "price": 1299},
                {"store": "Lenovo Store", "price": 1275},
                {"store": "BestBuy", "price": 1305}
            ]
        }
    ]
    
    result = []

    for product in products:
        try:
            table.put_item(Item=product)
            result.append({"product": product["productName"], "status": "Inserted"})
        except Exception as e:
            result.append({"product": product["productName"], "status": "Failed", "error": str(e)})

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Seeding completed",
            "result": result
        })
    }
