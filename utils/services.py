from .key_act import add_key,show_key,del_key
import os
from utils.kword_search import search_mail


def clear():
    os.system("cls" if os.name == "nt" else "clear")

def serv():
    print("-------------- MailPy ----------------\n")
    print("1. Connect to my mail with MailPy ")
    print("2. Add Keyword for search ")
    print("3. Remove keyword from search ")
    print("4. Search the mail ")
    print("5. Quite \n")



def services():
    x=True
    while x:
        try:
           
            serv()
            ans=int(input("Enter the number of the services you need : "))
            clear()

            if 1 <= ans <= 5:
            
                if ans == 5:
                    x=False


                else:
                    if ans == 1:
                        print("This services will be active soon")

                    elif ans == 2:
                        a=True
                        while a:
                            print("----------- Adding new key list ------------")
                            print("1. Add keyword")
                            print("2. Quite")
                            keyans=int(input("Enter the number of services : "))
                            clear()
                            if 1 <= keyans <=2:
                                if keyans ==2:
                                    a=False
                                else:
                                    key_wd=input("Enter the keyword : ")
                                    try:
                                        add_key(key_wd)
                                        show_key()
                                    except Exception as e :
                                        print(e)

                                    print(f'{key_wd},is added. ')
                            else:
                                print("Enter valide answer... \n")

                    elif ans == 3:
                        a=True
                        while a:
                            print("----------- Deleting key from list ------------")
                            print("1. Delete keyword")
                            print("2. Quite")
                            keyans=int(input("Enter the number of services : "))
                            clear()
                            if 1 <= keyans <=2:
                                if keyans ==2:
                                    a=False
                                else:
                                    show_key()
                                    key_wd=input("Enter the id : ")
                                    try:
                                        del_key(key_wd)
                                        show_key()
                                    except Exception as e :
                                        print(e)

                                    print(f'{key_wd},is deleted. ')
                            else:
                                print("Enter valide answer... \n")

                    elif ans == 4:
                        search_mail()
                        print(" \n")
        
            else:
                print("Enter the value correct! \n")

        except :
            print("invalid input, Please enter a Number in the list of services \n")

    
