import re

def Question27():
  first_name = input("Enter the first name : ")
  last_name = input("Enter the last name : ")
  zip_code = input("Enter the ZIP code : ")
  employee_id = input("Enter an employee ID : ")
  
  check = True
  if len(first_name) == 0:
    check = False
    print("The first name must be filled in")
  elif len(first_name) < 2:
    check = False
    print("{0:s} is not a valid first name. It is too short.".format(first_name))
    
  if len(last_name) == 0:
    check = False
    print("The last name must be filled in")
  elif len(last_name) < 2:
    check = False
    print("{0:s} is not a valid last name. It is too short.".format(last_name))
  
  zip_code_format = re.compile("[0-9]+")
  
  if re.match(zip_code_format, zip_code) is None:
    check = False
    print("The ZIP code must be numeric")
  
  id_format = re.compile("[A-Z]{2}-[0-9]{4}")
  if re.match(id_format, employee_id) is None:
    check = False
    print("{0:s} is not a vald ID.".format(employee_id))
  
  if check:
    print()