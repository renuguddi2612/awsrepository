import json
import urllib.request

def lambda_handler(event, context):

    url = "https://api.example.com/data"

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    print(data)

    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }