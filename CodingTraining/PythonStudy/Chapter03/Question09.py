import math

def Question09():
  print('What is the length of the room in meter?')
  length = int(input())
  print('What is the width of the room in meter?')
  width = int(input())
  area = length * width
  liters = math.ceil((area / 9))
  pre_context = 'You will need to purchase '
  middel_context = ' liters of paint to cover '
  post_conext = ' square meters'
  print(pre_context + str(liters) + middel_context + str(area) + post_conext)