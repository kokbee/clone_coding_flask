# -*- coding:utf-8 -*-
# code : kokbee

from flask import Flask, jsonify, request, escape
import datetime

from core import database as db

app = Flask(__name__)

nowdatetime = datetime.datetime.now()
nowdate = nowdatetime.strftime("%Y-%m-%d %H:%M:%S")

@app.route('/')
@app.route('/index')
def index():
    return 'Clone Flask'

@app.route('/api/years', methods=['GET', 'POST'])
def years():
    '''
    년도의 범위 API
    '''

    years = []
    # get -3 ~ +3
    if request.method == "GET":
        for y in range(nowdatetime.year-3, nowdatetime.year+3):
            if not y in years:
                years.append(str(y))
        
        data = {}
        data.update({"data" : years})

        return jsonify(data)
    # post
    elif request.method == "POST":
        postData = request.get_json()
        start = postData['Start']
        end = postData['End']
        for y in range(start, end):
            if not y in years:
                years.append(str(y))

        data = {}
        data.update({"data" : years})

        return jsonify(data)


@app.route('/api/date', methods=['GET'])
def dates():
    '''
    날짜 범위 API
    '''

    beforeDate = nowdatetime - datetime.timedelta(days=7)
    afterDate = nowdatetime - datetime.timedelta(days=1)

    reqStart = request.args.get("Start")
    reqEnd = request.args.get("End")

    # 값이 있을경우
    if reqStart and reqEnd:
        startDate = datetime.datetime.strptime(str(reqStart),"%Y-%m-%d").date()
        endDate =datetime.datetime.strptime(str(reqEnd),"%Y-%m-%d").date()
    else:
        startDate = beforeDate.date()
        endDate = afterDate.date()
    
    dates = []
    sumDate = endDate - startDate
    for idx in range(sumDate.days +1):
        mDate = endDate - datetime.timedelta(days=idx)
        date = mDate.strftime("%Y-%m-%d")
        if not date in dates:
            dates.append(date)

    data = {}
    data.update({"date" : sorted(dates)})
    data.update({"range" : len(dates)})

    return jsonify(data)


@app.route('/api/user', methods=['GET'])
def user():
    '''
    유저 API
    '''

    reqUser = request.args.get("User")

    cursor = db.User(db="address", collection="users",userid=reqUser)
    data = cursor.getUser()
    close = cursor.close()

    return jsonify(data)