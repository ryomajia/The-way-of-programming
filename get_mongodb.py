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
def styleai_shopping_image_list():
    coll = _create_mongodb_client('pl-prod-001.chinacloudapp.cn', 53493, 'image_styleai-shopping', 'raw')
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

def create_repetition_elements_list(list_name):
    import collections
    print [item for item, count in collections.Counter(list_name).items() if count > 1]

def create_without_repetition_elements_list(list_name):
    print len(set(list_name))

infs_styleai_shopping_image_list = [x for x in styleai_shopping_image_list()]


#blob_image_list = []
#infs_image_list = []
##infs_only_list = []
md5_list = []
sha1_list = []
id_list = []
other_list = []
md5_id_list = []
sha1_id_list = []
for x in infs_styleai_shopping_image_list:
    #infs_image_list.append(x['sha1'])
    id_list.append(x['id'])
    md5_list.append(x['md5'])
    sha1_list.append(x['sha1'])
for x in id_list:
    if x not in sha1_list:
        if x in md5_list:
            md5_id_list.append(x)
        else:
            other_list.append(x)

print len(md5_id_list)
print len(other_list)
print md5_id_list
print other_list
#for x in _enumerate_blob('styleai-shopping-img-raw'):
#    blob_image_list.append(x[0])

#for x in blob_image_list:
#    if x not in infs_image_list:
#        infs_only_list.append(x)

#print len(infs_image_list)
#print len(blob_image_list)
#create_repetition_elements_list(infs_image_list)
#create_without_repetition_elements_list(infs_image_list)

#print infs_only_list

