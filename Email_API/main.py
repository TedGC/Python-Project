import requests
# import send_email

# make it more dynamic for various topics
topic = 'tesla'

api_key = "9a23c1c29bda4520b3f536b36ebecf21"
url = "https://newsapi.org/v2/everything?" \
        f"q={topic}&" \
        "from=2025-12-13&" \
        "sortBy=publishedAt&" \
        "apiKey=9a23c1c29bda4520b3f536b36ebecf21"

request = requests.get(url)

content = request.json()

body=''
for article in content['articles']:
    if article['title'] is not None:
        "Subject: Today's News"
        body = body + article['title'] + '\n' \
    + '\n' + article['description'] + '\n' + article['url'] + 2 * '\n'

body = body.encode('utf-8')
send_email(message=body)