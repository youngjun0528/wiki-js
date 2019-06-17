
def Question19():
  print("Your Weight :")
  weight = int(input())
  print("Your Height :")
  height = int(input())
  bmi = (weight/(height*height))*703
  print("Your BMI is {0:.2f}".format(bmi))
  if bmi > 18.5 and bmi < 25:
    print("you are within the ideal weight range")
  else:
    print("You date overweight. You should see your doctor.")