import json
import urllib3
import boto3

def lambda_handler(event, context):
    # 1. Setup (Change these!)
    API_KEY = '91e6bb41176342158ed71d79f26axxxx'
    VERIFIED_EMAIL = 'abc@gmail.com' # The one you verified in Step 1
    
    url = f"https://newsapi.org/v2/top-headlines?category=technology&language=en&apiKey={API_KEY}"
    http = urllib3.PoolManager()
    
    try:
        # 2. Fetch News
        response = http.request('GET', url)
        data = json.loads(response.data.decode('utf-8'))
        articles = data.get('articles', [])[:5] # Top 5 stories
        
        # 3. Format Message
        email_body = "Good Morning! Here is your daily Tech News:\n\n"
        for art in articles:
            email_body += f"TITLE: {art['title']}\nLINK: {art['url']}\n\n"
            
        # 4. Send Email via SES
        ses = boto3.client('ses')
        ses.send_email(
            Source=VERIFIED_EMAIL,
            Destination={'ToAddresses': [VERIFIED_EMAIL]},
            Message={
                'Subject': {'Data': 'Daily AWS Tech Digest'},
                'Body': {'Text': {'Data': email_body}}
            }
        )
        
        return {"statusCode": 200, "body": "News email sent!"}
        
    except Exception as e:
        print(f"Error: {e}")
        return {"statusCode": 500, "body": str(e)}