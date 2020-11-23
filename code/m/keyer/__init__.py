# Part of RedFile
#
# Author: Outflank B.V. / Mark Bergman / @xychix
#
# License : BSD3
import shelve
import codecs
import os
from hashlib import md5
import helper

### CONSTANTS
secret = "YOURSECRETHERE"
fileTable = { -1 : "error.txt",
              0 : "default.txt",
              1 : "proxy.txt",
              2 : "payload.txt"}

for i in range(3,5):
    fileTable[i] = "payload2.txt"

for i in range(5,99):
    fileTable[i] = "monkey.jpg"

## usage:
# http://127.0.0.1:18080/keyer/7103f096074271321c6cebd743ac8d9b5b6b52d65f7e16a8a08a33570275a750/test
# basic url or redirector.....................|modname|key.....|notused
class f():
  def __init__(self,key,h,req={}):
    self.key = key.encode("utf-8",'ignore')
    cwd = os.path.dirname(os.path.realpath(__file__))
    self.folder = cwd
    self.scoreRes = self.score()
    if self.scoreRes in fileTable:
        self.returnFile = fileTable[self.scoreRes]
    else:
        self.returnFile = fileTable[0]

  def score(self):
    d = shelve.open('%s/data.shelve'%self.folder)
    if len(self.key) != 64:
      return(False)
    stok = self.key[:32]
    tok = self.key[32:]
    chk = "%s%s"%(secret,tok)
    if stok == md5(chk.encode('utf-8')).hexdigest():
      #the key is valid
      if not self.key in d.has_key:
        #the key is new
        d[self.key] = 1
        return(1)
      else:
        d[self.key] += 1
        return(d[self.key])
    return(-1)

  def fileContent(self):
    ff = self.returnFile
    with open("%s/%s"%(self.folder,ff), 'rb') as f:
      return f.read()

  def fileType(self):
    ff = self.returnFile.split('.')[1]
    return(helper.getContentType(ff))

def newKey():
  from hashlib import md5
  from time import time
  strTime = str(time()).encode('utf-8')
  tok = md5(strTime).hexdigest()
  chk = "%s%s"%(secret,tok)
  stok = md5(chk.encode('utf-8')).hexdigest()
  key = "%s%s"%(stok,tok)
  return(key)
