
def Question22():
  first = int(input("Enter the first number : "))
  second = int(input("Enter the second number : "))
  third = int(input("Enter the third number : "))
  list = [first, second, third]
  list.sort(reverse=True)
  print("The largest number is {0:d}".format(list[0]))