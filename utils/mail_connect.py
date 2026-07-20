from dotenv import load_dotenv
import os
import imaplib
import email


load_dotenv()


username=os.getenv("EMAIL")
password=os.getenv("PASSWORD")

# Connect mail with username and password

def connect_mail():
    mail=imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username,password)
    mail.select("inbox")
    print("mail is connected")
    return mail
