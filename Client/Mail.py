import smtplib
import email.message import EmailMessage

class Mail():
    def __init__(self):
        self.mailFrom = "2021jubijubi@gmail.com"
        self.mailPassword = "qwer1234!@#$"
        self.mailTo = None