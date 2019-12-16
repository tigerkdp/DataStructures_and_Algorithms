#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 10:02:06 2018

@author: kdp
"""

class ListStack:
    
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, item):
        self.stack.append(item)
        
        if self.min_stack:
            if self.min_stack[-1] > item:
                self.min_stack.append(item)
        else:
            self.min_stack.append(item)
    
    def peek(self):
        print(self.stack[-1])
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty()==True:
            print("Empty - cant pop")
            return 0
        else: 
            popped = self.stack.pop()
            if popped <= self.min_stack[-1]:
                self.min_stack.pop()
            return popped 
        
        
    def display(self):
        print(self.stack, sep=",")
        
    def displayReverse(self):
        print(self.stack[::-1])
        
    def sortStack(self):
         self.stack.sort()
         print(self.stack)
         
    def minValue(self):
        print(self.min_stack[-1])
        return self.min_stack[-1]
        
    def maxValue(self):
        return max(self.stack)
        
    def removeDup(self):
        self.stack.sort()
        n = self.size()-1
        temp = self.stack.copy()
        for i in range(0, n):
            if self.stack[i] == self.stack[i+1]:
                del temp[i]
        self.stack = temp
        
        

        
        
        

#test:
ls = ListStack()
ls.push(1)
ls.push(2)
ls.push(3)
ls.push(4)
ls.display()  #[1, 2, 3, 4]

print(ls.size())  #4
ls.push(-1)
ls.minValue()  #-1 
ls.display() #[1, 2, 3, 4,-1]
ls.peek()  #-1
ls.push(3)
ls.push(4)
ls.push(4)
ls.push(5)
print(ls.size())  #9
ls.display()          #[1, 2, 3, 3, 4, 4, 5]
ls.displayReverse()   #[5, 4, 4, 3, 3, 2, 1]
ls.sortStack()        #[1, 2, 3, 3, 4, 4, 5]
print(ls.minValue())  #1
print(ls.maxValue())  #5
ls.removeDup()   
ls.display()        #[1, 2, 3, 4, 5]
ls.pop()   
ls.display()      #[1, 2, 3, 4]