import boto3
import base64

def lambda_handler(event, context):
    path = event['rawPath'].lstrip('/')  # Extract image path

    # Initialize S3-compatible client
    s3 = boto3.client(
        's3',
        endpoint_url='https://your-storage-endpoint.com',
        aws_access_key_id='YOUR_ACCESS_KEY',
        aws_secret_access_key='YOUR_SECRET_KEY',
        region_name='your-region'
    )

    try:
        obj = s3.get_object(Bucket='your-bucket-name', Key=path)
        content = obj['Body'].read()
        content_type = obj.get('ContentType', 'application/octet-stream')

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": content_type,
                "Cache-Control": "public, max-age=86400"
            },
            "body": base64.b64encode(content).decode('utf-8'),
            "isBase64Encoded": True
        }

    except:
        return {"statusCode": 404, "body": "Not Found"}
