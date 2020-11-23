#!/usr/bin/env python
# Part of RedFile
#
# Author: Outflank B.V. / Mark Bergman / @xychix
#
# License : BSD3
from flask import Flask, abort
import werkzeug.exceptions as ex
from flask import make_response, send_file
import random
import jinja2
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from io import BytesIO
import importlib
from flask import request
from flask_cors import CORS
import os,sys
import logging
import traceback
#import sys

### add CWD to path
#cwd = os.path.dirname(os.path.realpath(__file__))
#sys.path.insert(0, cwd)

#### logging test
toFile = logging.FileHandler('log.log')
toStderr = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
toFile.setFormatter(formatter)
toStderr.setFormatter(formatter)
###


app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
CORS(app)
app.logger.addHandler(toFile) 
app.logger.addHandler(toStderr)

#sys.path.append('/code/m/')

@app.route('/<hash>/<key>/<filename>')
def genFile(hash,key,filename):
    try:
        app.logger.debug("importing m.%s"%hash)
        m  = importlib.import_module('m.%s'%hash)
    except Exception as e:
        app.logger.error('Module %s not found'%(hash))
        app.logger.error('Went looking in %s'%sys.path)
        stackTrace = traceback.format_exc()
        app.logger.exception(e)
        abort(404)
    r = m.f(key,hash,request)
    response = make_response(r.fileContent())
    response.headers['Content-Type'] = r.fileType()
    return response

@app.route('/static/')
def staticlst():
    from os import walk
    lst = []
    for (a,b,c) in walk('static'):
        lst.extend(c)
        lst.extend(b)
        html="<html>"
        for i in lst:
            html += "<a href='static/%s'>%s</a><br>"%(i,i)
        html += "</html>"
        return(html)

if __name__ == '__main__':
    #app.run(host='0.0.0.0',port=18081)
    app.run(host='0.0.0.0',port=8000,debug=True)
