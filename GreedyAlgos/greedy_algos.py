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

Time Complexity NLogN
Space Complexity LogN

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
    
Time Complexity - ON
Space Complexity - OV (length of the result array)
"""  
        

            
#Fractional Knapsack
#Fill the knapsack such that the value is maximum and total weight is W.
#Items can be broken down to maximize knapsack

#Algorithm
#Calculate the ratio (value/weight) for each item
# sort the items based on this ratio in desc order
#Take the items with the highest ratio until weight allows
#At the end, add the next item in fraction as you can

class item_value:
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt   #ratio of value/weight
        
    def __lt__(self, other):
        return self.cost < other.cost
    
class fractional_knapscak:
    
    @staticmethod
    def get_max_value(wt, val, capacity):
        
        iVal = []
        for i in range(len(wt)):
            item_val=item_value(wt[i], val[i], i)
            print(item_val)
            iVal.append(item_val)
            
        #sort the item based on ratio in desc
        iVal.sort(reverse=True)
        
        total_value = 0
        
        #take each item with highest ratio
        for i in iVal:
            curr_wt = int(i.wt)  #curr weight
            curr_val = int(i.val)  #curr value
            if capacity - curr_wt >= 0: #if capacity - curr wt >0
                capacity -= curr_wt     #deduce weight from capacity and make it new capacity
                total_value += curr_val #add value to total_value
            else:       # capacity - weight is less than zero
                fraction = capacity / curr_wt  #fraction of the capacity
                total_value += curr_val * fraction  #total value = curr val*fraction
                capacity = int(capacity - (curr_wt * fraction)) #update capacity
                break
        return total_value
    
wt = [10,40,20,30]
val = [60,40,100,110]
capacity = 50

max_value = fractional_knapscak.get_max_value(wt, val, capacity)
print("Max Value that can go in the Knapsack is", max_value)


            
            
        
        
    
        
        
    
    
    


