import json
import boto3
import base64

ENDPOINT = 'image-classification-2024-10-12-19-50-11-719'

def lambda_handler(event, context):
    # Decode the image data
    image = base64.b64decode(event['body']['image_data'])
    
    # Instantiate a SageMaker runtime client
    runtime = boto3.client("runtime.sagemaker")
    
    # Make a prediction
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType="image/png",
        Body=image
    )
    
    # Read the response
    inferences = json.loads(response['Body'].read().decode())

    # We return the data back to the Step Function
    event["inferences"] = inferences
    return {
        'statusCode': 200,
        'body': {"image_data": event['body']["image_data"], # json.dumps(event)
                "s3_bucket": event['body']["s3_bucket"],
                "s3_key": event['body']["s3_key"],
                "inferences": event["inferences"]
        }
    }
