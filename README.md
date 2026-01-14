# 📰 Automated Daily Tech News Notifier

A serverless AWS application that automates the delivery of trending technology news. The system fetches real-time headlines from the NewsAPI and delivers a curated digest directly to a user's inbox every 24 hours.

## 🔗 Project Links
- **Live Status Dashboard:** [PASTE_YOUR_AMPLIFY_URL_HERE]
- **Demonstration Video:** [PASTE_YOUR_VIDEO_LINK_HERE]

## 🛠️ Tech Stack
- **Compute:** AWS Lambda (Python 3.12)
- **Automation:** Amazon EventBridge (Cron Scheduler)
- **Communication:** Amazon SES (Simple Email Service)
- **Hosting:** AWS Amplify (Frontend Status Dashboard)
- **API:** NewsAPI.org
- **Frontend:** HTML5, CSS3 (Modern Glassmorphism Design)

## 🏗️ Architecture
The project follows a decoupled, event-driven serverless architecture:

1. **Trigger:** **Amazon EventBridge** wakes up the system once every 24 hours.
2. **Compute:** **AWS Lambda** performs a `GET` request to NewsAPI to fetch top tech headlines.
3. **Processing:** The Python script parses the JSON response and formats it into a clean HTML email template.
4. **Delivery:** **Amazon SES** handles the secure delivery of the news digest to verified email addresses.
5. **UI:** **AWS Amplify** hosts a professional landing page to monitor system status.

![Architecture Diagram](./architecture-diagram.png)
