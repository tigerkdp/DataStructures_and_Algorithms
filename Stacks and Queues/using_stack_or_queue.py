#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 14:20:26 2019

@author: kdp
"""


#Check well formed bracket symbols 

def is_well_formed(s):
    
    left_chars = []
    brack_dict = {'(':')',   '{':'}', '[':']'}
    
    for char in s:
        if char in brack_dict:
            left_chars.append(char)
            print(left_chars)
        elif not left_chars or brack_dict[left_chars.pop()] != char:
            return False
        
    return not left_chars


ret_bool =is_well_formed("([]){[]}")
ret_bool = is_well_formed("[(]")
print(ret_bool)


            
#Queue using stacks


# caveat: elements should be popped from s1 and pushed into s2
# when s2 is completely empty
class queue_using_stacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    #all additions will happen in S1. 
    #they will be moved to S2 when S2 is empty. 
    def add(self, new_item):
        self.s1.append(new_item)
        print(new_item, "added")
        
    def remove(self):
        if self.s2 == []:
            
            #if s2 is empty then pop all elem from s1 and push to s2
            while self.s1:
                item = self.s1.pop()
                self.s2.append(item)
                    
        #the first elem popped from s2 will be the first one inserted
        item = None
        if self.s2:
            item = self.s2.pop()

        print(item, "removed")
        return item 
    
    def empty(self):
        if self.s1.empty() and self.s2.empty():
            return True
        else:
            return False
        
    def display(self):
        print(self.s2)
        print(self.s1)
    
        
Q1 = queue_using_stacks()
Q1.add(10)
Q1.add(20)
Q1.add(30)
Q1.add(40)
Q1.remove()
Q1.remove()
Q1.add(50)
Q1.remove()
Q1.remove()
Q1.add(60)
Q1.add(70)
Q1.remove()

        
#Stack using queue:
class stack_using_queues:
    
    def __init__(self):
        self.q1 = []
        self.q2 = []
        
    def empty(self):
        if self.q1 == []:
            return True
        return False
    
    def push(self, new_item):
        self.q1.append(new_item)
        print(new_item, "added to queue at the back" )
        
    def pop(self):
        
        if self.q1 == []:
            return "No Item to pop"
        
        while len(self.q1) > 1:
            item = self.q1.pop(0)
            self.q2.append(item)
            
        item = self.q1.pop()
        self.q1, self.q2 = self.q2, self.q1 

        print(item, "item popped from queue as stack")
        return item
    
print()
stack = stack_using_queues()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.pop()
stack.pop()
stack.pop()
stack.push(50)
stack.pop()
stack.pop()


#Checking Balancing of Symbols

def balance_of_symbols(expr):
    
    open_symbols = ['(', '[', '{']
    closed_symbols = [')', ']', '}']
    sym_dict = {')':'(',   '}':'{', ']':'['}
    
    sym_stack = []
    
    n = len(expr)
    
    for i in range(n):
        if expr[i] in open_symbols:
            sym_stack.append(expr[i])
            
        if expr[i] in closed_symbols:
            if sym_stack == []:
                return False
    
            popped = sym_stack.pop()
            if popped != sym_dict.get(expr[i]):
                return False
         
    return not sym_stack  #true

exp_bool1 = balance_of_symbols("(A+B)+(C+D)")
print(exp_bool1)
exp_bool2 = balance_of_symbols("(A+B)+[C+D)")
print(exp_bool2)
            
        
# Given and array A. Find the Spans. 
# Span is the max number of consecutive elements such that A[j] <= A[j+1]
# Common in stock market. Max number of consecutive days the price of stock
# up to the current day has been less than or equal to its price on day i.

def finding_spans2(A):
    
    spans = [1] * len(A)
    n=len(A)
    for i in range(1,n) :
        if A[i] >= A[i-1]:
            spans[i] = spans[i-1]+1
    print(spans)
            
A = [6,3,4,4,2,3,4,5]
finding_spans2(A)
        
    
