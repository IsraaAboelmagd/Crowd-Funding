def save_user_to_file(user_info):
    try:
        fileObj=open("users.txt",'a')
    except Exception as e:
        print(e)
        return False
    else:
        fileObj.write(user_info)
        fileObj.close()
        return True
    
def list_all_users():
    try:
        fileObj=open("users.txt",'r')
    except Exception as e:
        print(e)
        return False
    else:
        users=fileObj.readlines()
        return users
   
