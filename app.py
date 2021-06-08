# -*- coding:utf-8 -*-
# code : kokbee

from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)
 
@app.route('/')
@app.route('/index')
def index():
    return 'Clone Flask'

@app.route("/api/years", methods=['GET', 'POST'])
def years():
    '''
    년도의 범위 API
    '''
    nowdatetime = datetime.datetime.now()
    nowdate = nowdatetime.strftime("%Y-%m-%d %H:%M:%S")

    years = []
    # get -3 ~ +3
    if request.method == "GET":
        for y in range(nowdatetime.year-3, nowdatetime.year+3):
            if not y in years:
                years.append(str(y))
    # post
    elif request.method == "POST":
        postData = request.get_data()
        print (postData)
        start = postData['Start']
        end = postData['End']
        for y in range(start, end):
            if not y in years:
                years.append(str(y))

    data = {}
    data.update({"data" : years})

    return jsonify(data)