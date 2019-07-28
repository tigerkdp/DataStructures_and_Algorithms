# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Learning Arrays 

def unsorted_linear_search(A, data):
    n = len(A)
    
    for i in range(0, n):
        if A[i] == data:
            return i
    
    return -1

A = [1,19,5,8,24,3, 12,14,4,2]
print(unsorted_linear_search(A, 3))
print(unsorted_linear_search(A, 6))

#O(N)
#output: 
#5
#-1

def sorted_search(A, data):
    n = len(A)
    
    for i in range(0,n):
        if A[i] == data:
            return i
        else:
            if A[i] > data:
                return -1
            
    return -1

A = [1,2,3,4,5,6,8,10,12,24,25]
print(sorted_search(A, 10))
print(sorted_search(A, 11))

#O(N)
#output
#7
#-1

#constraint - sorted
def Binary_search_iterative(A, data):
    lo = 0
    hi = len(A)-1
    
    while lo <= hi:
        mid =  lo+(hi-lo) // 2
        if A[mid] == data:
            return mid
        elif A[mid] > data:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

A = [1,2,3,4,5,6,8,10,12,24,25]
print(Binary_search_iterative(A, 2))
print(Binary_search_iterative(A, 25))

#O(logN)
#1, 10

#recursion. divide and conquer
def binary_search_recursive(A, lo, hi, data):

    if hi >= lo:
        mid = lo+ (hi-lo) // 2
        if A[mid] == data:
            return mid
        elif A[mid] < data:
            return binary_search_recursive(A, mid+1, hi, data)
        else:
            return binary_search_recursive(A, lo, mid-1, data)       
    else:
        return -1

A = [1,2,3,4,5,6,8,10,12,24,25]
print(binary_search_recursive(A, 0, len(A)-1, 3))
print(binary_search_recursive(A, 0, len(A)-1, 24))

#O(logN)
#2, 9
        

def check_duplicates_brute_force(A):
    n = len(A)
    for i in range(0, n):
        for j in range(1, n):
            if A[i] == A[j]:
                print("Dups exists")
                return
    print("No Dups")
    
A = [1,2,3,4,5,6,8,4,12,24,25]
check_duplicates_brute_force(A)
#output 
#Dups exists
#O(N2)

#sort the list. and then compare value with value next to it.
def check_dups_in_sorted(A):
    A.sort()
    n = len(A)
    for i in range(0, n-1):
        if A[i] == A[i+1]:
            print("Dups exists")
            return
            
    print("Dups do not exist")

A = [1,19,5,8,24,3, 12,2,4,2]
check_dups_in_sorted(A)
#output
#Dups exists
#O(NLogN) - NLogN due to sorting.


#read the array and move even numbers in front of the list
#and odd numbers in the back.
def even_odd(A):
    lo = 0
    hi =  len(A) -1
    
    while lo < hi:
        if A[lo] % 2 == 0:
            lo += 1
        else:
            A[lo], A[hi] = A[hi], A[lo]
            hi -= 1
        
A = [1,19,5,8,24,3, 12,2,4,2]
even_odd(A)
print(A)
#output
# [2,4,2,8,24.12,3,5,19,1]
        

#have to return the index of the array
#or set the remaining values to None.
#and only print the values that are not None.
def delete_dups_from_sorted_array(A):    
    if not A:
        return 0
    
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index-1] != A[i]:
            A[write_index] = A[i]
            write_index +=1
            
    return write_index

A = [1,2,2,4,5,6,8,12,12,24,25]
index = delete_dups_from_sorted_array(A)
#first 9 entries are good out of 11 
print("Array after removal of the dups")
print(A[0:index])
#[1, 19, 5, 24, 3, 12, 2, 8, 2, 4]
    

#max elem
#define a max variable and keep checking each value
def find_max_elem_in_array(A):
    n = len(A)
    
    max = A[0]
    for i in range(1, n):
        if A[i] > max:
            max = A[i]
    return max

A = [10,324,45, 90, 100]
max1 = find_max_elem_in_array(A)
print("\nLargest elem is", max1)


#function to find a given integer x appears more than n/2 times
#divide and conquer using binary search

