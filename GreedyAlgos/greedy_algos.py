#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 20:57:38 2019

@author: kdp

1. Activity Selection Problem
2. Coin Change Problem

"""



#sort activities by end time
#store first activity as previous activity and print first activity
#Traverse through the sorted activities. 
#if start time of current activity is >= end time of previous activity, print
#set previous activity as current activities end time
def activity_selection(start_time_arr, end_time_arr):
    
    activities = zip(start_time_arr, end_time_arr)
    sorted_activities = sorted(activities, key=lambda x: x[1])
    #print(sorted_activities)
    
    previous_activity = sorted_activities[0][0]
    print(sorted_activities[0])
    
    #traverse through the sorted activities from 1 to n-1
    for i in range(1, len(sorted_activities)):
        #print(sorted_activities[i][0], sorted_activities[i-1][1])
        if sorted_activities[i][0] >= previous_activity:
            print(sorted_activities[i])
            previous_activity = sorted_activities[i][1]
    
    
start_time_arr = [0, 3, 1, 5, 5, 8]
end_time_arr =   [6, 4, 2, 8, 7, 9] 
activity_selection(start_time_arr, end_time_arr)

""" - 4 activities
(1, 2)
(3, 4)
(5, 7)
(8, 9)

"""

#Coin change problem
# Given a value v, we want to make changes of V $, which is the minimum # of coins
# needed to make the change 
#We have infinite supply of denominations in $ of [1, 2, 5, 10, 20, 50, 100, 500, 1000] 
#valued coins/notes


# Traverse backwards. If denominations <= N, append to result and reduce N
# if N reaches less than 0, 
def coin_change(N, denominations):
    
    result= []
    hi = len(denominations)-1
    while hi >= 0:
        if denominations[hi] <= N:
            result.append(denominations[hi])  
            N = N - denominations[hi]
        else:
            hi-=1
        if N <= 0:
            print(result)
            break

denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
coin_change(2352, denominations)
      
"""
1000, 1000, 100, 100, 100, 50, 2]
"""  
        
            
        
        
        
    
    
    


