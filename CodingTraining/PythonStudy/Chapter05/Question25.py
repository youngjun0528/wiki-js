#http://whatisthenext.tistory.com/116
import re

def Question25():
  password = input("Enter the password : ")
  vali = password_validator(password)
  print("The password {0:s} is a {1:s} password.".format(password, vali))
  
def password_validator(password):
  if len(password) < 8:
    if password.isdigit():
      return 'very week'
    elif password.isalpha():
      return 'week'
    else:
      return 'wrong'
  else:
    if not(password.isdigit()) and not(password.isalpha()) and password.isalnum():
      return 'strong'
    elif not(password.isdigit()) and not(password.isalpha()) and not(password.isalnum()):
      p = re.compile('[^a-zA-Z0-9]+')
      m = p.search(password) 
      if m is not None:
        c = re.sub(p, "", password)
        print(c)
        if c.isalnum():
          return 'very strong'
        else:
          return 'wrong'  
      else:
        return 'wrong'  
    else:
      return 'wrong'  