# -*- coding:utf-8 -*-
# code : kokbee

import sys,os,re
from flask import Flask

app = Flask(__name__)

@app.route('/index', methods=['GET','POST'])
def index():
    return "Hello World"

def app():
    return app