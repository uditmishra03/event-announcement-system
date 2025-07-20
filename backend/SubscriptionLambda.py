import json
import boto3

def lambda_handler(event, context):
    try:
        print("Received event:", json.dumps(event))
        
        # If coming from API Gateway with Lambda Proxy integration, the body is a string
        if 'body' in event:
            body = json.loads(event['body'])  # Decode stringified JSON
        else:
            body = event

        email = body.get('email')
        if not email:
            raise ValueError("Missing email in request.")

        sns = boto3.client('sns')
        topic_arn = 'arn:aws:sns:us-east-1:<ACCOUNT-ID>:event-announcements-topic'

        response = sns.subscribe(
            TopicArn=topic_arn,
            Protocol='email',
            Endpoint=email, 
            ReturnSubscriptionArn=True

        )
        print("SNS response:", response)

        return {
            "statusCode": 200,
            "headers": {  # Add this if frontend needs CORS
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*"
            },
            "body": json.dumps({"message": "Subscription request sent."})
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*"
            },
            "body": json.dumps({"error": str(e)})
        }
