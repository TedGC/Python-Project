import requests
import send_email

api_key = "9a23c1c29bda4520b3f536b36ebecf21"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-12-13&sortBy=publishedAt&apiKey=9a23c1c29bda4520b3f536b36ebecf21"

request = requests.get(url)

content = request.json()

body=''
for article in content['article']:
    if article['title'] is not None:
        body = body + article['title'] + '\n' + article['description'] + 2 * '\n'

body = body.encode('utf-8')
send_email(message=body)