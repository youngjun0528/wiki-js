import os

def Question46():
  try:
    read_file = open(os.getcwd()+"/Chapter08/Question46_example.txt", 'r')
    file_list = read_file.readlines()
    read_file.close()
    
    file_str_org = ""
    for index in file_list:
      file_str_org = file_str_org + " " + index.strip()
    
    file_str_list = file_str_org.strip().split(' ')
    
    str_list = {}
    
    for index in file_str_list:
      if str_list.get(index) is None:
        str_list[index] = 1
      else:
        str_list[index] = str_list[index] + 1 
        
    sort_str = sorted(str_list, key=lambda index: str_list[index], reverse=True)
    
    for index in sort_str:
      print(index + ":", end="")
      for star in range(str_list[index]):
        print("*", end="")
      print("")
    
  except IOError as err:
    print(err)