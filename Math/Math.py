# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
#Learning Math related prog. 


#recursive
def fact(n):
    if n < 2:
        return n
    else:
        return n * fact(n-1)
    
print(fact(5))

Factlist = list(map(fact, range(11)))
print(Factlist)

#output[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]


#fibonnaci
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(8))



#whether n is even or odd.
def evenOrodd(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
        
evenOrodd(7)


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

#recursive
def GCD(a,b):
    if b == 0 or a == b:
        return a  
    else:
        return GCD(b, a % b)
     
n = GCD(504, 396)
print(n)


#LCM
def LCM(a, b):
    gcd = GCD(a,b)
    a=abs(a)
    b=abs(b)
    lcm = (a // gcd) * b
    print(lcm)
    
LCM(21,6)


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
    print(alist)
    
primeList(100)
        
#is prime
def isPrime(N):
    for i in range(2, N):
        if N % i == 0:
            return False
    return True
       
print(isPrime(67))

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
InterSect1(A, B,C)


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

#median of an array
import math
def median(A):
    n = len(A)
    if n % 2 != 0:
        mid = math.floor(n//2)
        print("median is ", A[mid])
    else:
        mid = math.floor(n//2)-1
        mid2 = mid+1
        med = (A[mid] + A[mid2])/2
        print("median is ", med)
         
A = [600, 470, 170, 430, 300]
median(A)


# Stand Dev, Variance
def varianceStdDev(A):
    n = len(A)
    sum=0
    if n==0:
        return
    else:
        for i in A:
            sum = sum+i
            aver = sum/n
    print("average is ", aver)
    varNum2 =0 
    sumofSq =0
    for i in A:
       varNum = 0
       varNum = abs(i - aver) 
       varNum2 = varNum * varNum
       sumofSq = sumofSq+varNum2
       var = sumofSq / n
    print("variance is ", var)
    stddev=0
    stddev = math.floor(math.sqrt(var))
    print("stddev is ", stddev)
    
A = [600, 470, 170, 430, 300]
varianceStdDev(A)


#Roman to Int
def romanToInt(R):
    
    roman_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    hi = len(R)-1
    sum=roman_map.get(R[hi])
    for i in range(hi-1, -1, -1):   #i=len-2, i<=0 , i--
        
        r1 = roman_map.get(R[i])
        r2 = roman_map.get(R[i+1])
        
        if r1 < r2:
            sum = sum - roman_map.get(R[i]) 
        else:
            sum = sum + roman_map.get(R[i])
    print(sum)

U = "CMXCIV"
romanToInt(U)