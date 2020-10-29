import wget
from zipfile import ZipFile
import os

url ='https://insert-usernamehere.github.io/dblink.txt'
wget.download(url, 'dblink.txt')

f=open("dblink.txt", "r")
db = f.read()


wget.download(db, 'AOmaster.zip')
zf = ZipFile('AOmaster.zip', 'r')
zf.extractall('')
zf.close()
f.close
if os.path.exists("dblink.txt"):
  os.remove("dblink.txt")
else:
  pass
if os.path.exists("AOmaster.zip"):
  os.remove("AOmaster.zip")
else:
  pass
if os.path.exists("base/serverlist.txt"):
  os.remove("base/serverlist.txt")
else:
  pass
url = 'https://insert-usernamehere.github.io/serverlist.txt'
wget.download(url, 'base/serverlist.txt')
os.startfile("Attorney_Online.exe")
