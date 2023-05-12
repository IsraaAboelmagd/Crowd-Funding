from inputshelper import askforstring ,askforemail,generate_id,askforInt,valid_date
from ProjectHandler import save_project_to_file,find_project_by_id,delete_project_from_file,list_all_projects
from datetime import date
def create_project(user_id):
   title = input("Please enter book title: ")
   details=input("enter the details of project : ")
   target=askforInt("enter the total target of the project: ")
   start=valid_date("enter start date for the project")
   end=valid_date("enter end date for the project")
   while not end > start:
      end=valid_date("enter valid end date for the projct, it should be bigger than start date")
   project_info=f"{user_id}:{generate_id()}:{title}:{details}:{target}:{start}:{end}\n"
   save_project_to_file(project_info)
   print("---creating project succssefully---")
    

def delete_project(user_id):
    project_id = askforInt("Please enter the id of the project you want to delete: ") 
    found = find_project_by_id(project_id,user_id)
    if found :
        print("--- project found ")
        removed=delete_project_from_file(found[1])
        if removed:
            print('--- project deleted successfully ---')
        else:
            print("--- problem happened while deleting the project ---")
    else:
        print("Project not found, please try again with valid id ")

def display_all_projects():
    projects=list_all_projects()  
    if projects:
        for project in projects:
          print(project.strip('\n'))
    else:
        print('---- Error happened please try again ----')

def edit_project(user_id):
    project_id = askforInt("Please enter the id of the project you want to edit: ") 
    found = find_project_by_id(project_id,user_id)
    if found:
        print("--- project found ")
        project_details= found[1].strip('\n').split(":")
        print(project_details)
        while True:
         print("---which filed you want to edit---")
         edit=input("t for title --- d for details --- g for target --- s for start date --- e for end date --- x for exit: ")
         if edit=='t':
               edit_item=str(input("enter new title: "))
               project_details[2]=edit_item
         elif edit=='d':
               edit_item=input("enter new details: ")
               project_details[3]=str(edit_item)
         elif edit=='g':
               edit_item=askforInt("enter new target: ")
               project_details[4]=edit_item
         elif edit=='s':
               edit_item=valid_date("enter new start date: ")
               if str(edit_item)< project_details[6] :
                   project_details[5]=str(edit_item)
               else:
                   print("===>you can't make start date coming after end date: ")
         elif edit=='e':
               edit_item=valid_date("enter new end date")
               if str(edit_item)> project_details[5] :
                   project_details[6]=str(edit_item)
               else:
                   print("===>you can't make end date coming before start date")              
         elif edit=='x':
               print("back to main list")
               exit()     
         else:
               print("not valid choise")
         delete_project_from_file(found[1])
         project_details=f"{user_id}:{project_id}:{project_details[2]}:{project_details[3]}:{project_details[4]}:{project_details[5]}:{project_details[6]}\n"
         save_project_to_file(project_details) 
    else:
        print("Project not found, please try again with valid id ")