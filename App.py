# -*- coding:utf-8 -*-
# code : kokbee

import sys,os,re
from flask import Flask

app = Flask(__name__)
 
@app.route('/')
@app.route('/index')
def index():
    return 'Clone Flask'