import wget
from zipfile import ZipFile
import os

url = 'https://dl-web.dropbox.com/zip_download_get/AlmbzsmQFJoXMDjatWC8GPEJF9_TlpMbJRxH7wuBHwYs-VU7VugCkBJz43JrtwzWbqMgITUDPgphN1_Ram7cGlw_jHL-GuLGZflGWsUu7FQppg?_download_id=9366712886235573678541395990133492636470298964969832627960112919&_notify_domain=www.dropbox.com'
wget.download(url, 'AOmaster.zip')
zf = ZipFile('AOmaster.zip', 'r')
zf.extractall('')
zf.close()
if os.path.exists("AOmaster.zip"):
  os.remove("AOmaster.zip")
else:
  pass
