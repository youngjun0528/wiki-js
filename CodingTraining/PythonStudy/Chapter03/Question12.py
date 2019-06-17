
def Question12():
  print('Enter the principal : ')
  principal = int(input())
  print('the rate of interest : ')
  rate = float(input())
  print('Enter the number of years : ')
  years = int(input())
  total = principal*(1+years*rate/100)
  print('After %s years at $%f, the investmeet will be worth $%f' % (years, rate, total))
  
  