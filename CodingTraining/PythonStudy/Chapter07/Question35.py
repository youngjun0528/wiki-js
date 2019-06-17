import random

def Question35():
  nameList = []
  while True:
    name = input("Enter a name : ")
    if name == '' or name is None:
      break
    else:
      nameList.append(name)
  
  index = random.randrange(0,len(nameList))
  print("The winner is... {0:s}".format(nameList[index]))