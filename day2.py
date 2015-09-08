__author__ = 'juliajia'

#!/usr/bin/env python




class stack:

    errormessage = 'error'
    def __init__(self,  num = 0):
        self.stack_list = []
        self.n = num
    def pop(self):
        if self.stack_list == []:
            return self.errormessage
        else:
            a = self.stack_list.pop()
            self.n = self.n - 1
        return a

    def push(self, stack_element):
        self.stack_name.append(stack_element)
        self.n = self.n + 1


    def top(self):
        top_element = self.stack_name[self.n - 1]
        return top_element

    def size(self):
        count = self.n
        return count




"""
a = stack().push("abc")
print a
b = stack().push("efg")
print b
c = stack().size()
print c
d = stack().top()
print d
print stack_list
e = stack().pop()
print e
print stack_list
"""

