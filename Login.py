from userHandler import list_all_users

def find_user_to_login():
    email=input("enter your email: ")
    password=input("enter your password: ")
    users = list_all_users()
    for user in users:
        user_details= user.strip('\n').split(":")
        if user_details[3]==email:
            if user_details[4]==password:
                print("---you entered successfully---")
                return user_details[0]
    else:
        print("---you failed maybe your email or password isn't correct---\n=====please try again====")
        find_user_to_login()
        
        # return user_details[0]
