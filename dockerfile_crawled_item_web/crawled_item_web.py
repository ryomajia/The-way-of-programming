from app import app
from flask import request
from flask import render_template
import json
from bson import json_util
from bson.objectid import ObjectId
from random import randint
import pymongo
import hashlib



mongoClient = pymongo.MongoClient("192.168.1.4",27017)
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

def blob_url(list_name):
    blob_url_list = []
    for url in list_name:
        hash_value = hashlib.sha1(url).hexdigest()
        url_list = url.split(".")
        format_count = len(url_list) - 1
        blob_url = "https://pbgcnnorth.blob.core.chinacloudapi.cn/styleai-shopping-img-raw/" + hash_value +\
                       "." + url.split(".")[format_count]
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
    blob_url_list = blob_url(extra_images_url_list)
    prop_blob_url_list = []
    for i in prop_images_url_list:
        hash_value = hashlib.sha1(i).hexdigest()
        url_list = i.split("?")[0].split('.')
        format_count = len(url_list) - 1
        url = "https://pbgcnnorth.blob.core.chinacloudapi.cn/styleai-shopping-img-raw/" + \
              hash_value + "." + i.split('?')[0].split('.')[format_count]
        prop_blob_url_list.append(url)
    gallery_blob_url_list = blob_url(gallery_images_url_list)
    prop_length = len(prop_images_url_list)
    gallery_length = len(gallery_blob_url_list)
    extra_length = len(blob_url_list)
    return render_template("json.html",json_key = item_keys_list,json_dict = item_dict,prop_list = prop_blob_url_list,
                           gallery_list = gallery_blob_url_list,extra_list = blob_url_list,
                           prop_length = prop_length,gallery_length = gallery_length,extra_length = extra_length)


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
    blob_url_list = blob_url(extra_images_url_list)
    prop_blob_url_list = []
    for i in prop_images_url_list:
        hash_value = hashlib.sha1(i).hexdigest()
        url = "https://pbgcnnorth.blob.core.chinacloudapi.cn/styleai-shopping-img-raw/" + \
              hash_value + "." + i.split('?')[0].split('.')[4]
        prop_blob_url_list.append(url)

    prop_length = len(prop_images_url_list)
    gallery_length = len(gallery_images_url_list)
    extra_length = len(extra_images_url_list)
    return render_template("json.html",json_key = item_keys_list,json_dict = item_dict,prop_list = prop_blob_url_list,
                           gallery_list = gallery_images_url_list,extra_list = blob_url_list,
                           prop_length = prop_length,gallery_length = gallery_length,extra_length = extra_length)


