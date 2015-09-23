from app import app
from flask import request
from flask import render_template
import json
from bson import json_util
from bson.objectid import ObjectId
from random import randint
import pymongo
import hashlib



mongoClient = pymongo.MongoClient("pl-prod-001.chinacloudapp.cn", 53493)
db = mongoClient['item_styleai-shopping']
db_image = mongoClient['image_styleai-shopping']


def toJson(data):
    return json.dumps(data, default=json_util.default)





def find_item(item_name):
    if request.method == "GET":
        count = db[item_name].find().count()
        item_id = randint(0, count - 1)
        results = db[item_name].find().skip(item_id).limit(1)
        json_results=[]
        for result in results:
            json_results.append(result)
    return toJson(json_results)

def search_item(item_name, item_ID):
    results = list(db[item_name].find({"id": item_ID}))
    return toJson(results)

def json_dict(item_name):
    json_dict = json.loads(find_item(item_name))[0]
    return json_dict

def search_dict(item_name, item_ID):
    search_item_dict = json.loads(search_item(item_name, item_ID))[0]
    return search_item_dict

def blob_url(list_name):
    blob_url_list = []
    for url in list_name:
        hash_value = hashlib.sha1(url).hexdigest()
        blob_url = "https://pbgcnnorth.blob.core.chinacloudapi.cn/styleai-shopping-img-raw/" + hash_value + ".jpg"
        blob_url_list.append(blob_url)
    return blob_url_list




@app.route('/')
@app.route('/index')
def index():
    #return render_template("index.html",sources = item_list)
    from flask import redirect, url_for
    return redirect(url_for('item', item_name='yohobuy'))


@app.route('/<string:item_name>', methods=['GET', "POST"])
def item(item_name):
    if request.method == "POST":
        ID = request.form.get("item_id")
        search_item_name = request.form.get("item_name")
        search_item_dict = search_dict(search_item_name, ID)
        search_item_keys_list = search_item_dict.keys()
        prop_images_url_list = []
        gallery_images_url_list = []
        extra_images_url_list = []
        for key in search_item_keys_list:
            if key == "prop_images":
                url_list = search_item_dict[key]
                for url in url_list:
                    prop_images_url_list.append(url)
            elif key == "gallery_images":
                url_list = search_item_dict[key]
                for url in url_list:
                    gallery_images_url_list.append(url)
            elif key == "extra_images":
                url_list = search_item_dict[key]
                for url in url_list:
                    extra_images_url_list.append(url)
        blob_url_list = blob_url(extra_images_url_list)
        prop_blob_url_list = []
        for i in prop_images_url_list:
            hash_value = hashlib.sha1(i).hexdigest()
            url = "https://pbgcnnorth.blob.core.chinacloudapi.cn/styleai-shopping-img-raw/" + \
                  hash_value + ".jpg"
            prop_blob_url_list.append(url)
        gallery_blob_url_list = blob_url(gallery_images_url_list)
        prop_length = len(prop_images_url_list)
        gallery_length = len(gallery_blob_url_list)
        extra_length = len(blob_url_list)
        return render_template("search.html", json_key = search_item_keys_list, json_dict = search_item_dict,
                               prop_list = prop_blob_url_list, gallery_list = gallery_blob_url_list,
                               extra_list = blob_url_list, prop_length = prop_length, gallery_length = gallery_length,
                               extra_length = extra_length)
    else:
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
                  hash_value + ".jpg"
            prop_blob_url_list.append(url)
        gallery_blob_url_list = blob_url(gallery_images_url_list)
        prop_length = len(prop_images_url_list)
        gallery_length = len(gallery_blob_url_list)
        extra_length = len(blob_url_list)
        return render_template("json.html", sources = ["tmall", "yohobuy"], current_item = item_name, json_key = item_keys_list,
                               json_dict = item_dict, prop_list = prop_blob_url_list,
                           gallery_list = gallery_blob_url_list, extra_list = blob_url_list,
                           prop_length = prop_length, gallery_length = gallery_length, extra_length = extra_length)



