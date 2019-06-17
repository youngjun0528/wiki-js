
def Question31():
  while True:
    pulse = input("Resting Pulse : ")
    if pulse.isdigit():
      pulse = int(pulse)
      break
    else:
      print("Enter the number.")
      
  while True:
    age = input("Age : ")
    if age.isdigit():
      age = int(age)
      break
    else:
      print("Enter the number.")    
    
    
  print("Intensity\t| Rate")
  print("------------------------")
  for intensity in range(55, 100, 5):
    total = int((((220-age)-pulse)*intensity/100)+pulse)
    print("{0:<d}%\t\t| {1:<d} bpm".format(intensity,total))