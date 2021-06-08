# -*- coding:utf-8 -*-
# code : kokbee

import pymongo

class MongoDB:
    def __init__(self):
        self.connect = pymongo.MongoClient("localhost:27017")

    def __str__(self):
        return "Running Database.."
    
    def close(self):
        return self.connect.close()



class User(MongoDB):
    '''
    Users Database
    '''
    def __init__(self, **kwargs):
        # 부모 접근 허용
        super().__init__()
        self.db = self.connect[kwargs['db']]
        self.cursor = self.db[kwargs['collection']]
        self.userid = kwargs['userid']

    def getUser(self):
        result =  self.cursor.find_one({
            "usernum":self.userid
        },{
            "_id":0
        })
        if not result:
            return None
        
        return result


class Folder(MongoDB):
    '''
    Folder Database
    '''
    def __init__(self, **kwargs):
        # 부모 접근 허용
        super().__init__()
        self.db = self.connect[kwargs['db']]
        self.cursor = self.db[kwargs['collection']]
        self.name = kwargs['name']

    def getFolder(self):
        result =  self.cursor.find_one({
            "folder":self.name
        },{
            "_id":0
        })
        if not result:
            return None
        
        return result


class Log(MongoDB):
    '''
    Log Database
    '''
    def __init__(self, **kwargs):
        # 부모 접근 허용
        super().__init__()
        self.db = self.connect[kwargs['db']]
        self.cursor = self.db[kwargs['collection']]
        self.start = kwargs['start']
        self.end = kwargs['end']

    def getLogs(self):
        results = self.cursor.find({
            "inputdate": {"$gte": self.start, "$lte": self.end}
        },{"_id":0})

        if not results:
            return None
        
        return list(results)