
def Question14():
  print("What is the order amount?")
  amount = int(input())
  print("What is the state?")
  state = input()
  duty = 0
  if state == 'WI':
    duty = 5.5
    print("The subtotal is ${0:,.2f}".format(amount))
    tax = float(amount) * duty / 100
    print("The tax is ${0:.2f}".format(tax))
    amount = amount + tax
  print("The total is ${0:.2f}".format(amount))
  
  