#helper binary search function
def binary_search_alt(A, lo, hi, data):

    if hi >= lo:
        mid = lo + hi // 2
        
        #check if A[mid] is first occ of x.
        #A[mid] is first occ if one of the following is true
        #1 mid == 0 and A[mid] == x
        #2 A[mid-1] < x and A[mid] == x
        if (mid == 0 or x > A[mid-1]) and (A[mid] == data):
            return mid
        elif A[mid] < data:
            return binary_search_recursive(A, mid+1, hi, data)
        else:
            return binary_search_recursive(A, lo, mid-1, data)       
    else:
        return -1


#binary search. 
def is_majority(A, n, x):
    
    #if i is found.
    i = binary_search_alt(A, 0, n-1, x)
    
    if i == -1:
        return False
    
    #check if the element is present more than n/2 times
    if ((i + n//2) <= (n-1)) and A[i + n//2] == x:
        return True
    else:
        return False
    

AB = [1,2,3,3,3,3,3,3, 10]
n=len(AB)
x = 3
print("does", x, "appear more than n/2 times in A?",is_majority(AB,n,x))
#output does 3 appear more than n/2 times in A? True

#start reading the array from the end. 
#Check last value and last value - 1. If matching then return
def last_duplicate_index_in_a_sorted_array(A):
    n = len(A)
        
    if (A is None or n <= 0):
        return
    
    for i in range(n-1, 0, -1): #reverse traversal
        if A[i] == A[i-1]:
            print("Last index is", i, "of the Last duplicate itm in A", A[i])
            return
    print("no dups")
    
A = [1,5,5,6,6,7,9]
last_duplicate_index_in_a_sorted_array(A)
#output: Last index is 4 of the Last duplicate itm in A 6


#buy the stock once and sell once. Buying has to happen before.
# min_price_so_far = store min_price until today 
# min of today's price and min_price_so_far
# max_profit_sell_today = what is the profit today (price-min_price_so_far)
# max_profit = max(max_profit and max_profilt today)
#
def buy_and_sell_stock_prices(prices):
    
    min_price_so_far = prices[0]  #initialize with the price on day1
    max_profit  = 0.0  #max profit is 0 on day 1.
    
    for price in prices:    
        #today's profit - today's price minus min price so far. 
        max_profit_sell_today = price - min_price_so_far
        
        #compare max profit until now and store the max
        max_profit = max(max_profit, max_profit_sell_today)
        
        #maintain minimum price so far.
        min_price_so_far = min(min_price_so_far, price)
        
    return max_profit

prices = [7,1,5,3,6,4]
print("max profit is", buy_and_sell_stock_prices(prices))


#arrange where B[0] <= B[1] >= B[3] <= B4 >= B5..
#computer alternation
#sorting is not needed. Median is not needed either
#iterating through the array and swapping A[i] A[i+1] when i is even
#and A[i] > A[i+1] or i is odd and A[i] < A[i+1] achieves it.
#O(N)
def rearrange(A):
    
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i : i+2], reverse = i % 2)
        
A = [1,19,5,8,24,3,12,2,4,2]
rearrange(A)
print("A[0] < A[1] > A2 < A3 > A4 < A5..")
print(A)
#output [1, 19, 5, 24, 3, 12, 2, 8, 2, 4]


#Given an array return a random subset of the given size of the array elemts
import random
def random_sampling(A, k):
    
    for i in range(k):
        r = random.randint(i, len(A)-1)
        A[i], A[r] = A[r], A[i]
        
A = [3,7,5,11]
k = 3
random_sampling(A, k)
print(A[0:k])


#find first elem larger than k in a sorted list
#divide and conquer 
#define a variable called result = inf.  
#keep updating result with A[mid] if A[mid] > k
#log(N)
def find_next_higher(A, k):
    
    lo = 0
    hi = len(A)-1
    
    result = float("inf")
    while lo <= hi:
        mid = (lo + hi) // 2
        
        if A[mid] > k:
            result = A[mid] #upfate result
            hi = mid - 1
        else:
            lo = mid + 1
            
    return result

A = [1,2,3,4,5,6,8,10,12,24,25]
k = 6
print("next higher than k {} is".format(k), find_next_higher(A, k))

#  using math technique.  
#Total = sum of values from 0 to n. 
#Sum_of_array = sum of all values in the input array
#return total - sum_of_array
def get_missing_num(A):
    n = len(A)
    total = (n+1) * (n+2) / 2
    sum_of_A = sum(A)
    return total - sum_of_A

