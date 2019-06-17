
def Question10():
  print('Price of item 1:')
  item1 = int(input())
  print('Quantity of item 1:')
  quantity1 = int(input())
  print('Price of item 2:')
  item2 = int(input())
  print('Quantity of item 2:')
  quantity2 = int(input())
  print('Price of item 3:')
  item3 = int(input())
  print('Quantity of item 3:')
  quantity3 = int(input())
  subtotal = item1*quantity1 + item2*quantity2 + item3*quantity3
  print('Subtotal: $ %.2f' %subtotal)
  tax = subtotal * 0.055
  print('Tax: $' + str(tax))
  total = subtotal + tax
  print('Total: $' + str(total))
  
  