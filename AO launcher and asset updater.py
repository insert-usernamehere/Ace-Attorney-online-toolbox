import wget
from zipfile import ZipFile
import os
import tkinter
import threading
import sys
import time


top = tkinter.Tk()

def DLCHR():
  T.delete(0, tkinter.END)
  T.insert(0, "now downloading characters please wait")
  if os.path.exists("base"):
    pass
  else:
    os.mkdir("base")
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
  T.delete(0, tkinter.END)
  T.insert(0, "Character downloading finished")
def DLSOU():
  if os.path.exists("base"):
    pass
  else:
    os.mkdir("base")
  T.delete(0, tkinter.END)
  T.insert(0, "now downloading sounds please wait")
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
  T.delete(0, tkinter.END)
  T.insert(0, "Sound downloading finished")
def serveradd():
  if os.path.exists("base"):
    pass
  else:
    os.mkdir("base")
  T.delete(0, tkinter.END)
  T.insert(0, "now adding best bois courthouse please wait")
  if os.path.exists("base/serverlist.txt"):
    os.remove("base/serverlist.txt")
  else:
    pass
  url = 'https://insert-usernamehere.github.io/serverlist.txt'
  wget.download(url, 'base/serverlist.txt')
  T.delete(0, tkinter.END)
  T.insert(0, "adding completed")
def startAO():
  os.startfile("Attorney_Online.exe")
def DLCHRB():
  global x
  x = threading.Thread(target=DLCHR)
  x.daemon = True
  x.start()
def DLSOUB():
  global x
  x = threading.Thread(target=DLSOU)
  x.daemon = True
  x.start()
def serveraddB():
  global x
  x = threading.Thread(target=serveradd)
  x.daemon = True
  x.start()
def startAOB():
  global x
  x = threading.Thread(target=startAO)
  x.daemon = True
  x.start()
def ALL():
  global x
  x = threading.Thread(target=DLCHR)
  x.daemon = True
  x.start()
  x = threading.Thread(target=DLSOU)
  x.daemon = True
  x.start()
  x = threading.Thread(target=serveradd)
  x.daemon = True
  x.start()
  T.delete(0, tkinter.END)
  T.insert(0, "Doing everything please wait")
  time.sleep(60)
  x = threading.Thread(target=startAO)
  x.daemon = True
  x.start()
  T.delete(0, tkinter.END)
  T.insert(0, "all downloading finished")
def on_closing():
  top.destroy()
  sys.exit()

T = tkinter.Entry(top,width=50)
T.pack()

T.delete(0, tkinter.END)
T.insert(0, "Welcome to the AO launcher")
  
A = tkinter.Button(top, text ="download characters", command = DLCHRB)
B = tkinter.Button(top, text ="download sounds", command = DLSOUB)
D = tkinter.Button(top, text ="start AO", command = startAOB)
C = tkinter.Button(top, text ="add best bois courthouse server", command = serveraddB)
E = tkinter.Button(top, text ="Do it all", command = ALL)
F = tkinter.Button(top, text ="kill thread (debug)", command = on_closing)
A.pack()
B.pack()
C.pack()
D.pack()
E.pack()
T.pack()
top.winfo_toplevel().title("AO launcher")
top.geometry("350x350")
top.protocol("WM_DELETE_WINDOW", on_closing)
top.mainloop()
sys.exit()
