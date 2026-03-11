import json
import boto3

def lambda_handler(event, context):

    s3 = boto3.client('s3')

    bucket_name = "lambda-demo-bucket-987654321"

    s3.create_bucket(Bucket=bucket_name)

    return {
        'statusCode': 200,
        'body': json.dumps("Bucket created successfully")
    }