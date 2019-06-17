import random

def Question32():
  while True:
    print("Let's play Guess the Number.")
    level = input("Pik a difficulty level(1, 2 or 3) : ")
    result = 0
    if int(level) == 1:
      result = random.randrange(1,10)
    elif int(level) == 2:
      result = random.randrange(1,100)
    elif int(level) == 3:
      result = random.randrange(1,1000)
    count = 0
    temp = input("I have my number. What's your guess? : ")
    while True:
      if not(temp.isdigit()):
        count = count + 1
        temp = input("Worng Number. Guess Again : ")
      elif int(temp) > result:
        count = count + 1
        temp = input("Too high. Guess Again : ")
      elif int(temp) < result:
        count = count + 1
        temp = input("Too low. Guess Again : ")
      elif int(temp) == result:
        print("Complete {0:s} Number! You got it in {1:d} guesses!".format(temp, count))
        break
    again = input("Play Again ?")
    if again == 'n':
      break
  print("Goodbye!")
      