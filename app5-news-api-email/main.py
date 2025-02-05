import requests
from email_service import send_email

APIKEY = "be835079174d475d91290e3dac7f495f"
TOPIC = "tesla"
url = f"https://newsapi.org/v2/everything?q={TOPIC}&sortBy=publishedAt&apiKey={APIKEY}&language=en"

response = requests.get(url)
content = response.json()
articles = content["articles"][:20]
message = "Daily news from NewsAPI.org about Tesla\n\n"


for article in articles:
    message += article["title"] or "Missing Title"
    message += "\n"
    message += article["description"] or "Missing Description"
    message += "\n"
    message += article["url"] or "Missing url"
    message += 2*"\n"

#message = message.encode("utf-8")

send_email("Daily News", message)