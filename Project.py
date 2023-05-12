import time
from ProjectHandler import list_all_projects
from ProjectFunctios import create_project,delete_project,display_all_projects,edit_project
from Login import find_user_to_login
def mainmenu():
    user_id=find_user_to_login()
    while True:
        choice = input("please enter n for new , l for list all , e for edit , d for delete, x for exit: ")
        if choice=='n':
            create_project(user_id)
        elif choice=='l':
           display_all_projects()
        elif choice=='e':
            edit_project(user_id)
        elif choice=='d':
            delete_project(user_id)
        elif choice=='x':
            print("====> Bye <====")
            exit()
