#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 16:09:22 2019

@author: kdp
"""

#lo, hi. 
#while lo < hi. swap.
def ReverseString(Astring):
    lo = 0
    Alist = []
    for letter in Astring:
        Alist.append(letter)
    hi = len(Alist)-1
    while lo < hi:
        Alist[lo], Alist[hi] = Alist[hi], Alist[lo]
        lo+=1
        hi-=1
    print("".join(Alist))
    
Astr = "repeated"
ReverseString(Astr)

#Pythonic way: 
print(Astr[::-1])

print() 
# Word count using dictionary
def wordCount(sentence):
    adict = {}
    alist = sentence.split(" ")
    for word in alist:
        if word in adict:
            adict[word] += 1
        else: 
            adict[word] = 1
    print(adict)
    

sentence = "Mary Mary had a little little lamb"
wordCount(sentence)
#{'Mary': 2, 'had': 1, 'a': 1, 'little': 2, 'lamb': 1}

print()
#count words
def wordCount(sentence):
    alist = sentence.split(" ")
    wordCount = len(alist)
    return wordCount
       
sentence = "Mary had a little lamb"
print("Mary had a little lamb has", wordCount(sentence), "words")
#Mary had a little lamb has 5 words

print()
#first repeated word using dictionary
def FirstRepeatedChar(sentence):
    adict = {}
    alist = sentence.split(" ")
    for word in alist:
        if word in adict:
            adict[word] += 1
        else: 
            adict[word] = 1
    print(adict)
    
    for key, item in adict.items():
        if item > 1:
            print(key, "is the first repeated word")
            return
        
sentence = "Mary had a little little lamb"
FirstRepeatedChar(sentence)
#{'Mary': 1, 'had': 1, 'a': 1, 'little': 2, 'lamb': 1}
#little is the first repeated word


#Print all substrings in a string
def print_all_substrings(str1):
    for i in range(len(str1)):
        for j in range(i, len(str1)):
            print(str1[i:j+1])

print_all_substrings("ABC")
"""
A
AB
ABC
B
BC
C
"""


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
print()
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
 
output
['A', 'B', 'C']
['A', 'C', 'B']
['B', 'A', 'C']
['B', 'C', 'A']
['C', 'B', 'A']
['C', 'A', 'B']

"""


print()
#first non repeated word
def FirstNonRepeatedChar(sentence):
    adict = {}
    alist = sentence.split(" ")
    for word in alist:
        if word in adict:
            adict[word] += 1
        else: 
            adict[word] = 1
    print(adict)
    
    for word in alist:
        print(word)
        if adict.get(word) == 1:
            print(word, "is the first non repeated char")
            return
        
sentence = "Mary Mary had a little little lamb"
FirstNonRepeatedChar(sentence)
#{'Mary': 2, 'had': 1, 'a': 1, 'little': 2, 'lamb': 1}
#had is the first non repeated char


#reverse words in a sentence
#split the sentence into a list
#lo, hi, 
#while lo < hi:, swap alist[lo], alist[hi] 
def reverseWordsInSentence(sentence):
    alist =sentence.split()
    hi = len(alist)-1
    lo = 0
    while lo < hi:
        alist[lo], alist[hi] = alist[hi], alist[lo]
        lo+=1
        hi-=1
    print(" ".join(alist))
    
sentence = "Mary had a little little lamb"
reverseWordsInSentence(sentence)
#lamb little little a had Mary


#hash function
#for each char, sum = [sum*"Fixed number"*ascii(i) ] mod wordLength
def stringHash(A):
    sum=0
    Kmul = 997
    n = len(A)
    for i in range(0, n):
        sum = (sum * Kmul + ord(A[i])) % n  
    print(sum)

A = "repeatedly"
stringHash(A)
#9

#group  by
from itertools import groupby
def fistCharsofConsChars(aStr):
    n = len(aStr)
    al = []
    al.append(aStr[0])
    for i in range(1, n):       #n=7 so it will compare 6th val
        if aStr[i] != aStr[i-1]:
            al.append(aStr[i])
        else:
            pass
    newStr = ""
    newStr = "".join(al)
    print(newStr)
    
    #python way
    result = []
    for (key,group) in groupby(aStr):
        result.append(key)
    print (''.join(result))
    
aStr = 'aaaaabbbbbbc'
fistCharsofConsChars(aStr)   


# Leader in election
import itertools
def winnerOfElection(Votes):
    
    votesDict = {} 
    
    for i in Votes:    
        if i in votesDict:
            votesDict[i] +=1
        else:
            votesDict[i] = 1
    max =0
    Elected  = ""        
    for key, value in votesDict.items():
        if value > max:
            max = value
            Elected = key
        
    print(max, "max votes received by", Elected )
    
    #Python way
    Votes.sort()
    for (key,group) in itertools.groupby(Votes):
        print (list(group))
    
    return max
        
Votes = ["Ketan", "Ketan", "Dulari", "Dulari", "John", "Megha", "Reena",
         "Sangita", "Anuja", "Ketan"] 
winnerOfElection(Votes)  


