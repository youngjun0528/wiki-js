
class Person:

  def __init__(self, first_name, last_name, position, separation_date):
    self.first_name = first_name
    self.last_name = last_name
    self.position = position
    self.separation_date = separation_date

  def showInfo(self):
    print("{0:>20s}| {1:>20s}| {2:>10s}".format(self.first_name +" "+ self.last_name, self.position, self.separation_date))


def Question40():
  person1 = Person("John", "Johnson", "Manager", "2016-12-31")
  person2 = Person("Tou", "Xiong", "Software Engineer", "2016-10-15")
  person3 = Person("Michaela", "Michaelson", "District Manager", "2015-12-19")
  person4 = Person("Jake", "Jacobson", "Programmer", "")
  person5 = Person("Jacquelyn", "Jackson", "DBA", "")
  person6 = Person("Sally", "Weber", "Web Developer", "2015-12-18")
  
  person_list = [person1, person2, person3, person4, person5, person6]
  
  search = input("Enter a search string : ")
  
  print("\t\tName|\t\t  Position| Separation Date")
  print("-----------------------------------------------------------")
  for index in person_list:
    name = index.first_name + " " + index.last_name
    if name.find(search) >-1:
      index.showInfo()
      