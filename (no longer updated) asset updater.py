import wget
from zipfile import ZipFile
import os

url ='https://insert-usernamehere.github.io/soudblink.txt'
wget.download(url, 'soudblink.txt')

f=open("soudblink.txt", "r")
db = f.read()
f.close()

wget.download(db, 'sounds.zip')
zf = ZipFile('sounds.zip', 'r')
zf.extractall('base')
zf.close()
if os.path.exists("soudblink.txt"):
  os.remove("soudblink.txt")
else:
  pass
if os.path.exists("sounds.zip"):
  os.remove("sounds.zip")
else:
  pass
url ='https://insert-usernamehere.github.io/chrdblink.txt'
wget.download(url, 'chrdblink.txt')

f=open("chrdblink.txt", "r")
db = f.read()
f.close()

wget.download(db, 'characters.zip')
zf = ZipFile('characters.zip', 'r')
zf.extractall('base')
zf.close()
if os.path.exists("chrdblink.txt"):
  os.remove("chrdblink.txt")
else:
  pass
if os.path.exists("characters.zip"):
  os.remove("characters.zip")
else:
  pass
