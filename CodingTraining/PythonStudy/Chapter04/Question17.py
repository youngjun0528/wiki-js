
def Question17():
  print("Weight : ")
  weight = int(input())
  print("Gender(Man / Woman) : ")
  gender = input()
  print("Alcol : ")
  alcol = int(input())
  print("Hour : ")
  time = int(input())
  
  if gender.lower() == "man":
    check = 0.73
  else:
    check = 0.6
    
  bac = (alcol * 5.14 / weight * check) - 0.015 * time
  print("Your BAC is {0:.2f}".format(bac))
  if bac > 0.08:
    print("It is not legal for your to drive.")
  else:
    print("It is legal for your to drive.")
  