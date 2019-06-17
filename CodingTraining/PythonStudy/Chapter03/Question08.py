
def Question08():
  print('How many people?')
  people = int(input())
  print('How many pizzas do you have?')
  pizza = int(input())
  print('How many pieces are in a pizza?')
  pieces = int(input())
  print(str(people) + ' people with ' + str(pizza) + ' pizzas')
  each_pieces = pizza * pieces / people
  print('Each person gets ' + str(each_pieces) + ' pieces of pizza.')
  leave_pieces = pizza * pieces % people
  print('There are ' + str(leave_pieces) + ' left over pieces')