import time
import requests
import selectorlib
from send_email import send_email
import db_context
import sqlite3


URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect("data.db")

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return  source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

def store_file(extracted):
    with open("data.txt", "a") as file:
        file.writelines(extracted + "\n")

def read_file():
    with open("data.txt", "r") as file:
        return file.read()

def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Events WHERE Band = ? AND City = ? AND Date = ?")
    db_context.query("")

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        if str.lower(extracted) != "no upcoming tours":
            if extracted not in read_file():
                store_file(extracted)
                send_email(message="Hey, new event was found!")
        time.sleep(2)