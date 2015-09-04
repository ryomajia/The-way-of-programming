__author__ = 'juliajia'

#!/usr/bin/env python

class queue:

    errormessage = 'error'
    def __init__(self, queue_name, num = 0):
        self.queue_name = []
        self.n = num
    def pop(self):
        if self.queue_name == []:
            return self.errormessage
        else:
            a = self.queue_name.pop()
            self.n = self.n - 1
        return a

    def push(self, queue_element):
        self.queue_name.insert(0,queue_element)
        self.n = self.n + 1


    def front(self):
        front_element = self.queue_name[0]
        return front_element


    def back(self):
        back_element = self.queue_name[self.n - 1]
        return back_element


    def size(self):
        count = self.n
        return count
