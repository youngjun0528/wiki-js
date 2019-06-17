
def Question38():
  list_num = input("Enter a list of numbers, separated by spaces : ")
  
  even_num = filterEvenNumber(list_num)
  
  print_num = ""
  for index in even_num:
    print_num = print_num + str(index) + " "  
  
  print("The even numbers are {0:s}.".format(print_num))
  
def filterEvenNumber(list_num):
  list_num = list_num.strip()
  even_num = []
  for index in list_num.split(' '):
    if int(index) > 0 and int(index)%2 == 0:
      even_num.append(index)
  return even_num