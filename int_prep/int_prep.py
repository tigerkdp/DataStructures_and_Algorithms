#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 20:24:13 2019

@author: kdp
"""

#Role of a DE
"""
    1) Responsible for building data solutions to help make raw data more useful and meaningful to the enterprise.
    2) Requires technical skills of skills, database design, some programiming skills
    3) Need communication skills to work across departments to understand what business leaders/users
       want to gain from compananies datasets, but also to share technical feasibility and constraints 
    4) Depending upon the organization, we may be required to build dashboards, ad-hoc analysis in finding trends
    5) Role can be more pipeline centric - database centric or generalist 

"""

#calculate the average word length

def avg_word_length(A):
    
    alist = A.split(" ")
    
    print(alist)
    count = 0 
    word_len=[]
    for i in alist:
        word_len.append(len(i))
        count+=1
    print(word_len)
    print(count)
    print(sum(word_len)/count)
    
       

A = "Mary had little lamb"
avg_word_length(A)


#check if a given ip address is valid

def validate_ip_address(A):
    
    ip_list = A.split(".")
    
    print(ip_list)
    result_list = []
    for i in ip_list:
        if i.isdigit() and int(i) >= 0 and int(i) < 255:
            result_list.append(i)
            
    if len(result_list) == 4:
        print(True)
    else:
        print(False)

A = "123.123.10.232"
validate_ip_address(A)

A = "a123.123.a.232"
validate_ip_address(A)

#Number of times a given char occurs in a given string

def char_number_of_times(A, S):
    
    adict = {}
    for i in A:
        if i in adict:
            adict[i] += 1
        else:
            adict[i] = 1 
            
    print(adict[S])

A="Sensitivity"
S = 'i'
char_number_of_times(A, S)


#Given an array containing None values. Fill in the None values with most left value in the array

def fill_in_non_null_values(a):
    
    for i in range(len(a)-1, -1, -1):
        if a[i] is None and a[i-1] is not None:
            a[i] = a[i-1]
        
    print(a)

a = [None,1,2,None,None,4,None,None]
fill_in_non_null_values(a)

#Return a list containing all the mismatched words (case sensitive) between two input strings

def mis_match_words(A, B):
    
    adict = {}
    alist = A.split(" ")
    blist = B.split(" ")
    for word in alist:
        adict[word] =1 
    for word in blist:
        if word in adict:
            adict[word] +=1 
        else:
            adict[word] = 1 

    result = []
    for key, val in adict.items():
        if val == 1:
            result.append(key)
        
    print(result)

A = "Mary had a little lamb"
B = "Joe had A little Goat" 
mis_match_words(A, B)

#Returns the smallest key (sorted alpha) of a given input dict containing nth highest value


#Given an array with n elements, provide elements along with the number of repeated occurrences of each
#needed to balance the array


#Return True if a given string containing the following kinds of brackets is balanced else return false


#Find minimum number of words between repeated occurrences of the search string in the input string


#Find if a given number x is a prime


#Top k elements from a list


#Phone to string combinations


#Remove zeros from the array


#Validate BST



#Determine if input is a palindrome


#Find two elements summing up to a target

def two_sum(A, target):
    
    adict = {}
    result = []
    for i in range(0, len(A)):
        
        tar_val = target - A[i]
        
        if tar_val in adict:
            result.append(adict.get(tar_val))
            result.append(i)
        else:
            adict[A[i]] = i
            
    print(adict)
    print(result)

A = [2,8,7,12,3,1, 34]
target = 14
two_sum(A, target)


#List max contiguous sum

def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    print(max_so_far)
    return max_so_far

A = [-2, 1,-3, 4, -1, 2, 1, -5, 4]
print("Max subarray", max_subarray(A))
#Max subarray 6

def contiguous_max_sub_array(A):
    
    dp = []
    #copy first number to new list.
    dp.append(A[0])
    
    #make the first element as max sum
    max_sum = dp[0]
    
    #traverse from elem 1. 
    #Compare with last elem in new list. 
    #Add new list element-1 with A[i] if its greater than 0 else only add A[i]
    for i in range(1, len(A)):
        if dp[i-1] > 0:
            dp.append(A[i] + dp[i-1])
        else:
            dp.append(A[i])
            
        max_sum = max(dp[i], max_sum)
     
    return max_sum

A = [-2, 1,-3, 4, -1, 2, 1, -5, 4]
print("contiguous max subarry ", contiguous_max_sub_array(A))

#Contigous sequence sum to given number




#Design backend for craigslist / netflix / youtube / Uber / Newsfeed 



# 
