import json
import urllib.request

def Question47():
  url = "http://api.open-notify.org/astros.json"
  text_data = urllib.request.urlopen(url).read().decode('utf-8')
  dict = json.loads(text_data)
  print("There are {0:d} people in space right now : ".format(len(dict['people'])))
  print("Name | Craft")
  print("---------------------------------------------")
  for index in dict['people']:
    print("{0:s} | {1:s}".format(index['name'], index['craft']))
   