A = [1,2,4,5,6]
print("missing number is ", get_missing_num(A))

#output 3

#find two elems whose sum is closes to 0
# sort all elem of input array
# use lo and high to traverse from both sides.
# sum = a[lo] + a[hi].  if sum1 <= minsum, update minsum.
#keep track of abs min. Repeat 
def two_elements_whose_sum_is_closest_to_zero(A):
    
    lo = 0
    hi = len(A)-1
    
    #variables to keep track of pairs
    min_lo = lo
    min_hi = hi
    if hi < 2:
        print("mininum two elements needed")
        return
    
    #sort
    A.sort()
    min_sum = float("inf")
    sum1 = float("inf")
    while lo < hi:
        
        sum1 = A[lo] + A[hi]
        
        #if sum1 is less than minsum. 
        #store sum1 in minsum. and update min_lo, min_hi
        if abs(sum1) <= abs(min_sum):
            min_sum = sum1
            min_lo = lo 
            min_hi = hi
            
        #sum1 is -ve traverse right(lo++). 
        #if sum is +ve, traverse left(hi--)
        if sum1 < 0:
            lo += 1
        else:
            hi -= 1
            
    #print the A[min_lo] and A[min_hi]
    print("The two elements whose sum is min are ", A[min_lo], A[min_hi])


A = [1,60, -20, 22, -98, 86, 21]
two_elements_whose_sum_is_closest_to_zero(A)
        

#assume no duplicates in an array
#divide and conquer.
#while lo < hi:
#mid = lo + (hi-lo)//2
#if A[mid] == data then return mid index. 
# if A[lo] <= A[mid] and 
    # data is less than A[mid] and data is greater than A[lo]
    # then hi = mid-1, move towards left subarray
    # else lo = mid+1 move towards right subarray
# if A[mid] <= A[hi]
    # if data >= A[mid] and data is less than A[hi]
    # then lo = mid+1 move towards right subarray
    # else hi = mid-1, move towards left subarray
#return -1
def search_in_rotated_array(A, data):
    lo = 0
    hi = len(A)-1
    
    while lo < hi:
        mid = lo + (hi-lo)//2
        
        if A[mid] == data:
            return mid
        
        if A[lo] <= A[mid]:
            if data < A[mid] and data >= A[lo]:
                hi = mid - 1
            else:
                lo = mid + 1
                
        if A[mid] <= A[hi]:
            if data > A[mid] and data <= A[hi]:
                lo = mid + 1
            else:
                hi = hi - 1
                
    return -1 

A = [3,4,5,6,1,2]
k  = 1 
print("Item found at index ", search_in_rotated_array(A, k))


#pring the max sum of contiguous data elements.
def contiguous_max_sub_array(A):
    
    dp = []
    #copy first number to new list.
    dp.insert(0, A[0])
    
    #make the first element as max sum
    max_sum = dp[0]
    
    #traverse from elem 1. 
    #Compare with last elem in new list. 
    #Add new list element-1 with A[i] if its greater than 0 else only add A[i]
    for i in range(1, len(A)-1):
        dp.append(A[i] + (dp[i-1] if dp[i-1] > 0 else 0))
        max_sum = max(dp[i], max_sum)
     
    return max_sum

A = [-2, 1,-3, 4, -1, 2, 1, -5, 4]
print(contiguous_max_sub_array(A))

# find  two sum.  
# Check each value from 0th index. 
# sum_result = target value - A[index]
# if sum_result exist in map1. then append the sum_result, A[i] into result list.
# otherwise continue updating the map with the A[i] value. 
# return result. 
def find_two_sum(A, target):
    
    result = []
    map1 = {} 
    
    for i in range(0, len(A)):  
        #9 - 7 = 2.
        sum_minus_element = target - A[i]
        
        #if 2 exist in map, then add  2 and 7.        
        if sum_minus_element in map1:
            result.append([sum_minus_element, A[i]])
            
        #iteration 0, 1, 2, 3
        #{2:2, 7:7, 11:11, 15:15}
        #first element 2 wont exist in map until this step.
        map1[A[i]] = A[i]
        
    return result

