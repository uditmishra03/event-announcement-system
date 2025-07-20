#!/bin/bash

# ------------------------------------------
# SNS Setup Script for Event Announcement System
# ------------------------------------------

TOPIC_NAME="event-announcements"
EMAIL="${1:-you@example.com}"  # Pass email as first argument, or use default

echo "Creating SNS topic: $TOPIC_NAME..."
TOPIC_ARN=$(aws sns create-topic --name "$TOPIC_NAME" --query 'TopicArn' --output text)

if [[ -z "$TOPIC_ARN" ]]; then
  echo "❌ Failed to create SNS topic. Exiting."
  exit 1
fi

echo "✅ SNS topic created: $TOPIC_ARN"

echo "Subscribing email: $EMAIL to $TOPIC_ARN..."
aws sns subscribe \
  --topic-arn "$TOPIC_ARN" \
  --protocol email \
  --notification-endpoint "$EMAIL"

echo "📩 Subscription request sent to: $EMAIL"
echo "🔔 Waiting for email confirmation. Check your inbox to confirm."

# Optional test publish (commented out)
# echo "Sending test message..."
# aws sns publish \
#   --topic-arn "$TOPIC_ARN" \
#   --subject "Test Announcement" \
#   --message "Hello from SNS setup script!"

# echo "✅ Test message sent."
