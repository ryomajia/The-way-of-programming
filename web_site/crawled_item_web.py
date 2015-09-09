#!flask/bin/python
from flask import Flask,request
import json
from bson import json_util
from bson.objectid import ObjectId
from random import randint
import pymongo

app = Flask(__name__)

mongoClient = pymongo.MongoClient("localhost",27017)
db = mongoClient['item_styleai-shopping']

def toJson(data):
    return json.dumps(data,default=json_util.default)

def get_item_id(collections):
    item_id_list = []
    item_list = []
    results = db[collections].find()
    for i in results:
        item_list.append(i)
    for i in item_list:
        item_id_list.append(i["_id"])
    return item_id_list

@app.route('/item/tmall/',methods=['GET'])

def find_tmall_item():
    if request.method == "GET":
        item_id_list = get_item_id("tmall")
        count = len(item_id_list)
        item_id = item_id_list[randint(0,count)]
        results = db['tmall'].find({"_id": item_id})
        json_results=[]
        for result in results:
            json_results.append(result)
        return toJson(json_results)


if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug = True)

