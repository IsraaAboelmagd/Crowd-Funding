from Registeration import registeration
from Project import mainmenu
print("==== Welcom to Crowd-Funding console app ====")
your_choise=input("--choose 1 for Registeration OR 2 for Login-- ")
if your_choise=='1':
    registeration()
elif your_choise=='2':
    mainmenu()
else:
    print("Not valid choise the program is exit")
