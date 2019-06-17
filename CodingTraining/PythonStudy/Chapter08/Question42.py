import os

def Question42():
  try:
    read_file = open(os.getcwd()+"/Chapter08/Question42_example.csv", 'r')
    file_lines = read_file.readlines()
    read_file.close()
  
    sort_lines = sorted(file_lines, key=lambda file : file.split(',')[2])
    print("Last First Salary")
    print("---------------------------------------------")
    for index in sort_lines:
      last = index.strip().split(',')[0]
      first = index.strip().split(',')[1]
      salary = index.strip().split(',')[2]
      print("{0:>10s} {1:>10s} {2:>10s}".format(last, first, salary))
  except IOError as err:
    print(err)
  
  