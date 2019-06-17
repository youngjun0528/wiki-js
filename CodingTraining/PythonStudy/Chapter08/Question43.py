import os

def Question43():
  site_name = input("Site name : ")
  author = input("Author : ")
  javascript = input("Do you want a folder for javascript? ")
  css = input("Do you want a folder for CSS? ")
  
  try:
    if not os.path.isdir(os.getcwd()+"/Chapter08/"+site_name+"/"):
      os.mkdir(os.getcwd()+"/Chapter08/"+site_name+"/")
    print("Created ./{0:s}".format(site_name))
    
    write_file = open(os.getcwd()+"/Chapter08/"+site_name+"/index.html", 'w')
    write_file.write("<title>"+site_name+"</title><meta>"+author+"</meta>")
    write_file.close()
    print("Created ./{0:s}/index.html".format(site_name))
    
    if javascript.lower() == "y":  
      if not os.path.isdir(os.getcwd()+"/Chapter08/"+site_name+"/js/"):
        os.mkdir(os.getcwd()+"/Chapter08/"+site_name+"/js/")
      write_file = open(os.getcwd()+"/Chapter08/"+site_name+"/js/index.js", 'w')
      write_file.close()
      print("Created ./{0:s}/js/".format(site_name))
        
    if css.lower() == "y":
      if not os.path.isdir(os.getcwd()+"/Chapter08/"+site_name+"/css/"):
        os.mkdir(os.getcwd()+"/Chapter08/"+site_name+"/css/")
      write_file = open(os.getcwd()+"/Chapter08/"+site_name+"/css/index.css", 'w')
      write_file.close()
      print("Created ./{0:s}/css/".format(site_name))
  except IOError as err:
    print(err)
      