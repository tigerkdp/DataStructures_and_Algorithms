#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 20:57:38 2019

@author: kdp
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
    
    for i in range(1, len(sorted_activities)):
        #print(sorted_activities[i][0], sorted_activities[i-1][1])
        if sorted_activities[i][0] >= previous_activity:
            print(sorted_activities[i])
            previous_activity = sorted_activities[i][1]
    
    
start_time_arr = [0, 3, 1, 5, 5, 8]
end_time_arr = [6, 4, 2, 8, 7, 9] 
activity_selection(start_time_arr, end_time_arr)