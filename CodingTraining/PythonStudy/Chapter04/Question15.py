
def Question15():
  collect = "abc$123"
  print("What is the password")
  password = input()
  if password == collect:
    print("Welcome!")
  else:
    print("That password is incorrect.")