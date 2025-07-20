![AWS](https://img.shields.io/badge/AWS-SNS%20%7C%20Lambda%20%7C%20API%20Gateway-orange)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
[![Notion Docs](https://img.shields.io/badge/📝%20Docs-Notion-000000?logo=notion&logoColor=white)](https://graceful-cupcake-08c.notion.site/AWS-Event-Announcement-System-236bdf85cfdf8091bbebcb81ad1a7b4e?source=copy_link)

---
# 📣 AWS Event Announcement System

A fully serverless event broadcasting system built using AWS services. Users can subscribe to email notifications for events, and admins can trigger new announcements — all in real-time.
> **TL;DR**: A serverless AWS-powered app where users can subscribe to email alerts for upcoming events. Admins can trigger announcements that go out in real time to all subscribers.
---
## 📌 AWS Event Announcement System – Project Summary

---
### 💡 What It Does

- A serverless application that enables:
  - Users to **subscribe** to event notifications via email.
  - Admins to **publish event announcements** through a secure API.
  - **Real-time alerts** sent via AWS SNS to all subscribers.
- Models a **production-grade serverless architecture** using native AWS services.

---

### ⚙️ How It Works – Step-by-Step

1. **Frontend Creation**
   - Built using HTML and CSS.
   - Uses an `events.json` file to simulate event data.
   - Hosted on **Amazon S3** using **static website hosting**.

2. **Backend Setup**
   - An **SNS topic** is configured to handle:
     - Email subscriptions.
     - Event notifications sent to all confirmed subscribers.

3. **Lambda Functions**
   - Two AWS Lambda functions are deployed:
     - `SubscriptionLambda` – Handles email subscription requests.
     - `EventRegistrationLambda` – Handles new event announcements.

4. **API Gateway Integration**
   - API Gateway exposes both Lambda functions via REST endpoints:
     - `POST /subscribe`
     - `POST /create-event`
   - Frontend uses these endpoints for user interaction.

5. **End-to-End Workflow**
   - A user submits their email → hits `/subscribe` → triggers an SNS confirmation email.
   - An admin posts a new event → triggers `/create-event` → SNS broadcasts it to subscribers.

---

### 📚 Practical Use Cases

- **Event Promotion** – Collect emails for webinars, meetups, product launches.
- **Early Access Alerts** – Notify internal teams or testers about new features/releases.
- **Birthday Shoutouts** – Hook into team calendars and send automated celebration emails.

---

### ✅ Key Benefits

- Fully **serverless**, **event-driven**, and **scalable**.
- Can be built **within the AWS Free Tier** (if cleaned up post-deployment).
- Can be implemented in **~2–3 hours**.

---

## 🚀 Features

- Static frontend hosted on S3.
- Serverless backend via AWS Lambda and API Gateway.
- Email notifications via AWS SNS.
- Simple, secure, and scalable.

---

## 🧱 Architecture

<img width="948" height="427" alt="image" src="https://github.com/user-attachments/assets/670ef6ec-13a3-41cc-b868-99ee122a64cd" />
<img width="716" height="447" alt="image" src="https://github.com/user-attachments/assets/ff03cc66-48a3-48fa-a83a-dc0ca19d2c99" />


---

## 🧩 Tech Stack

- **Frontend**: S3 Static Website Hosting (HTML/CSS/JS)
- **Backend**: AWS Lambda + API Gateway
- **Notifications**: AWS SNS
- **Security**: IAM Roles & Policies
- **Monitoring**: CloudWatch

---

## 📂 Project Structure
```
📁 frontend/
├── index.html
└── events.json
📁 backend/
├── EventRegistrationLambda
└── SubscriptionLambda
📁 infra/
├── sns-setup.sh
└── lambda-role.json
README.md
```
---

## 📦 Deployment Steps

1. **Create SNS Topic**
   - Use AWS Console or CLI to create a topic like `event-announcements`.

2. **Deploy Lambda Functions**
   - Two functions:
     - `SubscriptionLambda`
     - `EventRegistrationLambda`
   - Attach least-privilege IAM roles.

3. **Set Up API Gateway**
   - POST `/subscribe` → `SubscriptionLambda`
   - POST `/create-event` → `EventRegistrationLambda`

4. **Configure S3 Bucket**
   - Enable static website hosting.
   - Upload frontend files.

5. **Connect Everything**
   - Ensure correct permissions and CORS.
   - Test via curl or Postman.

---

## 🧪 Testing

- ✅ Subscription flow — confirmation email received.
- ✅ Duplicate email test.
- ✅ Admin event trigger → mass notification delivery.

---

## 🔒 Security

- IAM roles with minimum privileges.
- No hardcoded secrets.
- API Gateway with CORS rules.
- S3 Bucket Policy only for static assets.

---

## 📸 Snapshots

<details>
<summary>🎯 S3 Hosted Frontend</summary>

<img width="1646" height="891" alt="image" src="https://github.com/user-attachments/assets/ed6cbfc5-48d4-4354-aee2-86c8a39e0dc1" />

</details>

<details>
<summary>🚀 API Gateway Test</summary>

<img width="1264" height="364" alt="image" src="https://github.com/user-attachments/assets/4169d4ff-39f8-4a81-bd10-28ea65205ce8" />
<img width="1219" height="382" alt="image" src="https://github.com/user-attachments/assets/a27faee7-7217-48cd-a850-98c100fb22ac" />

</details>

<details>
<summary>📬 SNS Subscription</summary>

<img width="1231" height="613" alt="image" src="https://github.com/user-attachments/assets/4f5653c7-4424-4745-97be-e0d552f41f33" />

</details>

<details>
<summary>✉️ Email Notification</summary>

<img width="902" height="286" alt="image" src="https://github.com/user-attachments/assets/b684e4e9-9a55-413d-81a8-674b2e9fc794" />

</details>

<details>
<summary>📢 Event Notification</summary>

<img width="682" height="618" alt="image" src="https://github.com/user-attachments/assets/a05a8d82-9644-4ba2-9a7f-54bb52928b56" />
<img width="1203" height="387" alt="image" src="https://github.com/user-attachments/assets/e258db2e-b1a8-4610-bf88-2e7c939ddbb0" />

</details>

---

## 📈 Future Enhancements

- Admin dashboard for event creation.
- Authenticated submissions using Cognito.
- Event logs stored in DynamoDB.
- Automated CI/CD via GitHub Actions or SAM/CDK.

---

## 🧾 Sample API Payloads

**/subscribe**
```json
{
  "email": "someone@example.com"
}
```
**/create-event**
```json
{
  "title": "DevOps Webinar",
  "description": "Join us for a deep dive into serverless architecture.",
  "date": "2025-08-01"
}
```
---
## 📄 License
MIT License
```
MIT License

Copyright (c) 2025 Udit Mishra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell     
copies of the Software, and to permit persons to whom the Software is         
furnished to do so, subject to the following conditions:                      

The above copyright notice and this permission notice shall be included in    
all copies or substantial portions of the Software.                           

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR    
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,      
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE   
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER        
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN     
THE SOFTWARE.
```
---

<div align="center">

**⭐ If this project helped you, please consider giving it a star! ⭐**

Made with ❤️ using AWS Serverless Technologies

</div>