#Reverse only vowels
def reverseVowels(aStr):
    lo = 0
    vowels = ['a', 'i', 'e', 'o', 'u']
    hi = len(aStr)-1
    alist = list(aStr)
    while lo < hi:
        if alist[lo] in vowels and alist[hi] in vowels:
            alist[lo], alist[hi] = alist[hi], alist[lo]
            lo+=1
            hi-=1
        elif alist[lo] in vowels and alist[hi] not in vowels:
            hi-=1
        elif alist[lo] not in vowels and alist[hi] in vowels:
            lo+=1
        elif alist[lo] not in vowels and alist[hi] not in vowels:
            lo+=1     
            hi-=1
    print("".join(alist))
    return
            
A = "facetious"
reverseVowels(A)


#Common chars - Pythonic
from collections import Counter
def commonChars(aStr, bStr):
    
    alist = Counter(aStr)
    blist = Counter(bStr)
    commonDict = alist & blist
    commonChars = list(commonDict.elements())
    print("".join(commonChars))
    
A = "geeks"
B = "beGeeks"
commonChars(A, B)  



#Mirror Strings
#mirror chars alphafter first n chars
def mirrorStrings(aStr, n):
    
     reverseDict =  {"z":"a", "a":"z", "y":"b", "b":"y", "x":"c", "c":"x", "d":"w", 
                     "w":"d", "v":"e", "e":"v", "f":"u", "u":"f","t":"g", "g":"t",
                     "s":"h", "h":"s", "i":"r", "r":"i","j":"q", "q":"j", "p":"k", 
                     "k":"p", "o":"l", "l":"o","n":"m", "m":"n"}
    
     ld = len(aStr)
     answer = []
     answer1 = aStr[0:n]
     for i in range(n, ld):
         answer.append(reverseDict.get(aStr[i]))
     result = answer1+ "".join(answer)
     print(result)
     return result
 
st = "pneumonia"
n = 4
answer =  mirrorStrings(st, n)


# Remove Dups, split string.
def removeDupsSplitString(string, k):
 
    len_temp = 0
    temp = []
    
    for item in string:
        len_temp +=1
        if item not in temp:
            temp.append(item)
        if len_temp == k:
            print(''.join(temp))
            temp=[]
            len_temp=0
    
    for item in temp:
        print(item)
            
removeDupsSplitString("AABCAAADA",3)
# output:  AB  CA  AD


#Char frequency sort
#sort by the frequency of the characters.
def charfrequencySort(A):
    dic = {}
    l = []
    for char in A:
        dic[char] = dic.get(char,0) + 1
    print(dic)
    
    for keys in sorted(dic, key=dic.get, reverse=True):
        print(dic[keys])
        for i in range(dic[keys]):
            l.append(keys)
    print("".join(l))    
    
A = "trrree"
charfrequencySort(A)
#rrreet
#{'t': 1, 'r': 3, 'e': 2}

# length of last word
def lengthofLastWord(A):
    
    lyst = A.split()
    n=len(lyst)
    for i in range(n-1,-1,-1):
        print(len(lyst[i]))
        return
    
A = "Hell World"
lengthofLastWord(A)
#5

# P=Present, A=Absent,  L=Late
def rewardStudent(A):
    n = len(A)
    absent=0
    if A.find('LLL') != -1:
        return False
    
    for i in range(0, n): 
        if A[i] == "A":   
            absent +=1
    
    if absent > 1:
        return False
    
    return True
    
A = "PALL"
print(rewardStudent(A))
#True

#Count of words
def Minion(s):
    n = len(s)
    
    vowelDict = {}
    ConsDict = {}
    
    vowel = {'a', 'e', 'o', 'i', 'u', 'A', 'E', 'O', 'I', 'U'}
    
    for i in range(n):
        for j in range(n+1):
            if s[i] in vowel:
                vowelDict[s[ i:j ]] = vowelDict.get(s[i:j],0) +1
            else:
                ConsDict[s[ i:j ]] = ConsDict.get(s[i:j], 0) + 1
         
    del vowelDict['']
    del ConsDict['']
    
    print(vowelDict)
    print(ConsDict)
    vowCount=0
    consCount=0
    for Vowval in vowelDict.values():
        vowCount = vowCount + Vowval
    for Consval in ConsDict.values():
        consCount = consCount + Consval
    
    if vowCount > consCount:
        print("VowelCount", vowCount)
        return
    elif vowCount < consCount:
        print("ConsCount", consCount)
        return
    else:
        print("draw")
    
s="banana" 
Minion(s)
#{'a': 3, 'an': 2, 'ana': 2, 'anan': 1, 'anana': 1}
#{'b': 1, 'ba': 1, 'ban': 1, 'bana': 1, 'banan': 1, 'banana': 1, 'n': 2, 'na': 2, 'nan': 1, 'nana': 1}
#ConsCount 12


#isString anagram - using sorting
def isAnagram(StrA, StrB):
    
    list1 = list(StrA)  
    list1.sort()     #[a,a,a,g,m,n, r] 
    list2 = list(StrB)
    list2.sort()    #[a,a,a,g,m,n,r]
    
    if list1 == list2:
        return True
    else:
        return False
        
