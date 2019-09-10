#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 21:14:47 2019

@author: kdp
"""

"""program question breakdown in a Google Interview - source Byte-by-Byte.com
Graphs/Trees  - 29.8%
System Design - 22.6%
Arrays/String - 20.2%
Recursion - 9.5%
Dynamic Prog - 9.5%
Geometry/Math - 8.3% 
"""

"""
Template for designing recursive alg"
1. Determine size of the prob
2. Define base cases
3. Decompose computational problem with self-similar sub
   of smaller size and possibly additional diff probs
4. Define recurse cases by relying on induction and diagrams
    (induction - key idea is that programmers must assume the recursive
     code works for simpler and smaller problems even if they have not written
     of code. Referred as recursive leap of faith)
5. Test the code
"""

def fib_recur(n):
    if n <= 2 :
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)

print("fibonacci", fib_recur(5))
#outuput for 9: 34
#1, 1, 2, 3, 5     next fib numbers 8, 13, 21, 34, 55
"""
                         1 fib(5)
                       /  ret 5   \ 
                      /            \ 
               2  fib(4)           7  fib(3)
               / ret 3 \          / ret 2 \ 
              /         \        /           \ 
           3 fib(3)    6 fib(2)   8  fib(2)   9   fib(1)
           /ret 2 \    ret 1     ret 1        ret 1
          /        \                     
      4 fib(2)    5 f(1)         
      ret 1      ret 1          

"""

def fact_recur(n):
    if n == 1:
        return 1
    else:
        return n * fact_recur(n-1)

print("factorial", fact_recur(5))
#5*4*3*2*1 = 120
"""
       1   fact(5) --> 5 * 24 
          /ret 120
         /
     2   fact(4) --> 4 * 6 = 24
        /ret 24
        /
    3    fact(3) --> 3*2 = 6
        /ret 6
        /
    4   fact(2) --2*1 = 2
       /ret 2
       / 
    5   fact(1) 
       ret 1

"""


def sum_recur(n):
    if n == 1:
        return 1
    else:
        return n + sum_recur(n-1)


print("sum_recur", sum_recur(5))
#5+4+3+2+1 = 15

""" 
     1    sum(5) --> 5 + 10
         /ret 15
        /
     2   sum(4) --> 4 + 6
        /ret 10
        /
    3    sum(3) -> 3 + 3
        /retun 6
        /
    4    sum(2) --> 2 + 1 
        /ret 3
        /
    5    sum(1)
        ret 1
"""

def gcd(m, n):
    if m == 0:
        return n
    elif m > n:
        return gcd(n, m)
    else:
        return gcd(m, n-m)

print("gcd of 232,272 is", gcd(232, 272))
#gcd of 232,272 is 8

"""
                   1 gcd(232, 272)
               30   |ret 8
                    |
                   2 gcd(232,40)
               29   |ret 8
                    |
                  3  gcd(40, 232)
               28   |ret 8
                    |
                  4  gcd(40, 192)
               27   |ret 8
                    |
                  5  gcd(40, 152)
               26   |ret 8
                    |
                  6  gcd(40, 112)
              25    |ret 8
                    |
                 7   gcd(40, 72)
              24    |ret 8
                    |
                8    gcd(40, 32)
              23    |ret 8
                    |
                9   gcd(32, 40)
              22    |ret 8
                    |
                10    gcd(8, 32)
              21    |ret 8
                    |
                11   gcd(8,24)
              20   |ret 8
                   |
                12   gcd(8, 16)
              19   |ret 8
                   |
               13    gcd(8, 8)
             18    |ret 8
                   |
               14    gcd(8,0)
               17  |ret 8
                   |
               15    gcd(0, 8)
               16    ret 8
                       
"""

def gcd_v1(a, b):
    if b == 0:
        return a
    else:
        return  gcd_v1(b, a%b)

print("gcd of 539,84 is", gcd_v1(539, 84))
#gcd of 539,84 is 7
"""
        1      gcd(539, 84)
          10     /ret 7
        2      gcd(84, 35)
          9     /ret 7
        3       gcd(35, 14)
          8    /ret 7
        4       gcd(14, 7)
          7     /ret 7
        5       gcd(7, 0)
          6      ret 7
"""

def sum_of_list_recur(A):
    if len(A)==0:
        return 0
    else:
        return A[0] + sum_of_list_recur(A[1:])

A=[1,2,3,41,5]
print("sum_of_list_recur", sum_of_list_recur(A))
#sum_of_list_recur 52
"""
          1          sum([1,2,3,41,5])
            12       /ret 52
                     /
          2          1 + sum(2,3,41,5)
            11       /ret 52
                    /
          3          2 + sum(3,41,5)
            10       /ret 51
                    /
          4          3 + sum(41, 5)
            9       /ret 49
                    /
          5          41 + sum(5) 
            8       /ret 46  
                    /
          6          5  + sum(): 
            7        ret 5  
