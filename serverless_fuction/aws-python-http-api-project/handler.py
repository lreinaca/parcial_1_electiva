import json


def hello(event, context):
    body = {
        "message": "Hello Lorena, Welcome to the Serverless World!",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
