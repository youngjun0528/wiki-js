
def Question36():
  numList = []
  while True:
    num = input("Enter a number : ")
    if num == 'done':
      break
    else:
      numList.append(int(num))
  
  total = 0
  print("Numbers: ", end='')
  for index in range(len(numList)):
    total += numList[index]
    if index < len(numList)-1:
      print(numList[index], end=', ')
    else:
      print(numList[index])
  
  avg = total / len(numList)
  numList.sort()
  min = numList[0]
  max = numList[len(numList)-1]
  root = avg ** 0.5
  
  print("The average is {0:.2f}".format(avg))
  print("The minimum is {0:d}".format(min))
  print("The maximum is {0:d}".format(max))
  print("The standard deviation is {0:.2f}".format(root))