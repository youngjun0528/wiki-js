
def Question29():
  while True:
    rate = input("What is the rate of return ? ")
    if is_number(rate):
      years = round(72/float(rate) + 0.5)
      print("It will take {0:d} years to double your initial investment.".format(years))
      break
    else:
      print("Sorry. Thats not a valid input.")
    
def is_number(rate):
  try:
    if float(rate) == 0:
      return False
    else:
      return True
  except ValueError:
    return False