import json
import os

def Question44():
  try:
    read_file = open(os.getcwd()+"/Chapter08/Question44_example.json", 'r')
    file_lines = read_file.read()
    read_file.close()
    
    dict = json.loads(file_lines)
    
    while True:
      product = input("What is the product name ? ")
      check = False
      for index in dict['product']:
          if index['name'] == product:
            print("Name : {0:s}".format(index['name']))
            print("Price : {0:.2f}".format(index['price']))
            print("Quantity on hand : {0:d}".format(index['quantity']))
            check = True
      
      if check:
        break
      else:
        print("Sorry, that product was not found in our inventory")
  except IOError as err:
    print(err)
  