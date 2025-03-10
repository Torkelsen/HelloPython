import time
import requests
import selectorlib
import sqlite3
import smtplib, ssl
import os


URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


class Event:
    def scrape(self, url):
        """Scrape the page source from the URL"""
        response = requests.get(url, headers=HEADERS)
        source = response.text
        return  source

    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value


class Email:
    def send(self, message):
        host = "smtp.gmail.com"
        port = 465

        username = os.getenv("SERVICEACCOUNTGMAILUSERNAME")
        password = os.getenv("SERVICEACCOUNTGMAILPASSWORD")

        receiver = os.getenv("SERVICEACCOUNTGMAILUSERNAME")
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)


class Database:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)

    def read(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        band, city, date = row
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Events WHERE Band = ? AND City = ? AND Date = ?", (band, city, date))
        rows = cursor.fetchall()
        return rows

    def store(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Events (Band, City, Date) VALUES (?,?,?)", row)
        self.connection.commit()


if __name__ == "__main__":
    while True:
        event = Event()
        scraped = event.scrape(URL)
        extracted = event.extract(scraped)
        print(extracted)
        if str.lower(extracted) != "no upcoming tours":
            db = Database(db_path="data.db")
            row = db.read(extracted)
            if not row:
                db.store(extracted)
                email = Email()
                email.send(message="Hey, new event was found!")
        time.sleep(2)