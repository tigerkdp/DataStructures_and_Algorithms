# -*- coding: utf-8 -*-
"""
Array
"""
#Learning Arrays 
"""
- Brute Force approach finds all the possible solutions and selects desired solution per given the constraints.
- Dynamic Programming also uses Brute Force approach to find the OPTIMUM solution, either maximum or minimum.
- Backtracking also uses Brute Force approach but to find ALL the solutions.
- Solutions to the Backtracking problems can be represented as State-Space Tree.
- The constrained applied to find the solution is called Bounding function.
- Backtracking follows Depth-First Search method.
- Branch and Bound is also a Brute Force approach, which uses Breadth-First Search method.

1) print the list
2) unsorted_linear_search
3) isListSorted
4) sum_unique_elements
5) Binary_search_iterative  (D&C)
6) Binary_search_recursive (D&C)
7) Reverse the list
8) Print kth item from the last
9) Check duplicate item brute force
10) Check duplicated in sorted list
11) Check duplicated wihtin K sorted  (set)
12) Even or odd item
13) Segregate even and odd items in the list
14) Prime numbers till N
15) If a number is prime
16) Append N items at the end
17) Delete dups from sorted list
18) Find max item in the list
19) Max diff between two items in a list (max, min var)
20) Find majority item in a list (n/2)
21) Item appearing max number of times
22) Leader more than half of the items
23) Last index of a duplicate item in a list
24) Buy and sell stock once for max profit
25) Rearrange items such that A[1] > A[2] < A[3]..
26) Sort the items in wave form
27) Rotate array by k 
28) Common elements (intersection) in 3 sorted arrays
29) Random sampliing from 0 to k
30) Find next higher item than k (D&C)
31) Get missing number
32) Dutch national flag
33) Merge two sorted arrays
34) Two elements whose sum is closest to zero
35) Search in rotated array
36) Max sum in a subarray
37) Contiguous max sum in a subarray
38) Find two items that mathces k (Two Sum)
39) Has two sum in an array
40) Find three sum that matches k (Three sum)
41) Optimal way to merge files (Optimal Merge - Heap)
42) Local Maxima
50) Find the park element
43) Local Minima
44) Cyclic Rotation in an unsorted array
45) Necklace Beads of items in a list
46) Product of all items besides index item
47) Equilibrium (sum of left items == sum of right items)
48) Print all sublists 
49) Print all sublists alternate
51) zero_sum_sub_array
52) Finding Spans 

"""

def list_print(An):
    
    for i in An:
        print(i, end =" ")
    print()
            
An = [1,19,5,8,24,3,12,14,4,2]
list_print(An)

def print_list_comb(lst):
    
    for item in lst:
        for item2 in lst:
            print(item, item2)
    
lst = [1,2,3]
print_list_comb(lst)

"""
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
"""

def unsorted_linear_search(A, data):
    n = len(A)
    
    for i in range(0, n):
        if A[i] == data:
            return i
    
    return -1

A = [1,19,5,8,24,3,12,14,4,2]
print("Found at position", unsorted_linear_search(A, 3))
print("Found at position", unsorted_linear_search(A, 6))

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
print("Found at position", sorted_search(A, 10))
print("Found at position", sorted_search(A, 11))

#O(N)
#output`
#7
#-1

#is list soted - recursive
def isListSorted(A, index):
    if index == 1:
        print("sorted")
        return
    else:
        if A[index] >= A[index-1]:
            return isListSorted(A, index-1)
    print("not sorted")
        
A=[1,2,3,4,5,6]
isListSorted(A, len(A)-1)
#sorted

#Sum of all unique elements
def sum_unique_elements(A):
    
    sum1 = A[0]
    A1=set()
    for i in range(1, len(A)):
        if A[i] not in A1:
            sum1 += A[i]
        A1.add(A[i])
    
    print("Sum of all unique elements", sum1)
    
A=[1,2,2,4,4,6]
sum_unique_elements(A)
#Sum of all unique elements 13

#Binary Search / Divide and Conquery
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
print("Found at position", Binary_search_iterative(A, 2))
print("Found at position", Binary_search_iterative(A, 25))

#O(logN)
#1, 10

#recursion. Binary Search divide and conquer
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
print("Found at ", binary_search_recursive(A, 0, len(A)-1, 3))
print("Found at ", binary_search_recursive(A, 0, len(A)-1, 24))

#O(logN)
#2, 9
     

