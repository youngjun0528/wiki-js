
def Question18():
  print("Press C to convert from Fahrenheit to Celsius.")
  print("Press F to convert from Celsius to Fahrenheit.")
  print("Your choice:")
  command = input()
  
  if command.lower() == 'c':
    print("print enter the temperature in Fahrenheit:")
    temperature = int(input())
    gen_temp = (temperature - 32) * 5/9
    print("The temperature in Celsius is {0:.2f}".format(gen_temp))
    
  if command.lower() == 'f':
    print("print enter the temperature in Fahrenheit:")
    temperature = int(input())
    gen_temp = (temperature * 5/9) + 32
    print("The temperature in Celsius is {0:.2f}".format(gen_temp))  