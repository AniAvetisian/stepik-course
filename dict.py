#!/usr/bin/env python3

class DictClass(object):

    def __init__(self):
         self.mdict={}

    def __setitem__(self, key, value):
        self.mdict={key:value}

    def __str__(self):
        return str(self.mdict)
    def myclear(self):
        self.mdict= {}

    def myget(self,key):
        if key in self.mdict:
            return self.mdict[key]
    def myupdate(self, a):
        return self.mdict.update(a)
    def mydel(self,key):
        del self.mdict[key]
    def mykeys(self):
        return self.mdict.keys()
    def myvalues(self):
        return self.mdict.values()
