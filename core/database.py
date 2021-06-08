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
        print (kwargs)
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