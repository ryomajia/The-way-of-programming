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
db_images = mongoClient['image_styleai-shopping']

def toJson(data):
    return json.dumps(data,default=json_util.default)





def find_item(item_name):
    if request.method == "GET":
        count = db[item_name].find().count()
        item_id = randint(0,count - 1)
        results = db[item_name].find().limit(1).skip(item_id)
        json_results=[]
        for result in results:
            json_results.append(result)
    return toJson(json_results)


def json_dict(item_name):
    json_dict = json.loads(find_item(item_name))[0]
    return json_dict

def blob_url(list_name,item_name):
    blob_url_list = []
    for url in list_name:
        images = db_images[item_name].find({"url":url})
        print url.split(".")
        for image in images:
            blob_url = "https://pbgcnnorth.blob.core.chinacloudapi.cn/styleai-shopping-img-raw/" + image["sha1"] +\
                       "." + url.split(".")[4]
            blob_url_list.append(blob_url)
    return blob_url_list

@app.route('/')
@app.route('/index')

def index():
    user = {'nickname':'Miguel'}
    return render_template("index.html",title = 'Home',user = user)


@app.route('/tmall',methods=['GET'])

def item_tmall_json(item_name = "tmall"):
    item_dict = json_dict(item_name)
    item_keys_list = item_dict.keys()
    return render_template("json.html",json_key = item_keys_list,json_dict = item_dict)

@app.route('/yohobuy',methods=['GET'])

def item_yohobuy_json(item_name = "yohobuy"):
    item_dict = json_dict(item_name)
    item_keys_list = item_dict.keys()
    prop_images_url_list = []
    gallery_images_url_list = []
    extra_images_url_list = []
    for key in item_keys_list:
        if key == "prop_images":
            url_list = item_dict[key]
            for url in url_list:
                prop_images_url_list.append(url)
        elif key == "gallery_images":
            url_list = item_dict[key]
            for url in url_list:
                gallery_images_url_list.append(url)
        elif key == "extra_images":
            url_list = item_dict[key]
            for url in url_list:
                extra_images_url_list.append(url)
    blob_url_list = blob_url(extra_images_url_list,"raw")
    prop_length = len(prop_images_url_list)
    gallery_length = len(gallery_images_url_list)
    extra_length = len(extra_images_url_list)
    return render_template("json.html",json_key = item_keys_list,json_dict = item_dict,prop_list = prop_images_url_list,
                           gallery_list = gallery_images_url_list,extra_list = blob_url_list,
                           prop_length = prop_length,gallery_length = gallery_length,extra_length = extra_length)


