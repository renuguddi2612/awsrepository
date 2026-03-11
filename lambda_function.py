import json
import boto3

def lambda_handler(event, context):

    s3 = boto3.client('s3')

    bucket_name = "my-lambda-bucket"

    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-east-1'
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps(f"Bucket {bucket_name} created successfully")
    }