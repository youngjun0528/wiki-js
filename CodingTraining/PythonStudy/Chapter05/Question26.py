
import math

def Question26():
  balance = int(input("What is your balance ? "))
  percent = int(input("What is the APR on the card (as a percent) ? "))
  payment = int(input("What is the monthly payment yu can make ?"))
  
  result = calculate_manths_until_paid_off(balance, percent, payment)
  
  print("It will take you {0:d} months to pay off this card.".format(round(result+0.5)))
  
def calculate_manths_until_paid_off(balance, percent, payment):
  return -(1/30) * (math.log(1 + (balance/payment)*(1-(1+percent/36500)**30)) / math.log(1+percent/36500))