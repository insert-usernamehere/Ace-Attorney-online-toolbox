import wget
from zipfile import ZipFile
import os

if os.path.exists("base/serverlist.txt"):
  os.remove("base/serverlist.txt")
else:
  pass
url = 'https://insert-usernamehere.github.io/severlist.txt'
wget.download(url, 'base/serverlist.txt')
os.startfile("Attorney_Online.exe")
