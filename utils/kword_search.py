from utils.mail_connect import connect_mail
from utils.key_act import get_key
import email
from email.header import decode_header
    
def search_mail():
    keywords=get_key()
    mail=connect_mail()
    matched_id=set()

    for keyword in keywords:
        status, data=mail.search(None,"TEXT",keyword)

        if status == "OK" and data[0]:
            matched_id.update(data[0].split())

    print(f"Found {len(matched_id)} matching mail(s)\n")

    for email_id in matched_id:
        # RFC822 mean i need all the content of the mail
        status, mes_data=mail.fetch(email_id,"(RFC822)")

        if status =="OK":
            raw_mail=mes_data[0][1]
            msg=email.message_from_bytes(raw_mail)

            sender=msg.get("From")

            subject,encoding=decode_header(msg["Subject"])[0]

            if isinstance (subject,bytes):
                subject=subject.decode(encoding or 'utf-8')

            print(f"From : {sender}")
            print(f"Subject : {subject}")
            print("-"*50)