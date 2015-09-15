#!/usr/bin/env python
import os
process = os.popen("ps aux | grep /usr/bin/python | grep run.py").read()
process_list = process.split(' ')
for i in process_list:
    if i == "":
        process_list.remove(i)
os.system("kill -9 %s" % process_list[1])