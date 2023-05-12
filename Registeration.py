import re
from inputshelper import askforstring ,askforemail,generate_id
from userHandler import save_user_to_file
def registeration():
    user_id=generate_id()
    first_name=askforstring("Enter your First Name: ")
    last_name=askforstring("Enter your Last Name: ")
    email=askforemail("Enter your Email: ")
    password=input("Enter password : ")
    confirm_password=input("confirm password: ")
    while confirm_password != password:
        confirm_password=input("Not the same password enter it again: ")
    mobile_phone=input("Enter your number: ")
    while not re.fullmatch("^01[0125][0-9]{8}$", mobile_phone):
            mobile_phone=input("Not vailed number ,Enter your number again: ")
    user_info=f"{user_id}:{first_name}:{last_name}:{email}:{password}:{mobile_phone}\n"
    #add_user
    save_user_to_file(user_info)  

    print("---success registration---") 
