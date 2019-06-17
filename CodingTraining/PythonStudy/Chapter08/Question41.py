import os

def Question41():
  try:
    read_file = open(os.getcwd()+"/Chapter08/Question41_example.txt", 'r')
    file_lines = read_file.readlines()
    read_file.close()
  
    file_lines.sort()
    print("Total of {0:d} names".format(len(file_lines)))
    print("---------------------------------------------")
    for index in file_lines:
      print(index.strip())
  
    write_file = open(os.getcwd()+"/Chapter08/Question41_result.txt", 'w')
    write_file.write("Total of {0:d} names\n".format(len(file_lines)))
    write_file.write("---------------------------------------------\n")
    write_file.writelines(file_lines)  
    write_file.close()
  except IOError as err:
    print(err)
  
  
  