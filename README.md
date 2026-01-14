# 📰 Automated Daily Tech News Notifier

A serverless AWS application that automatically fetches trending technology news and delivers a curated digest to your inbox every 24 hours.

## 🔗 Project Links
- **Live Status Dashboard:** [PASTE_YOUR_AMPLIFY_URL_HERE]
- **Demonstration Video:** [PASTE_YOUR_VIDEO_LINK_HERE]

## 🏗️ Architecture
The system utilizes a modern, event-driven serverless architecture for maximum efficiency and zero maintenance.



## 🛠️ Services Used
- **Amazon EventBridge:** Scheduled "Cron" trigger that automates the daily workflow.
- **AWS Lambda:** Serverless compute engine that executes the Python backend logic.
- **Amazon SES (Simple Email Service):** Enterprise-grade email delivery for the news digest.
- **AWS Amplify:** Managed hosting for the public status dashboard.
- **NewsAPI:** External REST API providing real-time technology headlines.

## 🔄 Detailed Working Flow
The application operates in a five-stage automated pipeline:

1. **Automation:** **Amazon EventBridge** is configured with a schedule expression (e.g., `rate(1 day)`). At the designated time, it publishes an event to trigger the Lambda function.
2. **Ingestion:** The **AWS Lambda** function initiates a secure HTTPS request to the **NewsAPI** endpoint to retrieve the latest top 5 technology headlines in JSON format.
3. **Processing:** The Python script parses the raw data, extracting article titles, sources, and direct links. It then dynamically injects this content into a professionally styled **HTML/CSS Email Template**.
4. **Communication:** Lambda interfaces with the **Amazon SES** API to send the formatted newsletter to verified email addresses, ensuring high deliverability.
5. **Monitoring:** A status page hosted on **AWS Amplify** provides a real-time heartbeat of the system, displaying the timestamp of the last successful execution.

## 🚀 Deployment Guide
1. **API Setup:** Obtain an API key from [newsapi.org](https://newsapi.org).
2. **Email Verification:** Verify your sender/receiver emails in the **Amazon SES** console.
3. **Backend:** Deploy the Python code in `/backend` to a Lambda function and attach the `AmazonSESFullAccess` policy.
4. **Trigger:** Create an **EventBridge** schedule rule targeting your Lambda function.
5. **Frontend:** Zip the `/frontend` folder and deploy to **AWS Amplify**.

---
