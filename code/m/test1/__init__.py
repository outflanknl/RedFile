# Part of RedFile
#
# Author: Outflank B.V. / Mark Bergman / @xychix
#
# License : BSD3
import requests,json
import helper

## usage:
# http://127.0.0.1:18080/test1/one/two
# basic url .....................|modname|key.....|notused
class f():
  def __init__(self,module,req=None):
    uaString = req.headers.get('User-Agent')
    temp = {'module':module}
    for k,v in req.headers:
        temp[str(k)] = str(v)
    temp['args'] = req.args.to_dict()
    temp['url'] = req.url
    self.auJson = json.loads(json.dumps(temp))

  def fileContent(self):
      return json.dumps(self.auJson,sort_keys=True, indent=4)

  def fileType(self):
    return(helper.getContentType('json'))
