import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    sns = boto3.client('sns')
    bucket = 'event-announcement-system-<ACCOUNT-ID>'
    key = 'events.json'
    topic_arn = 'arn:aws:sns:us-east-1:<ACCOUNT-DI>:event-announcements-topic'
    
    # Handle preflight OPTIONS request
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Access-Control-Allow-Methods': 'POST,OPTIONS',
                'Access-Control-Max-Age': '86400'
            },
            'body': ''
        }
    
    # Wrap main logic in try-catch for proper error handling
    try:
        # Parse event from API Gateway
        try:
            body = event.get('body')
            if body:
                data = json.loads(body)
            else:
                data = event
            new_event = {
                "title": data["title"],
                "date": data["date"],
                "description": data["description"]
            }
        except Exception as e:
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({'error': f'Invalid input: {str(e)}'})
            }

        # Fetch current events
        try:
            response = s3.get_object(Bucket=bucket, Key=key)
            content = response['Body'].read().decode('utf-8').strip()
            events = json.loads(content) if content else []
        except Exception:
            events = []

        events.append(new_event)

        # Save updated list
        s3.put_object(
            Bucket=bucket,
            Key=key,
            Body=json.dumps(events),
            ContentType='application/json'
        )

        # Send notification
        sns.publish(
            TopicArn=topic_arn,
            Subject="New Event Created!",
            Message=f"New event: {new_event['title']} on {new_event['date']}"
        )

        # Return success response with CORS headers
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'message': 'Event created successfully'})
        }
        
    except Exception as e:
        # Return error response with CORS headers
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'error': str(e)})
        }
