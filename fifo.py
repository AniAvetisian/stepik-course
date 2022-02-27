#!/usr/bin/env python3

class Myfifo:
    def __init__(self):
        self.fifo={}
        self.count=0

    def __str__(self):
        return (str(list(self.fifo.values())))
    def push(self,el):
         self.fifo[self.count]=el
         self.count+=1
    def pop(self):
        minkey=min(self.fifo.keys())
        del self.fifo[minkey]
    def peek(self):
        maxkey = max(self.fifo.keys())
        return self.fifo[maxkey]
    def size(self):
        return self.count
