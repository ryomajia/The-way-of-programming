__author__ = 'juliajia'

#!/usr/bin/env python




class stack:

    errormessage = 'error'
    def __init__(self, stack_name, num = 0):
        self.stack_name = []
        self.n = num
    def pop(self):
        if self.stack_name == []:
            return self.errormessage
        else:
            a = self.stack_name.pop()
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

