import re
import time
from datetime import date
def askforstring(message):
    while True:
        instr = input(message)
        if instr.isalpha():
            return  instr
        print("----Error --> please enter it again-----")

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def askforemail(message):
    while True:
        email  = input(message)
        result =  re.fullmatch(pattern, email) 
        if result:
            return email
        print("----Error --> please enter it again-----")

def generate_id():
    return round(time.time())

def askforInt(message):
    while True:
        intnum = input(message)
        if intnum.isdigit():
            return  int(intnum)
        print("----Error --> please enter it again-----")

def valid_date(message):
    print(message)
    year = int(input('Enter a year: '))
    month = int(input('Enter a month: '))
    day = int(input('Enter a day: '))
    return date(year, month, day)
    
