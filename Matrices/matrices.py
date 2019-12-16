#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 20:19:48 2019

@author: kdp
"""



def print_all_elem(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end= ' ')
        print()
        
M = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
print_all_elem(M)
# 1 2 3 4 
#5 6 7 8 
# 9 10 11 12 


print()
def print_matx_alt(M):
    for row in M:
        for cell in row:
            print(cell, end=' ')
        print()
        
M = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
print_matx_alt(M)
# 1 2 3 4 
#5 6 7 8 
# 9 10 11 12 

def sum_of_matx_elm(M):
    s = 0
    for row in M:
        for cell in row:
            s += cell
    print(s)
    
M = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
sum_of_matx_elm(M)


def search_an_item_in_a_matx(M, k):
    for row in M:
        for cell in row:
            if cell == k:
                print("item found")
                return
    print("Item not found")
    
M = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
k = 10
search_an_item_in_a_matx(M, k)


def max_item_in_a_matx(M):
    max_item = float("-inf")
    for row in M:
        for cell in row:
            if cell > max_item:
                max_item = cell
    print("max_item is", max_item)
    
M = [[1,2,3,4], [5,6,7,8], [11,12, 82, 9]]
max_item_in_a_matx(M)


def print_diagonal_items(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if i == j:
                print(M[i][j], end=' ')
        print()
    
M = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
print_diagonal_items(M)



    
