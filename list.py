#!/usr/bin/env python3

class ClassList(object):

    def __init__(self,*args):
        self.mlist = []
        self.__appendmany(*args)

    def __appendmany(self, *args):
        for i in args:
            self.mlist.append(i)

    def __str__(self):
        return str(self.mlist)

    def __getitem__(self, key):
        return self.mlist[key]

    def __setitem__(self, key, value):
         self.mlist[key]=value

    def myappend(self, ob):
        self.mlist.append(ob)

    def myclear(self):
        self.mlist=[]

    def mycount(self,ob):
        c=0
        for i in self.mlist:
            if i==ob:
                c+=1
        self.mlist=c

    def myremove(self,ob):
        k=[]
        for i in self.mlist:
            if i!=ob:
                k.append(i)
        self.mlist=k

    def myreverse(self):
        self.mlist=self.mlist[::-1]



def main():
	a=ClassList(1,3,79,56,10,2)
	a.myremove(2)
	print(a)

if __name__=="__main__":
	main()
