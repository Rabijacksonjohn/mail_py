from mail_connect import connect_mail


# searching mail related to keyword

def search_mail():
    mail=connect_mail()
    _, data= mail.search(None,'OR','OR','TEXT', "Interview" ,'TEXT' ,"Meeting" ,'TEXT' ,"Internship")
    if data[0] :
        latest_email_id=data[0].split()[-1]
        total=len(data[0].split())
        fnd_mail=len(latest_email_id)
        print(f"{total}, number of mail is received in inbox")
        print(f"{fnd_mail}, number of mail related to keywards")
    else:
        print("no email is found in given keyword")


search_mail() 

