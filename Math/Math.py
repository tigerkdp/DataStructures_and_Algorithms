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
    
print("fibonnaci", fib(8))



#whether n is even or odd.
def evenOrodd(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
        
evenOrodd(7)

#power - recursive
def powerOf(n, k):
    if k < 2:
        return n
    else:
        return n* powerOf(n, k-1)
    
print(powerOf(4, 3))

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



def oddish_or_evenish(num):
   total = 0
   for n in str(num):
       total += int(n)
   if total % 2 == 0:
       return "Evenish"
   else:
       return "Oddish"
   

print(oddish_or_evenish(44))
#4 + 4 = 8 and hence it is "Evenish"
#"Evenish" if sum([int(x) for x in list(str(num))]) % 2 == 0 else "Oddish"



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


#Reverse a number using Stack
def reverse_a_num_using_stack(num):
    
    stack = []
    
    while num != 0:
        stack.append(num % 10)
        num = num // 10
        #stack = [1,5,7]
    
    reverse = 0
    i = 1
    while stack:
        reverse = reverse + stack.pop() * i  #1. (7 + 1*1)=7  #2. (7 + 5*10)=57  #3 (57+7*100)=157
        i = i * 10
        
    print(reverse)
    
reverse_a_num_using_stack(751)


#find a number is a perfect square
def is_perfect_square(x):
    s = int(math.sqrt(x))
    if s*s == x:
        return True
    else:
        return False

#find if a number is fibonnaci
def is_fibonacci(n):
    return is_perfect_square(5*n*n+4) or is_perfect_square(5*n*n-4)

print("Fibonnaci or n numbers")
for i in range(1,10):
    if is_fibonacci(i):
        print(i, "is Fibonnaci")
    else:
        print(i, "is not Fibonnaci")
        

