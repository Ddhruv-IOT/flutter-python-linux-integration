#! /usr/bin/python3

import cgi
import subprocess

print("context-type: text/html")
print()

data = cgi.FieldStorage()
u_l = data.getvalue("z")

cmmd = "sudo" + u_l

try:
  output = subprocess.getoutput(cmmd)
  
  if "command not found" in output or "Error" in output:
      print("\n Falied !")
      print("Error worng command")
      print("Try again wiith correct command")
  
  else:
     print("\n")
     print(output)

except:
     print("ERROR!")
