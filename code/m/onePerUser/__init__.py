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
import logging
import requests

### CONSTANTS
#log_host = "host.docker.internal"
log_host = False
logger = logging.getLogger("onePerUser")
fh = logging.FileHandler('onePerUser.log')
fh.setLevel(logging.INFO)
logger.addHandler(fh)

fileTable = { -1 : "error.txt"}
for i in range(2,999):
    fileTable[i] = "default.txt"

## usage:
# http://127.0.0.1:18080/onePerUser/?u=John
# http://127.0.0.1:18080/onePerUser/?u=Alice
# basic url or redirector.....................|modname|key.....|notused
class f():
  def __init__(self,module,req={}):
    self.userName = req.args.get('u')
    #self.key = key.encode("utf-8",'ignore')
    cwd = os.path.dirname(os.path.realpath(__file__))
    self.folder = cwd
    self.scoreRes = self.score()
    if self.scoreRes in fileTable:
        self.returnFile = fileTable[self.scoreRes]
    else: # likely 1, that isn't in the table.
        if os.path.isfile("%s.txt"%self.userName):
          self.returnFile = "%s.txt"%self.userName
        else:
          self.returnFile = fileTable[-1]
    if log_host:
        r =requests.get('http://%s/log/sx_ll1/?mod=%s&served=%s&userName=%s&score%s'%(log_host,module,self.returnFile,self.userName,self.scoreRes))
    logger.info('END module:%s served:%s user:%s score:%s %s'%(module,self.returnFile,self.userName,self.scoreRes,req.data))

  def score(self):
    d = shelve.open('%s/data.shelve'%self.folder)
    if not self.userName in d.keys():
      #the userName is new
      d[self.userName] = 1
      return(1)
    else:
      d[self.userName] += 1
      return(d[self.userName])
    return(-1)

  def fileContent(self):
    ff = self.returnFile
    with open("%s/%s"%(self.folder,ff), 'rb') as f:
      #return("%s %s"%(self.returnFile,self.key)) ## useful for debugging
      return f.read()

  def fileType(self):
    ff = self.returnFile.split('.')[1]
    return(helper.getContentType(ff))
