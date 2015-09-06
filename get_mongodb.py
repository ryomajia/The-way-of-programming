__author__ = 'juliajia'

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo

from azure.storage.blob import BlobService


def _create_mongodb_client(host, port, db_name, collection_name):
    client = pymongo.MongoClient(host, port)
    db = client[db_name]
    collection = db[collection_name]
    return collection
def tmall():
    coll = _create_mongodb_client('pl-prod-001.chinacloudapp.cn', 53493, 'item_styleai-shopping', 'tmall')
    cursor = coll.find()
    dst = next(cursor, None)
    while dst is not None:
        yield dst
        dst = next(cursor, None)
    cursor.close()


def yohobuy():
    coll = _create_mongodb_client('pl-prod-001.chinacloudapp.cn', 53493, 'item_styleai-shopping', 'yohobuy')
    cursor = coll.find()
    dst = next(cursor, None)
    while dst is not None:
        yield dst
        dst = next(cursor, None)
    cursor.close()

def _enumerate_blob_container(store, container_name):
    next_marker = None

    while True:
        try:
            blobs = None
            blobs = store.list_blobs(container_name, maxresults=5000, marker=next_marker)
            for blob in blobs:
                yield blob
        except:
            pass

        if blobs is not None:
            next_marker = blobs.next_marker
            if next_marker is None or next_marker is u'':
                break

def _enumerate_blob(container_name):
    store = BlobService(
        host_base='.blob.core.chinacloudapi.cn',
        account_name='pbgcnnorth',
        account_key="aObY6B98AcrdOm1INmE7KjNRG3uxddQyiMlUfELfN8L5xh2cJYJ7GC1CzTsH+ZtFoqsE8u4YNWQdeMRUGPPxEQ==",
    )

    for blob in _enumerate_blob_container(store, container_name):
        id = blob.name.split('.')[0]
        url = 'https://pbgcnnorth.blob.core.chinacloudapi.cn/' + container_name + '/' + blob.name
        yield (id, blob.name, url)


pics = {id: None for id, name, url in _enumerate_blob('styleai-shopping-webcache')}
infs_tmall = [x for x in tmall()]
infs_yohobuy = [x for x in yohobuy()]
#for i in infs :
#    print i['domain']

print len(infs_tmall) + len(infs_yohobuy)

print len(pics)