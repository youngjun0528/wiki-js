
def Question13():
  print('What is the principal amount: ')
  principal = int(input())
  print('What is the rate : ')
  rate = float(input())
  print('Enter the number of years : ')
  years = int(input())
  print('Enter the number of times the interest is compounded per year : ')
  times = int(input())
  total = principal*pow((1+rate/100/times), years*4)
  print('%d invested at %f%% for %d years compounded %d times per year is $%.2f' %(principal, rate, years, times, total))
  
  
  