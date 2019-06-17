import os

def Question45():
  try:
    read_file = open(os.getcwd()+"/Chapter08/Question45_example.txt", 'r')
    file_str = read_file.read()
    read_file.close()
  
    print("Input file string : ")
    print(file_str, end="\n\n")
    
    count = file_str.count("utilize")
    print("Input file \"use\" string count : {0:d}".format(count), end="\n\n")
    
    print("Output file string : ")
    re_file_str = file_str.replace("utilize", "use")
    print(re_file_str)
  
    write_file = open(os.getcwd()+"/Chapter08/Question45_result.txt", 'w')
    write_file.write(re_file_str)  
    write_file.close()
  except IOError as err:
    print(err)
  
  