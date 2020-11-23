# Part of RedFile
#
# Author: Outflank B.V. / Mark Bergman / @xychix
#
# License : BSD3
import requests,json
import helper

## usage:
# http://127.0.0.1:18080/agent/test/test
# basic url .....................|modname|key.....|notused
class f():
  def __init__(self,key,h,req={}):
    uaString = req.headers.get('User-Agent')
    temp = {}
    for k,v in req.headers:
        temp[str(k)] = str(v)
    self.auJson = json.loads(json.dumps(temp))

  def fileContent(self):
      return json.dumps(self.auJson,sort_keys=True, indent=4)

  def fileType(self):
    return(helper.getContentType('json'))
