
from datetime import datetime

def Question06():
  print('What is your current age?')
  age = input()
  print('At waht age would you like to retire?')
  retire = input()
  print('You have ' + age + 'years left util you can retire.')
  start_year = datetime.today().year
  end_year = start_year + (int(retire) - int(age))
  print('It\'s ' +str(start_year)+ ', so you can retire in '+ str(end_year))