A = [2,7,11,15]
target = 9
print(find_two_sum(A, target))
#output: [[2, 7]]


#Two sum in a sorted array
# traverse from both sides of the array. lo and hi
# sum A[lo] and A[hi] and if it matches target, return True
# if the sum is less than target, then move lo
#if the sum is greater than target, move hi.
# Return false if not found.
def has_two_sum_in_sorted_array(A, target):

    lo = 0
    hi = len(A)-1

    while lo <= hi:
        if A[lo] + A[hi] == target:
            return True
        elif A[lo] + A[hi] < target:
            lo += 1
        else:
            hi -= 1

    return False

A = [2,7,11,15]
target = 9
print("Two sum exists in the array", has_two_sum_in_sorted_array(A, target))

# Two for loops needed.  
#First for loop from 0 to n-1.  For i in 0 to n.
# define a set.   calculate currSum = target - A[i]
# Second for loop one 1 to n.  For j in i+1 to n.
# if currSum is in the set, then found. print A[i], A[j], currSum-A[j]
# otherwise value from 2nd for loop into the set.
#return False.
def find_three_sum(A, target):
    
    n = len(A)
    for i in range(0, n-1):
        
        s =set()
        curr_sum = target - A[i]
        
        for j in range(i+1, n):
            if (curr_sum - A[j]) in s:
                print("Triplet is ", A[i], A[j], curr_sum-A[j])
                return True
            s.add(A[j])
    
    return False

A = [1,4,45,6,10,8]
target = 50
print(find_three_sum(A, target))
#output
#Triplet is  1 45 4

def has_three_sum(A, target):

    A.sort()
    return any(has_two_sum_in_sorted_array(A, target-a) for a in A)

A = [1,4,45,6,10,8]
target = 50
print("Has three sum", has_three_sum(A, target))

#optimal way to merge subfiles
#merge files of size 4 and 6 first.
#define heap.
# Push all elements of the input array into the heap. It will be min heap.
# define a variable called count=0.  
# Until there are elements in heap, 
    #keep popping first two elements. # sum them and store them into a temp
    #keep summing the temp variable with count variable. 
    #push the temp variable back into the heap.
#return 
import heapq as pq
def minimumTime(numOfSubFiles, files):   
    h = []  
    for i in range(0, numOfSubFiles):
        pq.heappush(h, files[i])
        
    cnt = 0
    
    while len(h) > 1:
        
        temp = pq.heappop(h) + pq.heappop(h)
        cnt += temp
        
        pq.heappush(h, temp)
        
    return cnt
    
files=[3,6,5,11]
numOfSubFiles = 4
min_time = minimumTime(numOfSubFiles, files)
print(min_time)
#output 47,  3+5:8,  6+8=14, 11+14=25, 8+14+25=47


#
def optimalUtilization(deviceCapacity, foregroundAppList, backgroundApplist):
    
    result = []
    foregroundMap = {} 
    backgroundMap = {}
    
    #push all matrix (row, col) elements from foreground list into dictionary.
    #key = column, value = row. 
    for i in range(0, len(foregroundAppList)): 
        foregroundMap[foregroundAppList[i][1]] = foregroundAppList[i][0]
     
    # just for validation
    print(foregroundMap)

    #push all matrix (row, col) elements from foreground list into dictionary.
    #key = column, value = row. 
    for i in range(0, len(backgroundApplist)): 
        backgroundMap[backgroundApplist[i][1]] = backgroundApplist[i][0]    

    print(backgroundMap)
    
    #For each value in foreground map, 
    #store the subtracted value in sum_minus from target - key (two sum problem)
    #if the sum minus is in background dictionary, then print both values
    for key, value in  foregroundMap.items():   
        sum_minus = deviceCapacity - key
        
        #if 2 exist in map, then add  2 and 7.        
        if sum_minus in backgroundMap:
            result.append(value)
            result.append(backgroundMap[sum_minus])
            
            print(result)
            result = []
            
deviceCapacity = 10
foregroundAppList= [[1,3],[2,5],[3,7], [4,10]]
backgroundAppList = [[1,2],[2,3],[3,4], [4,5]]

optimalUtilization(deviceCapacity, foregroundAppList,backgroundAppList )

#output 3
#[2, 4]  #5 + 5 = 10
#[3, 2]  #7 + 3 = 10
