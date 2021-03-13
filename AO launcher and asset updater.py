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
  try:
      if os.path.exists("base"):
        pass
      else:
        os.mkdir("base")
      if os.path.exists("base/characters"):
        pass
      else:
        os.mkdir("base/characters")
      wget.download('http://fierce-push.auto.playit.gg:53368/characters.zip', 'characters.zip')
      zf = ZipFile('characters.zip', 'r')
      zf.extractall('base/characters')
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
  except Exception:
        T.delete(0, tkinter.END)
        T.insert(0, "oh no! an error occoured this might be due to the server being down please wait 5 minutes and try again. DEBUG INFO: exception on process DLCHR")
def DLCORT():
  T.delete(0, tkinter.END)
  T.insert(0, "now downloading courtrooms please wait")
  try:
      if os.path.exists("base"):
        pass
      else:
        os.mkdir("base")
      if os.path.exists("base/background"):
        pass
      else:
        os.mkdir("base/background")
      wget.download('http://fierce-push.auto.playit.gg:53368/courtrooms.zip', 'courtrooms.zip')
      zf = ZipFile('courtrooms.zip', 'r')
      zf.extractall('base/background')
      zf.close()
      if os.path.exists("cortdblink.txt"):
        os.remove("cortdblink.txt")
      else:
        pass
      if os.path.exists("courtrooms.zip"):
        os.remove("courtrooms.zip")
      else:
        pass
      T.delete(0, tkinter.END)
      T.insert(0, "Courtroom downloading finished")
  except Exception:
        T.delete(0, tkinter.END)
        T.insert(0, "oh no! an error occoured this might be due to the server being down please wait 5 minutes and try again. DEBUG INFO: exception on process DLCORT")
def DLSOU():
  if os.path.exists("base"):
    pass
  else:
    os.mkdir("base")
  if os.path.exists("base/sounds"):
    pass
  else:
    os.mkdir("base/sounds")
  T.delete(0, tkinter.END)
  T.insert(0, "now downloading sounds please wait")
  try:
      wget.download('http://fierce-push.auto.playit.gg:53368/sounds.zip', 'sounds.zip')
      zf = ZipFile('sounds.zip', 'r')
      zf.extractall('base/sounds')
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
  except BaseException:
      T.delete(0, tkinter.END)
      T.insert(0, "oh no! an error occoured this might be due to the server being down please wait 5 minutes and try again. DEBUG INFO: exception on process DLSOU")
def serveradd():
  if os.path.exists("base"):
    pass
  else:
    os.mkdir("base")
  T.delete(0, tkinter.END)
  T.insert(0, "now adding best bois courthouse please wait")
  try:
      if os.path.exists("base/serverlist.txt"):
        os.remove("base/serverlist.txt")
      else:
        pass
      url = 'http://fierce-push.auto.playit.gg:53368/serverlist.txt'
      wget.download(url, 'base/serverlist.txt')
      T.delete(0, tkinter.END)
      T.insert(0, "adding completed")
  except BaseException:
      T.delete(0, tkinter.END)
      T.insert(0, "oh no! an error occoured this might be due to the server being down please wait 5 minutes and try again. DEBUG INFO: exception on process SERVERADD")
def startAO():
  try:
    os.startfile("Attorney_Online.exe")
  except BaseException:
    T.delete(0, tkinter.END)
    T.insert(0, "oh no! an error occoured this might be due to AO not being in the same directory as the application. DEBUG INFO: exception on process startAO")
def startAOA():
  T.delete(0, tkinter.END)
  T.insert(0, "Doing everything please wait")
  time.sleep(97)
  try:
    os.startfile("Attorney_Online.exe")
    T.delete(0, tkinter.END)
    T.insert(0, "all downloading finished")
  except BaseException:
    T.delete(0, tkinter.END)
    T.insert(0, "oh no! an error occoured this might be due to AO not being in the same directory as the application. DEBUG INFO: exception on process startAOA")
def DLCHRB():
  global x
  x = threading.Thread(target=DLCHR)
  x.daemon = True
  x.start()
def DLCORTB():
  global z
  z = threading.Thread(target=DLCORT)
  z.daemon = True
  z.start()
def DLSOUB():
  global j
  j = threading.Thread(target=DLSOU)
  j.daemon = True
  j.start()
def serveraddB():
  global i
  i = threading.Thread(target=serveradd)
  i.daemon = True
  i.start()
def startAOB():
  global v
  v = threading.Thread(target=startAO)
  v.daemon = True
  v.start()
def ALL():
  global a1
  global a2
  global a3
  global a4
  global a5
  a1 = threading.Thread(target=DLCHR)
  a1.daemon = True
  a1.start()
  a2 = threading.Thread(target=DLSOU)
  a2.daemon = True
  a2.start()
  a3 = threading.Thread(target=serveradd)
  a3.daemon = True
  a3.start()
  a5 = threading.Thread(target=DLCORT)
  a5.daemon = True
  a5.start()
  a4 = threading.Thread(target=startAOA)
  a4.daemon = True
  a4.start()
def on_closing():
  top.destroy()
  sys.exit()

T = tkinter.Entry(top,width=50)
T.pack()

T.delete(0, tkinter.END)
T.insert(0, "Welcome to the AO launcher")
  
A = tkinter.Button(top, text ="download characters", command = DLCHRB)
L = tkinter.Button(top, text ="download courtrooms", command = DLCORTB)
B = tkinter.Button(top, text ="download sounds", command = DLSOUB)
D = tkinter.Button(top, text ="start AO", command = startAOB)
C = tkinter.Button(top, text ="add best bois courthouse server", command = serveraddB)
E = tkinter.Button(top, text ="Do it all", command = ALL)
F = tkinter.Button(top, text ="kill thread (debug)", command = on_closing)
A.pack()
L.pack()
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
