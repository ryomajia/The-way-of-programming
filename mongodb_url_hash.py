#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import collections

mongoClient_old = pymongo.MongoClient("192.168.1.133", 27017)
db = mongoClient_old["item_styleai-shopping"]
db_list = list(db["yohobuy"].find())
url_hash_list = []

for i in db_list:
    url_hash_list.append(i["id"])
#url_hash_repetition_list = [item for item, count in collections.Counter(url_hash_list).items() if count > 1]
print len(url_hash_list)
print len(set(url_hash_list))
#print len(url_hash_repetition_list)
#print url_hash_repetition_list[0]
#for i in url_hash_repetition_list:
 #   print list(db["yohobuy"].find({"url_hash": i}))
