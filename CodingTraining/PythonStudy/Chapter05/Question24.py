
def Question24():
  print("Enter two strings and I'll tell you if they are anagram:")
  first = input("Enter the first string : ")
  second = input("Enter the second string : ")
  
  if is_anagram(first, second):
      print("{0:s} and {1:s} are anagram.".format(first, second))
  else:
    print("{0:s} and {1:s} are not anagram.".format(first, second))
  
  
def is_anagram(first, second):
  check = []
  k = 0
  if len(first) == len(second):
    for i in first:
      check.append(False)
      for j in second:
        if i == j:
          check[k] = True
      k = k + 1
    if(check.count(False) > 0):
      return False
    else:
      return True
  else:
    return False