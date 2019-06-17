import math

def Question07():
  print('What is the length of the room in feet?')
  length = input()
  print('What is the width of the room in feet?')
  width = input()
  print('You enterd dimenstions of ' + length + ' feet by ' + width + ' feet')
  area = int(length)*int(width)
  square = area * 0.09290304 #pow(int(length), 2)*pow(int(width), 2) * 0.09290304
  print('The area is ' + str(area) +' square feet ' + str(round(square,3)) + ' square meters')