stra = "anagram"
strb = "naagram"
isAnagram(stra, strb)
#True

#Anagram
def anagram(A):
    dict1={}
    for i in A:
       dict1.setdefault("".join(sorted(list(i))), []).append(i)
    for values in dict1.values():
        print(values, end=",")
    print()

A = ['cat','act', 'ate', 'eat', 'mary', 'orchestra', 'carthorse']
anagram(A)
#['cat', 'act'],['ate', 'eat'],['mary'],['orchestra'],

#Anagram
def anagram(A):
    dict1={}
    sum1 = 0
    for i in A:
        for x in i:
            sum1 += ord(x)
        dict1.setdefault(sum1, []).append(i)
        sum1 = 0
    print(dict1)
    #key is sum of asci chars
    #{312: ['cat', 'act'], 314: ['ate', 'eat'], 441: ['mary'], 971: ['orchestra']}

A = ['cat','act', 'ate', 'eat', 'mary', 'orchestra', 'carthouse']
anagram(A)
#{312: ['cat', 'act'], 314: ['ate', 'eat'], 441: ['mary'], 971: ['orchestra']}
#['cat', 'act']
#['ate', 'eat']
#['mary']
#['orchestra']


print()
#Compress String
#A5B35C3D1
St1 = "AAAAABBBBBCCCD"
count1 = 1
str1 = []
fs = St1[0]

for i in range(1, len(St1)):
    if St1[i] == fs:
        count1 +=1
    else:
        str1.append(fs) 
        str1.append(str(count1))
        fs = St1[i]
        count1 = 1

str1.append(fs)
str1.append(str(count1))

print("".join(str1))
#A5B5C3D1


# unique Chars
def uniqueChars(strA):
    li = []
    n = len(strA)
    for i in range(0, n):
        if strA[i].upper() in li:
             return "False"
        else:
            li.append(strA[i].upper())
    return True
    
stra = "facetious"  #facetious
print(uniqueChars(stra))
#True


#Revers chars without impacting spec chars
def reverseString(StrA):
    lo = 0
    hi = len(StrA)-1
    li = list(StrA)
    while lo < hi:
        if str(li[lo]).isalpha() == True and str(li[hi]).isalpha() == True:
            li[lo], li[hi] = li[hi], li[lo]
            lo+=1
            hi-=1
    
        if str(li[lo]).isalpha() == True and str(li[hi]).isalpha() == False:
            hi-=1
        
        if str(li[lo]).isalpha() == False and str(li[hi]).isalpha() == True:
            lo+=1
    
    print("".join(li))
A = "WaterBottle!"
reverseString(A)
#elttoBretaW!


#Swap value and keys
def group_by_owners(files):
    adict = {}
    for key, value in files.items():
        adict.setdefault(value, []).append(key)
    return adict       
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))
#{'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}


#Travel itinerary
def TravelItinerary(travelDict):
    
    #traverse the dict 
    #and reverse
    reversetravel={}
    for k, v in travelDict.items():
        reversetravel[v] = k

    #if k not in reverse, k = start
    for k, v in travelDict.items():
        if k not in reversetravel:
            start = k
            break
        
    if start is None:
        print("Invalid input")
        return
    
    to = travelDict.get(start)
    while to is not None:
        print(start + "->" + to + " ")
        start = to
        to = travelDict.get(to)
            
    
travelDict = {"Chennai":"Bangalore", "Bombay":"Delhi", "Goa":"Chennai", "Delhi":"Goa"}
TravelItinerary(travelDict)
#Bombay->Delhi 
#Delhi->Goa 
#Goa->Chennai 
#Chennai->Bangalore 


#Number to string
def print_3_digit(number):
    
    basic_lookup = ['', 'One', 'Two', 'Three', 'Four', 'Five', 
                    'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
                    'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
                    'Seventeen', 'Eighteen', 'Nineteen'
                    ]
    
    tens_lookup = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
                   'Seventy', 'Eighty',  'Ninety']
    
    hundred_digit = number // 100
    if hundred_digit > 0 :
            print(basic_lookup[hundred_digit] + ' Hundred ', end=' ')
        
    remainder = number % 100
    if remainder > 0:
        if remainder <= 19:
            print(basic_lookup[remainder] + ' ', end='')
        else:
            
            tens_digit = remainder // 10
            unit_digit = remainder % 10
            print(tens_lookup[tens_digit] + ' ', end='')
            print(basic_lookup[unit_digit] + ' ', end='')
    
def print_num_in_words(number):
    
    if number == 0:
        print("Zero")
        return
    
    millions = number // 1000000
    remainder = number - (millions * 1000000)
    
    thousands = remainder // 1000
    remainder = remainder - (thousands * 1000)
    
    if millions > 0:
        print_3_digit(millions)
        print('Million', end='')
        
    if thousands > 0:
        print_3_digit(thousands)
        print('Thousand ', end='')
        
    if remainder > 0:
        print_3_digit(remainder)
        
    print('')
    
print_num_in_words(999)
#Nine Hundred  Ninety Nine 

print_num_in_words(842453)
#Eight Hundred  Forty Two Thousand Four Hundred  Fifty Three


    