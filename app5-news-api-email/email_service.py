import os
import ssl, smtplib
from email.mime.text import MIMEText

def send_email(subject, message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("SERVICEACCOUNTGMAILUSERNAME")
    password = os.getenv("SERVICEACCOUNTGMAILPASSWORD")

    context = ssl.create_default_context()

    msg = MIMEText(message, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = username
    msg["To"] = username

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.send_message(msg)