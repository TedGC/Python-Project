import requests

api_key = "9a23c1c29bda4520b3f536b36ebecf21"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-12-13&sortBy=publishedAt&apiKey=9a23c1c29bda4520b3f536b36ebecf21"

request = requests.get(url)

content = request.json()

for article in content:
    print(article['title'])
