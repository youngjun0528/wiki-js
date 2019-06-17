
def Question34():
  employee = []
  employee.append("Jhon Smish")
  employee.append("Jackie Jackson")
  employee.append("Chris Jones")
  employee.append("Amanda Cullen")
  employee.append("Jeremy Goodwin")
  
  print("There are {0:d} employees : ".format(len(employee)))
  for index in employee:
    print(index)
    
  remove = input("Enter an employee name to remove : ")
  del(employee[employee.index(remove)])
  
  print("There are {0:d} employees : ".format(len(employee)))
  for index in employee:
    print(index)
  
  