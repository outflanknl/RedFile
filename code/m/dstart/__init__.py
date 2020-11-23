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
import datetime
import requests

### CONSTANTS
DEBUG = True
debug_hosts = ["debug","desktop-test"]
log_host = "127.0.0.1"

fileTable = {-2 : "debug.only.txt",
             -1 : "error.txt",
              0 : "error.txt",
              1 : "leeg.txt",
              2 : "leeg.txt"}

for i in range(3,999):
    fileTable[i] = "leeg2.txt"

#for i in range(5,999):
#    fileTable[i] = "monkey.jpg"

## usage:
# http://127.0.0.1:18080/dstart/test/?name=testName
# basic url or redirector.....................|modname|key.....|notused
class f():
    def __init__(self,key,h,req={}):
        self.key = datetime.date.today().strftime("%Y%m%d")
        cwd = os.path.dirname(os.path.realpath(__file__))
        self.folder = cwd
        self.scoreRes = self.score()
        req_host = req.path.split('/')[-1][:-4][::-1]
        if self.scoreRes in fileTable:
            self.returnFile = fileTable[self.scoreRes]
        else:
            self.returnFile = fileTable[0]
        #### DEBUG PORTION
        url_append =""
        if DEBUG:
            if req_host in debug_hosts:
                self.returnFile = fileTable[-2]
                url_append = "&debugpayload=%s"%(self.returnFile)
        #### END DEBUG
        req_served = fileTable[self.scoreRes]
        #r =requests.get('http://%s/log/crl/?mod=dstart&host=%s&served=%s&key=%s&score=%s%s'%(log_host,req_host,req_served,self.key,self.scoreRes,url_append))

    def score(self):
        d = shelve.open('%s/data.shelve'%self.folder)
        if not self.key in d:
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