#Reverse an array 
def reverse_list(A):
    
    lo = 0
    hi = len(A)-1
    while lo < hi:
        A[lo], A[hi] = A[hi], A[lo]
        lo, hi = lo + 1, hi - 1
    print("Reversed Array", A)
        

A = [1,19,5,8,24,3,12,14,4,2]
reverse_list(A)
#Reversed Array [2, 4, 14, 12, 3, 24, 8, 5, 19, 1]


#Kth from the last
def printKthfromLast(A, k):
    
    #python way
    print("Kth from last Python way", A[-k])
    
    lo = 0
    hi = len(A)
    # traverse till K
    while lo < k:
        lo+=1
       
    #set kth=0. Continue traversing. Kth++
    #when reached at end. Kth reaches at the dest.
    kth=0
    while lo < hi:
        kth+=1
        lo+=1
    print("Kth from last", A[kth])
    
A=[1,2,3,4,5,6,7]
printKthfromLast(A, 4)
#Kth from last Python way 4


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


def check_dups_within_k_unsorted(A, n, k):
    
    my_set = []
    for i in range(0, n):
        if A[i] in my_set:
            return True
        
        my_set.append(A[i])
        
        if i > k:
            my_set.remove(A[i-k])
    return False


A = [10,5,3,4,3,5,6]
n = len(A)
if check_dups_within_k_unsorted(A, n, 3):
    print("Yes Dups within k distance")
else:
    print("No dups with k distance")
#Yes Dups within k distance

