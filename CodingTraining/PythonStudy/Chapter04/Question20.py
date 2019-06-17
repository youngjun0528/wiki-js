
def Question20():
  amount = int(input("what is the order amount ? "))
  state = input("What state do you live in ? ")
  county = input("What county do you live in ? ")
  if state.lower() == 'wisconsin':
    state_tax = amount * 0.08
    if county.lower() == 'eau':
      county_tax = 0.005
    else:
      county_tax = 0.004
    total_tax = state_tax + county_tax
    amount = amount + total_tax
    print("The state tax is ${0:.2f}".format(state_tax))
    print("The total tax is ${0:.2f}".format(total_tax))
    print("The total is ${0:.2f}".format(amount))
  elif state.lower() == 'ilinoi':
    state_tax = amount * 0.08
    total_tax = state_tax
    amount = amount + total_tax
    print("The state tax is ${0:.2f}".format(state_tax))
    print("The total tax is ${0:.2f}".format(total_tax))
    print("The total is ${0:.2f}".format(amount))
  else:
    print("The total is ${0:.2f}".format(amount))  
  
      
  