import json

def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "task": "default",
        "headers": {"Content-Type": "application/json"},
        "body": event,
    }