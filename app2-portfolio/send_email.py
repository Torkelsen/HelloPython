import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "torkelsen.serviceacc@gmail.com"
    password = os.getenv("SERVICEACCOUNTGMAILPASSWORD")
    print("pass")
    print(password)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(from_addr=username, to_addrs=username, msg=message)