"""


def sum_list_len_alt2(A):
    if len(A) == 0:
        return 0
    elif len(A) == 1:
        return A[0]
    else:
        middle = len(A) // 2
        return (sum_list_len_alt2(A[0:middle])
                + sum_list_len_alt2(A[middle:len(A)]))


B = [5,3,4,2,3]
print("sum_list_len_alt2", sum_list_len_alt2(B))
#sum_list_len_alt2 17

"""
       1     sum(5,3,4,2,3) len=5  middle( 5/2) = 2
            /   18   ret 17            \
           /                            \
  2  sum(5,3),len=2,middle=1   8  sum(4,2,3), len = 3, middle, 3//2 = 1  
     / 7 ret 8  \                / 17 ret 9   \     
    /          \                /              \    
 3   sum(5)     \         9  sum(4)             \
 4  ret 5   5  sum(3)   10  ret 4     11  sum(2,3) middle, 2/2 = 1
             6 ret 3                  /  16 ret 5  \
                                     /            \
                              12   sum(2)     14    sum(3)
                              13  ret 2       15   ret 3
"""  

def sum_list_limits_1(A, lower, upper):
    if lower > upper:
        return 0
    else:
        return A[upper] + sum_list_limits_1(A, lower, upper-1)

A1 = [4,2,3,1,5]
print("sum_list_limits_1", sum_list_limits_1(A1,0, len(A1)-1))
#sum_list_limits_1 15

"""  1   sum(4,3,2,1,5), 0, 4
    12   /ret 5+10 = 15
      /
  2    sum(4,3,2,1), 0, 3
  11   /ret 1+9 = 10
       /
  3   sum(4,3,2), 0, 2
  10   /ret 2+7=9
       /
  4   sum(4,3),  0, 1
   9  /ret 3+4=7
      /
 5    sum(4)    0, 0
  8   /ret 4+0=4
      /
 6    sum()     0, -1
  7   /ret 0
"""  


def sum_list_limits_2(A, lower, upper):
    if lower > upper:
        return 0
    else:
        return A[lower] + sum_list_limits_2(A, lower+1, upper)

A2 = [4,2,3,1,6]
print("sum_list_limits_2", sum_list_limits_2(A2, 0, len(A2)-1))
#sum_list_limits_2 16
"""
   1    sum(4,2,3,1,6), 0, 4
    12   /ret 4 + 12 =16
        /
  2    sum(2,3,1,6), 1, 4
   11    /ret 2 + 10 =12
        /
  3    sum(3,1,6), 2, 4
   10   /ret 3+7 = 10
        /
  4     sum(1, 6)  3, 4
    9   /ret 1+6 = 7
        /
  5     sum(6)   4, 4
    8   /ret 6+0 = 6
        /
  6     sum()    5, 4
    7    ret 0
"""
def sum_list_limits_3(A, lower, upper):
    if lower > upper:
        return 0
    elif lower == upper:
        return A[lower]
    else:
        middle = (upper + lower) // 2
        return (sum_list_limits_3(A, lower, middle)
                + sum_list_limits_3(A, middle, upper))

A3 = [4,2,3,1,7]
print("sum_list_limits_3", sum_list_limits_2(A3, 0, len(A2)-1))
#sum_list_limits_3 17

def print_n_numbers(n):
    if n == 0:
        return 0
    else:
        print(n, end= ",")
        print_n_numbers(n-1)
        
print(print_n_numbers(10))
#10,9,8,7,6,5,4,3,2,1,None
      
"""   
  1      print(10)
    21  | ret 0
        |
       10   #print
  2     print(9)
   21  |ret 0       
       |
       9   #print
  3    print(8)
   20   | ret 0
        |
       8  #print
  4     print(7)
    19  | ret 0
        |
       7 
  5     print(6)
    18  |ret 0
        |
       6
 6     print(5)
   17     | ret 0
        |
        5
 7      print(4)
   16     | ret 0
        |
        4
 8       print(3)
   15      |ret 0
        |
        3
 9       print(2)
   14     |ret 0
        |
        2
 10    print(1)
   13    | ret 0
       |
       1
11    print(0)
   12     ret 0
"""

def print_n_numbers_reverse(n):
    if n == 0:
        return 0
    else:
        print_n_numbers_reverse(n-1)
        print(n, end= ",")
        

print(print_n_numbers_reverse(10))
#1,2,3,4,5,6,7,8,9,10,None

""" 
 1    print(10)
     | ret 0
     |print 10
     |
 2   print(9)
     | ret 0
     |print 9
     |
 3   print(8)
     | ret 
     |print 8
     |
 4   print(7)
     | ret 
     |print 7
     |
 5   print(6)
     | ret 0
     |print 6
     |
 6   print(5)
     | ret 0
     |print 5
     |
 7   print(4)
     | ret 0 
     |print 4
     |
 8   print(3)
     | ret 0
     |print 3
     |
 9   print(2)
     |ret 0
     |print 2
     |
 10  print(1)
     |ret 0
     |print 1
     |
 11   print(0)
    ret 0

