import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "app8flask@gmail.com"
    password = "YOUR_GMAIL_PASSWORD" # this can be retrieved from google security and go to the account setting and obtain the key looking digits

    receiver = "app8flask@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
        

send_email("Hello, how are you?")
