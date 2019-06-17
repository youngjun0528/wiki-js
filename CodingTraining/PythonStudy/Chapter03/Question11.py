
def Question11():
  print('How many Euros are you exchanging?')
  euros = int(input())
  print('What is the exchange rate?')
  rate = float(input())
  dollars = round(euros * rate / 100, 2)
  print(str(euros) + ' Euros at an exchange rate of ' + str(rate) + ' is '+ str(dollars) + ' dollars')