"""


def add_digits(n):
    if n < 10:
        return n
    else:
        return add_digits(n // 10) + (n % 10)

print("add digits", add_digits(326))
#11

"""
    1    add(326)
     8   |ret 11
        |
   2     add(326//10) == 32
     7   | ret 5 + 326 % 10 (6) = 11
        |
   3      add(32//10)  == 3
     6   | ret 3 +  32 % 10 (2) = 5
        |
   4     add(3//10)
     5   ret 3
  
  
"""

def reverse_sequence(S, lo, hi):
    if lo < hi:
        S[lo], S[hi] = S[hi], S[lo] 
        reverse_sequence(S, lo+1, hi-1)
   

A= [4,3,6,2,8,9,5]
reverse_sequence(A, 0, 6)
print("reversed", A)

def print_digits_reversed_vert(n):
    if n < 10:
        print(n)
    else:
        print(n % 10)
        print_digits_reversed_vert(n // 10)


print(print_digits_reversed_vert(1234))


#4
#3
#2
#1
"""  
   1    print(1234)
         |
         |
         1234 % 10 = 4  #print
   2      print(123) #1234//10
         |
         |
         123 % 10 = 3  #print
   3     print(12)  #123//10 
         |
         |
        12 % 10 = 2  # print
   4     print (1)   #12//10
         |
         1 (n < 2)  #print
         

"""

def product(a, b):
    if a < b:
        return product(b,a)
    elif b != 0:
        return a + product(a,b-1)
    else:
        return 0
    
print("product of two numbers 4 and 5 is", product(4,5))
#product of two numbers 4 and 5 is 20

"""
  1          product(4,5)
            | ret 20
            |
  2                ret product(5,4)
            | 
            |
  3          5 + product(5,3)
     11     | ret 5 + 10 = 20
            |
  4          5 + product(5,2)
     10     | ret 5 + 10 = 15
            |
  5          5 + product(5,1)
     9      | ret 5 + 5 = 10
            |
  6          5 + product(5,0) 
   7             ret 0
    8         ret 5

"""


def max_item_in_list_DAC1(A):
    if len(A) == 1:
        return A[0]
    else:
        middle = len(A) // 2
        m1 = max_item_in_list_DAC1(A[0:middle])
        m2 = max_item_in_list_DAC1(A[middle:len(A)])
        return max(m1, m2)

A = [23, -1, 5, 56]
print("max_list_length_DAC1", max_item_in_list_DAC1(A))

#max_list_length_DAC1 56

"""
         1      max(23,-1,5,56), mid=4//2=2
              /  m1=22,m2=56 ret 56   \
             /      14                 \
            /                           \
  2    max(22,-1),mid=2//2=1      8     max(5,56), mid=2/2=1
      /  m1=22,m2=-1 \                /  m1=5 m2=56 ret=56 \ 
    /   7 ret 22        \             /         13          \
   /                   \       9   max(5)             11    max(56)
3  max(22),   5  max(-1)       10  ret 5              12    ret 56
4 ret 22      6   ret -1
        
"""

def max_item_in_list_DAC2(A, lower, upper):
    if lower == upper:
        return A[lower]
    else:
        middle = (upper + lower) // 2
        m1 = max_item_in_list_DAC2(A, lower, middle)
        m2 = max_item_in_list_DAC2(A, middle +1, upper)
        return max(m1, m2)

A = [23, -1, 5, 5, 4, 2, 7]
print("max_list_length_DAC2", max_item_in_list_DAC2(A, 0, len(A)-1))
#max_list_length_DAC2 23

def is_even(n):
    if n==0:
        return True
    elif n == 1:
        return False
    else:
        return is_even(n-2)

print("is 4 even", is_even(4))
print("is 3 even", is_even(3))
#is 4 even True
#is 3 even False

""" 
 1    is_even(4)   1    is_even(5)
 6    |ret True     6  | ret False
     |                 |
 2   is_even(2)    2     is_even(3)
  5   | ret True    5   |ret False
     |                 |
 3    is_even(0)   3    is_even(1)
 4    ret true      4   ret False
    
"""


#non-negative exponents
def power_is(b, n):
    if n==0:
        return 1
    else:
        return b * power_is(b, n-1)

print("power is", power_is(2, 3))
#power is 8

"""
 1   power(2,3)
  8  |ret 2 * 4 = 8
     |
 2    power(2, 2)
  7   |ret 2 * 2 = 4
     |
 3    power(2, 1)
  6   |ret 2 * 1 = 2
     |
 4    power(2, 0)
  5   ret 1

"""

def power_alt(x, y):
    if y == 0:
        return 1
    elif y % 2 == 0:
        return power_alt(x, y//2) * power_alt(x, y//2)
    else:
        return (x * power_alt(x, y//2)) * power_alt(x, y//2)

x = 2
y = 3
print("power alt is ", power_alt(x,y))
# power alt is  8


def decimal_to_binary(n):
    if n < 2:
        return n
    else:
        return 10 * decimal_to_binary(n//2) + (n % 2)

print("Decimal to binary", decimal_to_binary(8))
#Decimal to binary 1000
"""
    1. d2B(8)
    | return 1000
    |
    2. 10 * d2B(4)
    |8. 10 * 100 + 100 % 2 = 1000
    |
    3. 10 * d2B(2)
    |7. 10 * 10 + 10 % 2 = 0 = 100
    |
    4. 10 * d2B(1) 
    <2
        6. 10* 1 + 1%2 = 1 = 10
    5. return 1
    

"""


def decimal_to_base(n, b):
    if n < b:
        return n
    else:
        return 10 * decimal_to_base(n // b, b) + (n % b)

print("decimal to base", decimal_to_base(1024,2))
#decimal to base 10000000000


#Strings
def reverse_string(s):
    if len(s) == 1:
        return s[0]
    else:
        return reverse_string(s[1:]) + s[0]

print("reversing a string",  reverse_string("jimmie"))
#reversing a string eimmij

"""    
1   reverse(jimmie)
 12 |ret eimmi + j = eimmij 
    |
2    reverse(immie)
 11 |ret eimm + i = eimmi
    |
3    reverse(mmie)
 10 |ret eim + m = eimm
    |
4    reverse(mie)
 9  |ret ei + m = eim
    |
5    reverse(ie)
 8  |ret e + i = ei
    |
6    reverse(e), len=1
 7  ret e

"""


def is_palindrome(s):
    n = len(s)
    if n <=1:
        return True
    else:
        return s[0] == s[n-1] and is_palindrome(s[1:n-1])

print("is palindrome nayan", is_palindrome("nayan"))
print("is palindrome kasam", is_palindrome("kasam"))
#is palindrome nayan True
#is palindrome kasam False

"""
1 is_pal(nayan)                    1  is_pal(kasam)
       | ret True                     | 
       |                              |
2 [n]==[n]:true and is_pal(aya)      [k]==[m] 
  5   |  ret True                      ret False
      |
3 [a]==[a]:true and is_pal(y)
 4 ret True
"""


#consider dynamic programming
def longest_palindromic_substring(s):
    n = len(s)
    if is_palindrome(s):
        return s
    else:
        aux1 = longest_palindromic_substring(s[1:n])
        aux2 = longest_palindromic_substring(s[0:n-1])
        if len(aux1) > len(aux2):
            print(aux1)
            return aux1
        else:
            print(aux2)
            return aux2
        print("aux3")

print("longest palindromic substring is", longest_palindromic_substring("yayi"))
#longest palindromic substring is nayan

#the length is checked in case there are two palindromes returned

"""
              
  
                 1 yayi
               / 13.ret \
               /    yay  \
              /           \
             /             \
          2 ayi             12  yay
          /      \          aux2 = "yay" 
         /11.ret a\
        /          \
       3  yi          7 ay
      / 6   \              /  \
     / ret y \            /    \
    /         \          / 10.  \
   /          \        /ret a    \
  /            \      /           \
  4           5 y      /           \
  aux1=i      aux2=y   8 y         9 a
                    aux1=y        aux2=a             
"""              


def equal_strings(s,t):
    if len(s) != len(t):
        return False
    elif s == '':
        return True
    else:
        return s[0] == t[0] and equal_strings(s[1:], t[1:])

print("strings joe and joe are equal", equal_strings( "joe", "joe"))
print("strings smith and joe are equal", equal_strings( "smith", "joe"))
#strings joe and joe are equal True
#strings smith and joe are equal False

def equal_strings_tail(s, t):
    if len(s) != len(t):
        return False
    elif s == '':
        return True
    elif s[0] != t[0]:
        return False
    else:
        return equal_strings_tail(s[1:], t[1:])
    
"""
 1       equal(mary, mary)       1  equal(mary, joe)
   10     | ret True               |
         |                          |
 2       equal(ary, ary)            len(mary)=4, len(joe)=3 
   9     | ret True                 ret False
        |
 3       equal(ry, ry)
   8     | ret True
        |
 4       equal(y,y)
   7     |ret True
        |
 5       equal('','')
   6      ret True


"""


print("strings mary and mary are equal", equal_strings_tail( "mary", "mary"))
print("strings mary and joe are equal", equal_strings_tail( "mary", "joe"))
#strings mary and mary are equal True
#strings mary and joe are equal False

def occurrences_in_list(A, x):
    if A == []:
        return 0
    else:
        return int(A[0] == x) + occurrences_in_list(A[1:],x)

A=[1,2,5,2,3,2]
print("occurrences_in_list", occurrences_in_list(A,3))
#occurrences_in_list 2

"""
               occ(1,2,5,2,3,3), 2
               |ret 2
               |
               (1==2)=0 + occ(2,5,2,3,3),2
               |ret 2
               |
               (2==2)=1 + occ(5,2,3,3),2
               |ret 1 + 1 = 2
               |
               (5==2)=0 + occ(2,3,3), 2
               |ret 1
               |
               (2==2)=1 + occ(3,3), 2 
               |ret 1
               |
               (3==2) + occ(3), 2
               |ret 0
               |
               (3==2) + occ(), 2
               ret 0
                 
                 
"""
def linear_search_list_tail(A, x):
    n = len(A)
    if A==[]:
        return -1
    elif A[n-1] == x:
        return n-1
    else:
        return linear_search_list_tail(A[:n-1], x)


A=[1,34,5,12,4,23,2]
print("linear search in list", linear_search_list_tail(A,34))
#linear search in list 6

"""
            A[2]==34 search(1,34,5,12,4,23,2), n=7
            |return 1
            |
            A[23]==34 seach(1,34,5,12,4,23), n=6
            |ret 1
            |
            A[4]==34, search(1,34,5,12,4),  n=5
            |ret 1 
            |
            A[12]==34 search(1,34,5,12), n=4
            |return 1 
            |
            A[5]==34 search(1,34,5)  n=3
           |return 1
           |
           A[34]==34  search(1,34)  n=2
           return n-1 = 1
"""



def linear_search_linear(A, x, n):
    if A == []:
        return -n-1
    elif A[0] == x:
        return 0
    else:
        return 1 + linear_search_linear(A[1:], x, n)


A=[1,34,5,12,5,23,2]
n = len(A)
print("linear search in list", linear_search_linear(A, 12, n))
#linear search in list 3
print("linear search in list", linear_search_linear(A, 15, n))
#linear search in list -1

def linear_search_tail_2(A, x, n):
    if A == []:
        return -1
    elif A[0] == x:
        return n
    else:
        return 1 + linear_search_tail_2(A[1:], x, n+1)


A=[1,34,5,12,4,23,2]
n = len(A)
print("linear search in list", linear_search_linear(A, 23, n))
#linear search in list 5
print("linear search in list", linear_search_linear(A, 11, n))
#linear search in list -1

def binary_search(A, x, lower, upper):
    if lower > upper:
        return -1
    else:
        middle = (lower + upper) // 2
        if x== A[middle]:
            return middle
        elif x < A[middle]:
            return binary_search(A, x, lower, middle-1)
        else:
            return binary_search(A, x, middle+1, upper)

bb=[1, 3, 7, 22, 33, 44, 55, 56, 78]
print("binary search in a list" , binary_search(bb, 56, 0, len(bb)-1))
#binary search in a list 7

"""
                 bs(1,3,7,22,33,44,55,56,78), x=56  0+8//2 = 4
                                \          
                                 \  56 > 33 (A[4]), 
                            bs(44, 55, 56,78)  x=56, 5+8//2 = 6
                                 \
                                  \ 56 > 55 (A[6])
                           bs(56, 78)  x = 56, 7+8//2 = 7
                                \
                                 \ 56 == 56  x==(A[7])
                              return 7
    
"""

def flatten(A):
    if A == []:
        return A
    if isinstance(A[0], list):
        return A[0] + flatten(A[1:])
    else:
        return [A[0]] + flatten(A[1:])

A = [1,[1,2],[3],4, [3,4]]

print("Flattened list is ", flatten(A))


def get_smaller_than_or_equal_to(A, x):
    if A == []:
        return []
    elif A[0] <= x:
        return [A[0]] + get_smaller_than_or_equal_to(A[1:], x)
    else:
        return get_smaller_than_or_equal_to(A[1:],x)

AA = [9,6,1,7,4,5]
print("get smaller than 5", get_smaller_than_or_equal_to(AA, 5))
#get smaller than 5 [1, 4, 5]

def get_greater_than(A, x):
    if A == []:
        return []
    elif A[0] > x:
        return [A[0]] + get_greater_than(A[1:],x)
    else:
        return get_greater_than(A[1:],x)

AB = [9,6,1,7,4,5]
print("get greater than 5", get_greater_than(AB, 4))
#get greater than 5 [9, 6, 7, 5]


def is_list_sorted(A,n):
    if n == 1:
        return True
    elif A[n-1] <= A[n-2]:
        return False
    else:
        return is_list_sorted(A,n-1)
        

AZ = [1,3,5,6,8]
n=len(AZ)
print("is list sorted", is_list_sorted(AZ, n))
#is list sorted True

"""
  1    is_sorted(1,3,5,6,8),5
    9  |ret True
       |
       | 8 <= 6, nope
  2    is_sorted(1,3,5,6,8),4
    8  |ret True
       |
       | 6 <= 5 nope
  3    is_sorted(1,3,5,6,8),3
    8   |ret True
       |
       | 5 <= 3 nope
  4    is_sorted(1,3,5,6,8),2
    7   | ret True
       |
       | 3 <= 1 nope
  5    is_sorted(1,3,5,6,8),1
    6   ret True
       
"""

def select_sort_rec(a):
    if len(a) <= 1:
        return a
    else:
        b = list(a)
        m = min(b)
        b.remove(m)

        return [m] + select_sort_rec(b)

A = [7,5,23,3,8,4]
print(select_sort_rec(A))

"""
     1. sort(7,5,23,3,8,4)
     |  13. return [3,4,5,7,8, 23]
     |
         b = [7,5,23,3,8,4]
         m = 3
         b = [7,5,23,8,4]
     |
     2. [3] + sort(7,5,23,8,4)
     | 12. return [3,4,5,7,8,23]
     |  
         b = [7,5,23,8,4]
         m = 4
         b = [7,5,23,8]
     |
     3. [4] + sort(7,5,23,8)
     |  11. return [4,5,7,8, 23]
     |
         b = [7,5,23,8]
         m = 5
         b = [7,23,8]
     | 
    4. [5] + sort(7,23,8)
    | 10. return [5, 7, 8, 23]
    |
        b = [7,23,8]
        m = 7
        b = [23,8]
    |
    5. [7] + sort(23,8)
    |  9. return [7,8,23]
    |
        b = [23,8]
        m = [8]
        b = [23]
    |
    |
    6. [8] + [23]
    | 8. return [8,23] 
    |
    |
    7.return 23 

"""


def select_sort_rec_1(a):
    if len(a) <= 1:
        return a
    else:
        b = list(a)
        min_indx = b.index(min(b))
        aux = b[min_indx]
        b[min_indx] = b[0]
        b[0] = aux

        return [aux] + select_sort_rec_1(b[1:])

A = [7,5,23,3,8,4]
print(select_sort_rec_1(A))

def merge_sort(A):
    n = len(A)
    if n <= 1:
        return A
    else:
        m1 = merge_sort(A[0:n//2])
        m2 = merge_sort(A[n // 2: n])
        return merge(m1, m2)

def merge(a, b):
    if a == []:
        return b
    if b == []:
        return a
    else:
        if a[0] < b[0]:
            return [a[0]] + merge(a[1:],b)
        else:
            return [b[0]] + merge(a, b[1:])

AX = [7,3,4,5,6,33,3,6]
print("merge sort list is ", merge_sort(AX))
#merge sort list is  [3, 3, 4, 5, 6, 6, 7, 33]
                       
"""
44 step journey to sort 8 numbers. Journey includes return steps too.


                   1 msort(7,3,4,5,6,33,3,6) n=8.
                   /        44 r                \
                  /                              \
    2 msort(7,3,4,5)                              22 msort(6,33,3,6)
          /  21r   \                                /      41 r      \
         /          \                              /                  \
   3 msor(7,3)     11 msrot(4,5)           23 msort(6,33)           31 msort(3,6)
   /  10 r   \            | 18r \              /  30r   \             /   38 r   \
  /           \           |      \            /          \          32 msort(3)   34 msort(6)
 4 msort(7) 6 msort(3) 12 ms(4)  14 ms(5)  24 msort(6) 26 msort(33)  33 rm1=3     35  ret m2=6
5ret m1=7    7ret m2=3  13r m1=4 15r m2=5  25 r m1=6  27 m2=33        \            /
     \       /              \      /           \         /             \          /
      \     /                \    /             \       /             36 merge(3,6) 
    8 merge(3,7)           16 merge(4,5)  28 merge(6,33)             37 r [3,6]
    9 ret [3,7]             17 r[4,5]      29 r [6,33]                /
         \                  /                         \              /
          \                /                           \            /
             19 merge([3,7],[4,5])                  39  merge([6,33],[3,6])
             20 ret [3,4,5,7]                        40     ret [3,6,6,33]
                            \                      /
                             \                    /
                         42 merge([3,4,5,7],[3,6,6,33])
                          43 ret [3,3,4,5,6,6,7,33]     
"""                   


def pascal(n):
    if n==0:
        return [1]
    else:
        row = [1]
        previous_row = pascal(n-1)
        for i in range(len(previous_row)-1):
            row.append(previous_row[i] + previous_row[i+1])
        row.append(1)
    return row

print(pascal(8))
#[1, 8, 28, 56, 70, 56, 28, 8, 1]



#ABC -->0/0 --> call rec ABC
    #-->1/1 -->call ABC  2/2 call ABC [l==r match, print (ABC)]
    #ABC
    #-->2/1 -->call ACB  2/2 call ACB [l==r match print (ACB) ]
#ABC --> ABC

#ABC -->1/0 --> call rec  BAC
     #-->1/1 -->call BAC  2/2 Call BAC [l==r match print (ABC)]
     #BAC
     #-->2/1 -->call ACB  2/2 Call BCA [l==r matchprint (BCA)]
#BCA --> ABC

#ABC -->2/0 --> call rec CBA
    #-->1/1 -->call CBA  2/2 Call CBA [l==r match print (CBA)]
    #CBA
    #-->2/1 -->call CAB  2/2 Call CAB [l==r match print (CAB)]
#CBA --> ABC

def perm_of_list(A, l, r):
    if l==r:
        print(A)
    else:
        for i in range(l, r+1):
            A[l], A[i] = A[i], A[l]
            perm_of_list(A, l+1, r)
            A[l], A[i] = A[i], A[l]


B="ABC"
n = len(B)
A = list(B)
perm_of_list(A, 0, n-1)
"""
                 1 permutation of    (ABC)
               /         \                 \
      swap 0/0/   swp 1/0 \         swp 2/0 \ 
             /             \                 \ 
        2 ABC              5  BAC           8   CBA 
         /    \            /     \             /     \ 
swap 1,1/  2/1 \      1/1 /   2/1 \       1/1 /    2/1\ 
       /        \        /         \         /         \
  3 ABC      4 ACB     6 BAC   7 BCA     9  CBA     10  CAB
     |         |        |        |          |           |
 2/2 |    2/2  |    2/2 |    2/2 |      2/2 |       2/2 |
     |         |        |        |          |           |
   prnt       prnt     prnt     prnt        prnt       print
 


"""

#Catalan numbers
"""
C0 = 1 and  Cn+1 = for i to n summation of (Ci * Cn-1)
C4 = C0C3 + C1C2 + C2C1 + C3C0
"""
def catalan(n):
    if n <= 1:
        return 1

    res = 0
    for i in range(n):
        res += catalan(i) * catalan(n-i-1)

    return res

print("catalan numbers: ", end= "")
for i in range(10):
    print(catalan(i), end= " ")
print()
#output: 1 1 2 4 14 42 132 429 1430 4862



#Binomial Coefficient
#gives number of ways, disregarding order,
#that k object can be chosen from among n objects.
#formally k element subset of n element set
def binomialCoeff(n, k):

    if k == 0 or k == n:
        return 1

    return binomialCoeff(n-1, k-1) + binomialCoeff(n-1, k)

n = 5
k = 2
print("binomial Coeff of n=5, k=2 is", binomialCoeff(n, k))

"""   
                   1    binCoef(5,2)
                     /     38 r10     \ 
                    /                   \
                   /                      \ 
          2  binCoeff(4,1)                16  binCo(4,2)    
           / 15 et 4  \                     /   37 r6      \
          /            \                   /                \
         /              \                 /                  \
  3  binCoeff(3, 0)  5 binCo(3,1)       17 bin(3,1)            27  bin(3,2)
   4 r1             / 14 r3 \           /   26 r3  \              /   36 r3 \
                   /         \         /            \            /           \
                  /           \       /              \          28  b(2,1)     34 b(2,2)
      6 binCo(2,0)   8 binC(2,1)  18 binC(2,0)  20 b(2,1)          /33 r2 \    35 r1
      7   r1          / 13 r2 \    19  r1      / 25 r2 \          /        \
                     /         \              /         \        /          \
                    /           \          21 b(1,1)  23 b(1,1) /            \
           9 bin(1,1)    11 bin(1,1)       22  r1    24 r 1    /              \
            10  r1       12  r1                               /                \
                                                            29 b(1,1)       31 b(1,1)
                                                            30 r1           32 r1
                
"""

#Stair Climbing Puzzle
#A child is climbing up stairs with n steps. Can hop 1,2,3 steps at a time
#Count how many possible ways the child can jump the stairs

def steps_possible(n):
    if n < 1:
        return 0
    return 1 + steps_possible(n-1) + steps_possible(n-2) + steps_possible(n-3)

print("Possible ways a child can jump", steps_possible(3))

"""
            1               steps_possible(3)   
                /              r = 1+2+1+0=4                        \ 
               /                        |                            \ 
              /                         |                             \
            2   steps_possible (2)       9 steps_possible(1)        13 steps(0)
          /   ret 1+1+0+0  | \            | ret 1 +0+0+0    \       ret 0
         /                 |  \           |          \       \
        /                  |   \          |           \       \
    3  steps_poss(1) 7steps(0)  \          10 st(0), 11 st(-1), 12 st(-2)
      / ret 1 |    \   ret 0   8 steps(-1)  ret 0     ret 0     ret 0
4    /        |      \           ret 0
steps(0) 5 steps(-1)  6 st(-2)
ret 0    ret 0          ret 0
             

"""


#Dynamic programming
#coin change problem
# N = 4, s = {1,2,3} there are four solutions: {1,1,1,1}, {1,1,2}, {2,2}, {1,3}
#output should be 4.
def count(S, m, n):

    if n == 0:
        return 1

    if n < 0:
        return 0

    if m <= 0 and n >= 1:
        return 0

    return count(S, m-1, n) + count(S, m, n-S[m-1])

arr=[1,2,3]
m = len(arr)
print("coin change counts", count(arr, m, 4))




#output 4:
"""
                              C(1,2,3),3,4
                            /       r4       \
                           /                  \
                    C(123),2, 4                 C(123),3,4-S[3-1]=1
                     /   r3   \                      /    r1           \
                    /          \                     C(123),2,1         C(123),3, 1-S[3-1]
          C(123),1, 4      C(1,2,3),2 4-S[2-1]=2      /  r1    \              /  r0   \
        /  r1  \          /  r2     \                 C(123),1,1 ...         /         \
       /       \      C(123),1,2  C(123),2,2-S[2-1]=0   / r1                /          C(123),3,-2
 C(123),0, 4  C(123),1, 4-S[1-1]=3  /   r1    \        R0              C(123),2, -   ret 0
 ret 0       / r1 \     C(1,2,3),0,2  C(123),1,2-S[1-1]=1               ret 0
            /      \    r0            /  r1  \               
   C(123),0,3 C(123),1,3-S[1-1]=2    /        \                   
   ret 0        / r1   \      C(123),0,1  C(123),1,1-S[1-1]=0      
               /       \     ret 0        ret 1                     
    C(123) 0, 2  C(123), 1, 2-S[1-1]=1                   
    ret 0        /  r1   \                              
                /         \
       C(123),0,1    C(123),1, 1-S[1-1]=0
       ret 0           ret 1
                        
                      
"""
print("print all subsets or combinations")
def print_subsets(n, curr, res):
    if curr == 0:
        print(res)
        return
    
    for i in range(1, n+1):
        if i <= curr:
            print_subsets(n, curr-i, res+str(i))
    
print_subsets(4,4,"")
""" 
                      1   ss(4, "")       
                     /            |               \                 \
                    /             |                \                 \
      2   ss(3,"1")            10 ss(2, "2")  15 ss(1,"3")  17 print(0,"4")
          /      | \                      |           \ 
         /       |  \                     |            \
        /        |  9 print(0, "13")      |             \ 
       /         |                        |            16 print(0,"31")
 3 ss(2,"11")  7 ss(1, "12")              |         
     /      \              \              |\         
    /        \              \             | \     
4 ss(1 "111") \      8   print(0,"121")   |  \
 |         6 print(0,"112")               |   \
 |                             11 ss(1,"21")   14 print(0,"22")
 |                                   |       
5 print(0, "1111")                   |
                                13 print(0,"211")


o/p
1111
112
121
13
211
22
31
4
"""


# Consider Dynamic Programming
#Subset of sum problem
# Given a set of non-negative integers and a value sum,
# determine if there is a subset of a given set with sum equal to sum

def isSubsetSum(set, n, sum):

    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False

    if set[n-1] > sum:
        return isSubsetSum(set, n-1, sum)

    return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1])

set = [1, 2, 1]
sum = 4
n = len(set)
if isSubsetSum(set, n, sum) == True:
    print("Found a subset with given sum")
else:
    print("No subset with given sum")

#output Found a subset with given sum
"""
              3 4  (n=3-1=2, sum=4)
            /      r=True      \
           2 4                  2   3
         / F   \               /    T   \
       1 4     1 2 (4-2=2)    1 3        1  1  (n-1=1, 3-set[1]=1)
      / F \    / F   \       /  \       / T  \
    0 4  0 3  0 2   0 1    0 3  0,2   0 1   0  0
    rF   rF   F     F      F    F       F     T
                   
"""

#Longest common subsequence
#consider dynamic programming
def lcs(X, Y, m, n):

    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))

X = 'AXYT'
Y = 'AYZX'
print("Length of LCS is ", lcs(X, Y, len(X), len(Y)))

#output of LCS is 2  (AY)
""" Partial recursive tree for LCS

                                lcs(AXYT,       AYZX)
                                 /                      \ 
                                /                        \ 
                   lcs(AXY,        AYZX)                  lcs(AXYT,  AYZX)
               /                         \                    /            \ 
              /                            \                  /               \ 
        lcs(AX,        AYZX)                lcs(AXY, AYZ)   lcs(AXY, AYZX)      lcs(AXYT, AY)
        /          r1         \               \            /          \                /   \ 
       /                      \                 \...       /           \               /    \ 
      lcs(A, AYZX)             lcs(AX, AYZ)              lcs(AX, AYZX)  lcs(AX, AYZ)   ..     ..
     /     r1    \               /   r1     \           return 1             \ 
    /             \             /            \                                \ 
lcs("", AYZX)   lcs(A, AYZ)    lcs(A, AYZ)     lcs(AX, AY)                     lcs(AX, AY)
return 0       /  r1     \        /      \      /   r1     \                     /          \ 
              /         \    lcs("", AYZ)  ..    /           \                     /          \ 
    lcs("", AYZ)  lcs(A, AY) return 0        lcs(A, AY)      lcs(AX, A)           lcs(A, AY)   lcs(AX, A)
     return 0     /   r1  \                 /  r1   \          /    r1  \           /               \ 
                /           \               /       \         /          \         lcs("", AY)  lcs(AX, "")
        lcs("", AY)    lcs(A, A)   lcs("", AY)   lcs(A, A)  lcs(A, A) lcs(AX, "") return 0     return 0
        return 0        return 1    return 0      return 1  return 1  return 0
        
"""

#Cutting rod

def cutRod(price, n):
    if n <= 0:
        return 0
    max_val = float("-inf")

    for i in range(0,n):
        max_val = max(max_val, price[i] + cutRod(price, n-i-1))
    return max_val

arr = [1, 5, 8, 9]
size = len(arr)
print("Max obtainable value is ", cutRod(arr, size))

#Max obtainable value is 10
"""
                           cR(4)
                /                 \         \                \
               /                   \         \                \
           cR(3) i=0             cR(2)i=1     cR(1)i=2       cR(0)i=3
            r5                      r= 5+1     r8+0    \     r0
         /      \       \            |          |       \
        /        \       \           |          |        \
      cR(2)i=0 cR(1)i=1   cR(0)i=2   cR(1)i=0  cr(0)i=0  cR(0)i=1
     / r1 \          \                |1+0     r0        r0
    /      \          \               |
   cR(1)i=0 cR(0)i=1   cR(0)i=0      cR(0)i=0
   / r1+0  r0           r0           r0
  /
 cR(0)
 r0
"""

#Friends Pairing:
#Given n friends, each one can remain single or can be paired up with some other
#friend. Each friend can be paired only once.
# Find out the total number of ways in which friends can remain single or paired up
#{1}, {2}, {3} -- all single
#{1}, {2,3} : 2 and 3 paird but 1 is single
#{1,2}, {3} : 1 and 2 are paired but 3 is single
#{1,3}, {2} : 1 and 3 are paired but 2 is single
#{1,2} and {2,1} are same.
def countFriendsPairings(n):

    if n <= 1:
        return 1
    return countFriendsPairings(n-1) + ((n-1)  * countFriendsPairings(n-2))

n = 3
print(countFriendsPairings(n))

# output 4.  for n = 4, output 10, for n = 5, output is 26

#find a peak element - use binary search

def findpeak(A, low, high, n):

    mid = low + (high-low)/2
    mid = int(mid)

    if mid == 0 or A[mid-1] <= A[mid] and \
        (mid == n-1  or A[mid+1] <= A[mid]):
            return mid

    elif mid > 0 and A[mid-1] > A[mid]:
        return findpeak(arr, low, mid-1, n)

    else:
        return findpeak(arr, mid+1, high, n)

A = [1,3,20,4,1,0]
print("index of a peak point is", findpeak(A, 0, n-1, n))
#index of a peak point is 2
