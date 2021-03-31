import wget
from zipfile import ZipFile
import os
import tkinter
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
import threading
import sys
import time


app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()
msg = QLabel('Welcome to the AO launcher')


def DLCHR():
  msg.setText('now downloading characters please wait')
  try:
      if os.path.exists("base"):
        pass
      else:
        os.mkdir("base")
      if os.path.exists("base/characters"):
        pass
      else:
        os.mkdir("base/characters")
      wget.download('http://fierce-push.auto.playit.gg:47746/characters.zip', 'characters.zip')
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
      msg.setText('Character downloading finished')
  except Exception:
        msg.setText('oh no! an error occoured this might be due to the server being down please wait 5 minutes and try again. DEBUG INFO: exception on process DLCHR')
def DLCORT():
  msg.setText('now downloading courtrooms please wait')
  try:
      if os.path.exists("base"):
        pass
      else:
        os.mkdir("base")
      if os.path.exists("base/background"):
        pass
      else:
        os.mkdir("base/background")
      wget.download('http://fierce-push.auto.playit.gg:47746/courtrooms.zip', 'courtrooms.zip')
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
      msg.setText("Courtroom downloading finished")
  except Exception:
        msg.setText("oh no! an error occoured this might be due to the server being down please wait 5 minutes and try again. DEBUG INFO: exception on process DLCORT")
def DLSOU():
  if os.path.exists("base"):
    pass
  else:
    os.mkdir("base")
  if os.path.exists("base/sounds"):
    pass
  else:
    os.mkdir("base/sounds")
  msg.setText("now downloading sounds please wait")
  try:
      wget.download('http://fierce-push.auto.playit.gg:47746/sounds.zip', 'sounds.zip')
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
      msg.setText("Sound downloading finished")
  except BaseException:
      msg.setText("oh no! an error occoured this might be due to the server being down please wait 5 minutes and try again. DEBUG INFO: exception on process DLSOU")
def serveradd():
  if os.path.exists("base"):
    pass
  else:
    os.mkdir("base")
  msg.setText("now adding best bois courthouse please wait")
  try:
      if os.path.exists("base/serverlist.txt"):
        os.remove("base/serverlist.txt")
      else:
        pass
      url = 'http://fierce-push.auto.playit.gg:47746/serverlist.txt'
      wget.download(url, 'base/serverlist.txt')
      msg.setText("adding completed")
  except BaseException:
      msg.setText("oh no! an error occoured this might be due to the server being down please wait 5 minutes and try again. DEBUG INFO: exception on process SERVERADD")
def startAO():
  try:
    os.startfile("Attorney_Online.exe")
  except BaseException:
    msg.setText("oh no! an error occoured this might be due to AO not being in the same directory as the application. DEBUG INFO: exception on process startAO")
def startAOA():
  msg.setText("Doing everything please wait")
  time.sleep(113)
  try:
    os.startfile("Attorney_Online.exe")
    msg.setText("all downloading finished")
  except BaseException:
    msg.setText("oh no! an error occoured this might be due to AO not being in the same directory as the application. DEBUG INFO: exception on process startAOA")
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



layout.addWidget(msg)

  
A = QPushButton('download characters')
A.clicked.connect(DLCHRB)
L = QPushButton('download courtrooms')
L.clicked.connect(DLCORTB)
B = QPushButton('download sounds')
B.clicked.connect(DLSOUB)
D = QPushButton('start AO')
D.clicked.connect(startAOB)
C = QPushButton('add best bois courthouse server')
C.clicked.connect(serveraddB)
E = QPushButton('Do it all')
E.clicked.connect(ALL)
layout.addWidget(A)
layout.addWidget(L)
layout.addWidget(D)
layout.addWidget(B)
layout.addWidget(C)
layout.addWidget(E)
window.setWindowTitle('AO launcher')
window.setGeometry(350, 350, 350, 350)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
