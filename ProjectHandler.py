def save_project_to_file(project_info):
    try:
        fileObj=open("projects.txt",'a')
    except Exception as e:
        print(e)
        return False
    else:
        fileObj.write(project_info)
        fileObj.close()
        return True

def save_projects_to_file(project_list):
    try:
        fileObj=open("projects.txt",'w')
    except Exception as e:
        print(e)
        return False
    else:
        fileObj.writelines(project_list)
        fileObj.close()
        return True
  
def list_all_projects():
    try:
        fileObj=open("projects.txt",'r')
    except Exception as e:
        print(e)
        return False
    else:
        projects=fileObj.readlines()
        return projects


def find_project_by_id(project_id,user_id):
    projects= list_all_projects()
    for project in projects:
        project_details= project.strip('\n').split(":")
        if  project_details[1]==str(project_id):
            if  project_details[0]==str(user_id):
                return True , project
    else:
        return False 


def delete_project_from_file(project):
    projects= list_all_projects()
    projects.remove(project)  # list
    removed = save_projects_to_file(projects)
    return removed

# def edit_project_into_file(project):
#     print("which filed you want to edit")