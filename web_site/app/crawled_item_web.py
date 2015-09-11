from app import app
from flask import request
from flask import render_template
import json
from bson import json_util
from bson.objectid import ObjectId
from random import randint
import pymongo



mongoClient = pymongo.MongoClient("pl-prod-001.chinacloudapp.cn",53493)
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

def find_item(item_name):
    if request.method == "GET":
        item_id_list = get_item_id(item_name)
        count = len(item_id_list) - 1
        item_id = item_id_list[randint(0,count)]
        results = db['tmall'].find({"_id": item_id})
        json_results=[]
        for result in results:
            json_results.append(result)
        return toJson(json_results)

def json_value(item_name,key_name):
    json_dict = json.loads(find_item(item_name))[0]
    return json_dict[key_name]



@app.route('/')
@app.route('/index')

def index():
    user = {'nickname':'Miguel'}
    return render_template("index.html",title = 'Home',user = user)


@app.route('/tmall',methods=['GET'])

def item_json(item_name = "tmall"):
    json__id = json_value(item_name,"_id")["$oid"]
    json_url_hash = json_value(item_name,"url_hash")
    json_review_count = json_value(item_name,"review_count")
    json_attr = json_value(item_name,"attr")
    json_title = json_value(item_name,"title")
    json_price = json_value(item_name,"price")
    json_url = json_value(item_name,"url")
    json_domain = json_value(item_name,"domain")
    json_is_off_the_market = json_value(item_name,"is_off_the_market")
    json_crawled_datetime = json_value(item_name,"crawled_datetime")
    json_sell_count = json_value(item_name,"sell_count")
    json_shop_name = json_value(item_name,"shop_name")
    json_id = json_value(item_name,"id")
    json_promote_price = json_value(item_name,"promote_price")
    json_dict = {"json__id":json__id,"json_url_hash":json_url_hash,"json_review_count":json_review_count,
                 "json_attr":json_attr,"json_title":json_title,"json_price":json_price,
                 "json_url":json_url,"json_domain":json_domain,"json_is_off_the_market":json_is_off_the_market,
                 "json_crawled_datetime":json_crawled_datetime,"json_sell_count":json_sell_count,
                 "json_shop_name":json_shop_name,"json_id":json_id,"json_promote_price":json_promote_price}
    return render_template("json.html",json_dict = json_dict)



