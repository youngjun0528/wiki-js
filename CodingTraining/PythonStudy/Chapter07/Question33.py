import random

def Question33():
  answer = ["Yes", "No", "Maybe", "Ask again later", "Concentrate and ask again", "Outlook good", "Not bad", "It is certain"]
  
  index = random.randrange(0,8)
  input("What'syour question? ")
  print(answer[index])