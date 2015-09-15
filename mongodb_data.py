#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
mongoClient_old = pymongo.MongoClient("192.168.1.133",27017)
mongoClient_new = pymongo.MongoClient("192.168.1.133",28017)
db_old = mongoClient_old['item_styleai-shopping']
db_list = list(db_old["yohobuy"].find())
db_new = mongoClient_new['item_styleai-shopping']
db_new_list = list(db_new["yohobuy"].find())
db_new_hash_list = []
for i in db_new_list:
    db_new_hash_list.append(i["url_hash"])
for i in db_list:
    if i["url_hash"] not in db_new_hash_list:
        db_new["yohobuy"].insert(i)
print len(db_new_list)