#whether n is even or odd.
def evenOrOdd(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
        
evenOrOdd(7)
#odd


#Segregage even and odd numbers
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

#seive of erosthenes
#print all prime numbers below 100
# all all numbers from 2 to N in a list.
#define a variable count = 2.  
#while 2 < n. loop.
#for each i from 2 to n. remove i - if i%count=0, and i in alist, and i!=count.
  #increment count.
def primeList(N):
    if N < 2:
        return False
    elif N == 2:
        return True
    alist = []
    for i in range(2,N):
        alist.append(i)
    
    count=2
    while count < N:
        for i in range(2, N):
            if i % count == 0 and i in alist and i != count:
                alist.remove(i)
                i+=1
        #print(count)
        count +=1
    return alist
    
print("Prime numbers from 1 to n is", primeList(100))
#Prime numbers from 1 to n is [2, 3, 5, 7, 11, 13, 
#17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        
#is prime
def isPrime(N):
    for i in range(2, N//2):
        if N % i == 0:
            return False
    return True
       
print("is prime", isPrime(67))
#True

#split the array and add the first part to the end

def split_add_to_end(A, k):
    
    for i in range(0, k):
        A.append(A[0])  #as we r popping, we only have to select A[0]
        A.pop(0)        #once popped the rest of the elements shift

    print("Added at the end", A)
    
A = [12,10,4,5,6,32,43]
split_add_to_end(A, 3)
#Added at the end [5, 6, 32, 43, 12, 10, 4]

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


#max diff between two elements in an array
def max_difference(A):
    
    max1 = float("-inf")
    min1 = float("inf")
    
    for i in A:
        if i > max1:
            max1 = i
        if i < min1:
            min1 = i
        
    max_diff = max1 - min1 
    print("maximum difference in an array", max_diff)
    
A = [10,324,45, 90, 100]
max_difference(A)
#maximum difference in an array 314

#Element appears max # of times 
#use hash table
def max_appearance(N):
    a_hash = {}
    
    # add to a hash table
    for i in N:
        if i in a_hash:
            a_hash[i] +=1
        else:
            a_hash[i] = 1
    max =0
    print(a_hash)
    
    for key, item in a_hash.items():
        if item > max:
            max = key
    print(max)

A = [1,2,3,4,5,5,6,2,2,2,2]  
max_appearance(A)
#output 2

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


#Leader
#usign Hash Table 
def LeaderMoreThanHalf(A):
    li  = {}
    hi = len(A)
    lead = hi // 2
    A.sort()
    print("lead", lead)
    for i in range(0, hi):
        li[A[i]] = li.get(A[i], 0) + 1
    
    max = 0
    item = 0
    for k, v in li.items():
        if max < v:
            max = v
            item = k
            
    if max > lead:
        return item
    else:
        return -1
    
#A = [2,2,2,2,2,3, 4,4,4,6]
A = [1,1,1,1,50, 212443322]
#A = [-1]
print("leader more than half", LeaderMoreThanHalf(A))



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
    
    A.sort()
    lo = 0
    hi = len(A)-1
    
    while lo < hi:
        A[lo+1], A[hi] = A[hi], A[lo+1]
        lo +=2
        hi -=2 
    
    print("rearrange low high, low high", A)
    
#    for i in range(len(A)):
#        A[i:i+2] = sorted(A[i : i+2], reverse = i % 2)
        
A = [1,19,5,8,24,3,12,2,4,2]
rearrange(A)
print("A[0] < A[1] > A2 < A3 > A4 < A5..")
print(A)
#output [1, 19, 5, 24, 3, 12, 2, 8, 2, 4]


# sort in wave. 
def sortinWave(A):
    A.sort()
    n = len(A)
    for i in range(0, n-1,2):
        A[i], A[i+1] = A[i+1], A[i]
    return A
    
A=[6,5,10, 7,13,44,34]
print(sortinWave(A))
#[6, 5, 10, 7, 34, 13, 44]

print()
# Rotate
def rotateArray(A, d):
    
    n = len(A)-1
    templist = []
    for i in range(0, n):
        if i < d:
            templist.append(A[i])
            A.append(templist[i])
        else:
            pass

    nk = len(templist)-1
    for i in range(nk,-1,-1):
        #very slow as it moves
        A.pop(i)
    
    print("Rotated Array")
    print(A, end=" ")
       
A = [1,2,3, 4,5,6,7]
rotateArray(A, 3)

#[4, 5, 6, 7, 1, 2, 3] 


#Common elements in 3 sorted arrays
# while lo < hi. 
    #if A[lo] == B[lo] == c[lo], alo++, blo++,clo++
    #else A[lo] < B[lo], then alo++
    #else B[lo] < c[lo], then blo++
    #slse clo++
print()
def InterSect1(A, B,C):
    Alo, Ahi = 0, len(A)
    Blo, Bhi = 0, len(B)
    Clo , Chi = 0, len(C)
    while Alo < Ahi and Blo < Bhi and Clo < Chi:
        if A[Alo] == B[Blo] and B[Blo] == C[Clo]:
            print(A[Alo])
            Alo +=1 
            Blo +=1
            Clo +=1
        
        elif A[Alo] < B[Blo]:
            Alo+=1
        
        elif B[Blo] < C[Clo]:
            Blo+=1
            
        else:
            Clo+=1
            
A = [1,2,3,4,5]
B = [1,3]
C = [3,4,5]
print("Intersection of A, B, C is ")
InterSect1(A, B,C)

print()
#Given an array return a random subset of the given size of the array elemts
import random
def random_sampling(A, k):
    
    for i in range(0, k):
        r = random.randint(i, len(A)-1)
        A[i], A[r] = A[r], A[i]
        
A = [3,7,5,11]
k = 3
random_sampling(A, k)
print("Random Sampling from 0 to k", A[0:k])
#Random Sampling [7, 5, 3]


print()
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
#next higher than k 6 is 8

print()
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
#missing number is  3.0

print()
#Dutch National
# lo, mid = 0, and hi = len(n)-1
#if A[mid] ==0, then swap and move lo++,mid++. 
#else A[mid]==1, the mid++
#elseif A[mid]==2, then swap with high and hi--
def DutchNational(A):
    lo = 0
    hi = len(A)-1
    mid = 0

    while mid < hi:
       if A[mid] == 0:
            A[lo], A[mid] = A[mid], A[lo]
            lo+=1
            mid+=1
       elif A[mid] == 1:
            mid+=1
       else:  #A[mid] ==2
            A[mid], A[hi] = A[hi], A[mid]
            hi-=1
    print("Dutch National:", A)
    
A=[1,0,2,0,1,0,0,1,2,2,1,0]
DutchNational(A)
#Dutch National: [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2]

print()
#Common elements in 3 sorted arrays
# while lo < hi. 
    #if A[lo] == B[lo] == c[lo], alo++, blo++,clo++
    #else A[lo] < B[lo], then alo++
    #else B[lo] < c[lo], then blo++
    #slse clo++
def InterSect1(A, B,C):
    Alo, Ahi = 0, len(A)
    Blo, Bhi = 0, len(B)
    Clo , Chi = 0, len(C)
    while Alo < Ahi and Blo < Bhi and Clo < Chi:
        if A[Alo] == B[Blo] and B[Blo] == C[Clo]:
            print("Intersection element:", A[Alo])
            Alo +=1 
            Blo +=1
            Clo +=1
        
        elif A[Alo] < B[Blo]:
            Alo+=1
        
        elif B[Blo] < C[Clo]:
            Blo+=1
            
        else:
            Clo+=1
            
A = [1,2,3,4,5]
B = [1,3]
C = [3,4,5]
InterSect1(A, B,C)
#Interseciton element: 3


print()
#Merge two sorted arrays.
#define result list = c. 
# Alo, Blo, Ahi, Bhi. 
#while lo < hi for both A/B.
# first compare A and B 
# If A small, add value from A in C. else add B
# If A has remaining value, Add A.
# if B has remaining values Add B 
def mergeTwoSortedArrays(A, B):
    Alo, Ahi = 0, len(A)
    Blo, Bhi = 0, len(B)
    C = []
    while Alo < Ahi and Blo < Bhi:
        if A[Alo] < B[Blo]:
            C.append(A[Alo])
            Alo+=1
        else:
            C.append(B[Blo])
            Blo+=1
    while Alo < Ahi:
        C.append(A[Alo])
        Alo+=1
    while Blo < Bhi:
        C.append(B[Blo])        
        Blo+=1
        
    print(C)
A= [1,4,5,6,9,10]
B = [2,3,7, 8, 11,12,16,53]
mergeTwoSortedArrays(A, B) 
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 53]


#find two elems whose sum is closes to 0
# sort all elem of input array
# use lo and high to traverse from both sides.
# sum = a[lo] + a[hi].  if sum1 <= minsum, update minsum.
#keep track of abs min. Repeat 
print()
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
#The two elements whose sum is min are  -20 21
        

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
print()
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
#Item found at index  4

print("subarray")
def print_sub_array(A):
    
    list1 = []
    list2 = []
    n = len(A)
    for i in range(0, n):
        list2.append(A[i])
        for j in range(i+1, n):
            list2.append(A[j])
        list1.append(list2)
        list2=[]
    print(list1)

A = [1,2,3]
print_sub_array(A)

print("Continugous Sub array")
def print_sub_array(A):
    
    max_sub = float("-inf")
    n = len(A)
    for i in range(0, n):
        curr_subarry = 0 
        for j in range(i, n):
            curr_subarry += A[j]
            if curr_subarry > max_sub:
                max_sub = curr_subarry
            if curr_subarry < 0:
                curr_subarry = 0
                
    print("max_contig_sub", max_sub)

A = [-2,1,-3,4,-1,2,1,-5,4]
print_sub_array(A)

#max subarray
# max_ending_her: max(x, max_ending_here + x)
# max_so_far = max(max_so_far, max_ending_here)
def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    print(max_so_far)
    return max_so_far

nums = [-2, 1,-3, 4, -1, 2, 1, -5, 4]
print("Max subarray", max_subarray(nums))
#Max subarray 6


"""
max_ending_here = -2. max_so_far = -2
for x in A[1:]
    x=1 
    max_ending_here = max(1, -2+1=-1) = 1
    max_so_far = max(-2, 1) = 1
    
    x=-3
    max_ending_here = max(-3, 1-3=-2) = -2
    max_so_far = max(1, -2) = 1
    
    x=4
    max_ending_here  = max(4, -2+4) = 4 
    max_so_far = max(1, 4) = 4
    
    x=-1
    max_ending_here = max(-1, 4-1) = 3
    max_so_far =  max(4, 3)  = 4
    
    x = 2 
    max_ending_here = max(2, 3+2) = 5
    max_so_far =   max(4, 5) = 5 
    
    x = 1
    max_ending_here = max(1, 5+1)  = 6
    max_so_far =  max(5, 6)  = 6
    
    x=-5
    max_ending_here = max(-5, 6-5) = 1
    max_so_far = max(6, 1) = 6
    
    x=4
    max_ending_here = max(4, 1+4) = 5
    max_so_far = max(6, 5)


"""


#pring the max sum of contiguous data elements.
#also referred as max sequence in an array
print()
def contiguous_max_sub_array(A):
    
    dp = []
    #copy first number to new list.
    dp.append(A[0])
    
    #make the first element as max sum
    max_sum = dp[0]
    
    #traverse from elem 1. 
    #Compare with last elem in new list. 
    #Add new list element-1 with A[i] if its greater than 0 else only add A[i]
    for i in range(1, len(A)-1):
        if dp[i-1] > 0:
            dp.append(A[i] + dp[i-1])
        else:
            dp.append(A[i])
            
        max_sum = max(dp[i], max_sum)
     
    return max_sum

A = [-2, 1,-3, 4, -1, 2, 1, -5, 4]
print("contiguous max subarry ", contiguous_max_sub_array(A))
#contiguous max subarry  6


# find  two sum.  
# Check each value from 0th index. 
# sum_result = target value - A[index]
# if sum_result exist in map1. then append the sum_result, A[i] into result list.
# otherwise continue updating the map with the A[i] value. 
# return result. 
print()
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
print("Two elements sum matching target", find_two_sum(A, target))
#output: [[2, 7]]


#Two sum in a sorted array
# traverse from both sides of the array. lo and hi
# sum A[lo] and A[hi] and if it matches target, return True
# if the sum is less than target, then move lo
#if the sum is greater than target, move hi.
# Return false if not found.
print()
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
print("Two elements sum in the array", has_two_sum_in_sorted_array(A, target))
#Two elements sum in the array True

# Two for loops needed.  
#First for loop from 0 to n-1.  For i in 0 to n.
# define a set.   calculate currSum = target - A[i]
# Second for loop one 1 to n.  For j in i+1 to n.
# if currSum is in the set, then found. print A[i], A[j], currSum-A[j]
# otherwise value from 2nd for loop into the set.
#return False.
print()
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


print()
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
print()
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
print("Organize files pattern", min_time)
#output 47,  3+5:8,  6+8=14, 11+14=25, 8+14+25=47


# Two sum between two input matrix matching target
# two dictionary, 
print()
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



#Local Maxima
print()
def localMaxima(A):
    n = len(A)-1
    fs = A[0]
    ls = A[n]
    res = []
    for i in range(1, n):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            res.append(A[i])
    if fs > A[1]:
        res.append(fs)
    if ls > A[n-1]:
        res.append(ls)
    print("Local Maxima ", res)
        
A = [3,2,33,21,22,11]
localMaxima(A)  
#Local Maxima  [33, 22, 3]

def find_peak_elem_util(A, lo, hi, n):
    
    mid = lo + (hi - lo)//2
    
    if ((mid == 0 or A[mid-1] <= A[mid]) and (mid == n-1 or A[mid+1] <= A[mid])):
        return mid
    elif mid > 0 and A[mid-1] > A[mid]:
        return find_peak_elem_util(A, lo, mid-1, n)
    else:
        return find_peak_elem_util(A, mid+1, hi, n)
        

def peak_element(A, n):
    return find_peak_elem_util(A, 0, n-1, n)


A = [1,3,20,4,1,0]
n = len(A)
print("Index of a peak point elem is", peak_element(A, n))
#Index of a peak point elem is 2

#Local Minima
print()
def localMinima(A):
    n = len(A)-1
    fs = A[0]
    ls = A[n]
    res = []
    for i in range(1, n):
        if A[i] < A[i-1] and A[i] < A[i+1]:
            res.append(A[i])
    if fs < A[1]:
        res.append(fs)
    if ls < A[n-1]:
        res.append(ls)
    print("Local Minima", res)
    
A = [2,3,33,21,22,11]
localMinima(A) 
#Local Minima [21, 2, 11]


#Clycic rotation
print()
def cyclicRotationUnSorted(A, K):
    
    result = []
    L = len(A)
    for i in range(0, L):
        j = (i+K % L) % L
        result.insert(j, A[i])
        
    print("Cyclic rotaion by", K, result)
    
A = [3,8,9,7,4]
cyclicRotationUnSorted(A, 3)
#Cyclic rotaion by 3 [9, 7, 4, 3, 8]


#Necklace Beads
print()
def necklaceBeads(A):
    j = 0
    hi = len(A)-1
    #dict1= {}
    temp = 0
    list1 = []
    max_counter = 0
    for i in range(0, hi):
        #break when all elements are in list
        if len(A) != len(list1): 
            counter = 0 
            #A[j] again but it is already in list
            while A[j] not in list1: 
	      #dict for test
                #dict1.setdefault(i, []).append(A[j])
                list1.append(A[j])
                j =  A[j]
                counter += 1
            #increment j to next item
            temp +=1
            j = temp
            
            if counter > max_counter:
                max_counter = counter
        else:
            break    
    
    #print(dict1)
    print("Max beads found in a necklace", max_counter)
    
A = [5, 4, 0, 3, 1, 6, 2]
necklaceBeads(A)

A[0] = 5   
A[1] = 4
A[2] = 0 
A[3] = 3 
A[4] = 1
A[5] = 6    
A[6] = 2 

#output
#(5, 6, 2, 0 )  (4,1) (3).
#Max beads found in a necklace 4

#Prod without the index
#prod = 1, prod=1(prod)*2=2, prod=2(prod)*5=8, prod=8(prod)*5=40
print()
def prod_without_index(A):
    
    prod = 1
    res = []
    n = len(A)
    
    #when item=2, append [1], calculate prod=item*prod,2*1=[2]
    #when item=4, append [2],  calcuulate  prod=item*prod=4*2=[8],
    #when item=5 append[8], calculate prod=item*prod=5*8=[40]
    #when item=6, append[40], calculate prod=item*prod=6*40=[240] = but this is not appended.
    for item in A:
        res.append(prod)
        prod = item * prod    
    
    prod = 1
    
        #prod=1
    #res[3]*prod=40*1 = 40, 
        #prod =A[3]*prod=6*1=6,      
    #res[2]*prod= 8*6=48,
        #prod=A[2]*prod=5*6=30,
        # prod=A[1]*prod=4*30=120 
    # res[0]=1*120=120
    for i in range(n-1,-1,-1):
        res[i] = res[i]*prod  
        prod = A[i] * prod      
        
    print("Prod of all elements besides self", res)
    
A = [2,4,5,6]
prod_without_index(A)
# Res [1, 2, 8, 40]
#[120, 60, 48, 40]
#Prod of all elements besides self [120, 60, 48, 40]

#sum of right side = sum of left side 
def equilibrium(A):
    
    n = len(A)
    for i in range(0, n):
        left = sum(A[:i])
        right = sum(A[i:])
            
        if left == right:
            return True
    return False    
            
A = [5,5,12,10,12]
print(equilibrium(A))
#True


#print all sublist
def printSubArrayNew(A):
    
    n = len(A)
    sublist=[]
    for i in range(0, n):
        for j in range(i+1, n+1): 
            sub = A[i:j]
            sublist.append(sub)
    print("Print every sublists 1", sublist)
        
A = [1,2,3,4]
printSubArrayNew(A)
#Print every sublists [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [2], 
#[2, 3], [2, 3, 4], [3], [3, 4], [4]]

#
import math
def printSubArrayNew1(A):
    
    n = len(A)
    sublist=[]
    for i in range(0, n):
        for j in range(i+1, n+1): 
            sub = A[i:j]
            sublist.append(sub)
    
    print("Print every sublists 2", sublist)
    
    minAvg = math.inf
    for i in sublist:
        avg = sum(i) // len(i)  
        if avg < minAvg:
            minAvg = avg
    print("Average of the sublist is ", minAvg)
        
A = [2,3,4,5]
printSubArrayNew1(A)
#Print every sublists 2 [[2], [2, 3], [2, 3, 4], [2, 3, 4, 5], [3], 
#[3, 4], [3, 4, 5], [4], [4, 5], [5]]
#Average of the sublist is  2


#check if subarray with 0 sum exists or not.
#use set
def zero_sum_sub_array(A,n):
    
    s = {}
    out = []
    
    sum1 = 0
    for i in range(n):
        sum1 += A[i]
        
        #if current sum is 0, we found a subarray from indx 0 and ending at i
        if sum1 == 0:
            out.append((0, i))
        al = []
        
        #check if curr sum is in hash table or not
        #if curr sum already exist then it indicates this sum was the sum
        # of some subarray elem a[0]...a[i] and now the same sum-
        # is obtained for the curr subarry a[0]..a[j]
        # which means sum of of subarray a[i+1]..a[j] must be 0
        #insert curr sum into hash table
        if sum1 in s:
            al = s.get(sum1)
            for it in range(len(al)):
                out.append((al[it]+1, i))
        al.append(i)
        s[sum1] = al 
    return out      
    
def printOutput(output):
    for i in output:
        print("Subarray found from index " + str(i[0]), str(i[1]))
      
A = [3,4,-7,3,1,3,1,-4,-2,-2]
n = len(A)
out= zero_sum_sub_array(A, n)
if len(out) == 0:
    print("No subarray exist")
else:
    printOutput(out)
    
    
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
        
    
