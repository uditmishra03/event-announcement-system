## 🔐 IAM Role Inline Policies (with Justification)

The Lambda execution role `EventRegistrationLambda-role-5g2717m0` contains the following **inline policies** to grant scoped permissions. Each policy serves a distinct purpose in the project:
<img width="1599" height="562" alt="image" src="https://github.com/user-attachments/assets/2870d9f5-4b2c-45f2-a2e1-5cbd59353363" />

---

### 📄 1. `ScopedSNSPublishPolicy`

Grants permission to publish messages to a specific SNS topic used for event notifications.

#### 📌 Why it's needed:
This policy allows the Lambda function to trigger announcements via Amazon SNS when a new event is created. It's scoped to a **single topic** (`event-announcements`) to follow the principle of least privilege.

<details>
<summary>▶️ View Policy JSON</summary>

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sns:Publish"
            ],
            "Resource": "arn:aws:sns:ap-south-1:<ACCOUNT-ID>:event-announcements"
        }
    ]
}
```
---
### 📄 2. s3-bucket-getPutObjectPolicy
Provides controlled access to an S3 bucket used for frontend hosting or reading/writing JSON files.

#### 📌 Why it's needed:
This is used if the Lambda function needs to interact with the frontend's S3 bucket (e.g., fetching events.json, updating data, etc.). This can include s3:GetObject, s3:PutObject, etc., and should be bucket-specific.

<details> <summary>▶️ View Policy JSON</summary>
  
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::event-announcement-system-<ACCOUNT-ID>/*"
        }
    ]
}
```
---
### 📄 3. AWSLambdaBasicExecutionRole (Managed Policy)
Note: This is an AWS-managed policy, not an inline one, but it's important to list here.

#### 📌 Why it's needed:
Allows the Lambda function to create log groups, write to log streams, and send log events to Amazon CloudWatch. This is essential for observability and debugging in any serverless architecture.



