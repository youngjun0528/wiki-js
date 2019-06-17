import random

def Question37():
  min = int(input("What's the minimum length? "))
  special = int(input("How many special characters? "))
  num = int(input("How many numbers? "))
  
  basic_chr = "abcdefghijklmnopqrstuvwxyz"
  basic_num = "0123456789"
  basic_special = "~!@#$%^&*()_+`-={}|:\"<>?[]\;',./'"
  
  password_list = set()
  
  for index in range(special):
    count_special = random.randrange(0,len(basic_special))
    password_list.add(basic_special[count_special])
  
  
  for index in range(num):
    count_num = random.randrange(0,len(basic_num))
    password_list.add(basic_num[count_num])  
  
  
  for index in range(min-num-special):
    count_chr = random.randrange(0,len(basic_chr))
    password_list.add(basic_chr[count_chr])  
    
  print("Your password is")  
  for index in password_list:
    print(index, end='')
  print('')
    