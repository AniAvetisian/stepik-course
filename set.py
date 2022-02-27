#!/usr/bin/env python3

from random import randint
class Myset:
   def __init__(self):
       self.set=[]

   def __str__(self):
       return str(self.set).replace('[', '{').replace(']', '}')

   def add(self,obj):
       if obj not in self.set:
           self.set.append(obj)

   def difference(self,x):
        c=[]
        for i in self.set:
            if i not in x:
                c.append(i)
        return c
   def pop(self):
     del (self.set[randint(0,len(self.set)-1)])

   def  isdisjoint(self):
       c=[]
       for i in self.set:
           if i not in x:
               return True
           else:
               return False
