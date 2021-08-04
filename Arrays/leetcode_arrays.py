# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 10:42:05 2021

@author: ketnpt
"""

# Leetcode 1 
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        adict = {}
        list1 = []


        sum1 = 0 
        n = len(nums)
        for i in range(0,n):

            sum1 = target - nums[i]        
                        
            if sum1 in adict:
                list1.append(adict.get(sum1))
                list1.append(i)
            else:
                adict[nums[i]] = i                            
                
        return list1
        
            
nums = [3,2,4]
target = 6
s1 = Solution() 
print(s1.twoSum(nums, target))


# Leetcode 15
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n  = len(nums)
        
        res = []
        sum1 = float("-inf")
        for i in range(n):
            
            if nums[i] > 0:
                break
            
            if i == 0 or nums[i-1] != nums[i]:
                
                lo = i+1
                hi = n-1    
                while lo < hi:
                    sum1 = nums[i] + nums[lo] + nums[hi]
                    
                    if sum1 > 0:
                        hi-= 1 
                    elif sum1 < 0:
                        lo+=1
                    else:
                        res.append([nums[i], nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1
                        while lo < hi and nums[lo] == nums[lo-1]:
                            lo += 1
            
        return res
                    
            
        
nums = [-1,0,1,2,-1,-4]
s1 = Solution() 
print(s1.threeSum(nums))


#FourSum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        sum1 = float("-inf")
        res = []
        for i in range(n):
            for j in range(i+1, n-1):
                
                lo = j+1
                hi = n-2
                    
                while lo < hi:
                    
                    sum1  = nums[lo] + nums[hi] + nums[j] + nums[i]
                    
                    if sum1 > target:
                        hi -=1 
                    elif sum1 < target:
                        lo +=1
                    else:
                        res.append([nums[i], nums[j], nums[lo], nums[hi]])
                        hi -=1 
                        lo +=1
                        
                sum1 = float("-inf")
                    
        return res
        
nums = [1,0,-1,0,-2,2]
target = 0
s1 = Solution() 
print(s1.fourSum(nums, target))


# Leetcode 56
def merge(intervals: List[List[int]]) -> List[List[int]]:
    
    # sort the array
    intervals.sort(key = lambda i: i[0])
    
    # start at the 1st 
    res = [intervals[0]]
    print(res)
    # check others
    for start, end in intervals[1:]:
        # if overlap, expand 
        if start <= res[-1][1]:
            res[-1][1] = max(end, res[-1][1])
            
        # if not overlap, append
        else:
            res.append([start, end])
    
    # return 
    print(res)
    return res

merge([[1,3], [2,6], [8,10], [11,15]])


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]       
    
nums = [3,2,3,1,2,4,5,5,6]
k = 4
s1 = Solution() 
print(s1.findKthLargest(nums, k))

# Leetcode 238
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = nums[0]
        n = len(nums)
        res = [1]
        for i in range(1, n):
            res.append(prod)
            prod = prod * nums[i] 
        
        print(res)
        prod = 1
        for i in range(n-1,-1,-1):
            res[i] = res[i] * prod  
            prod = nums[i] *  prod   
            
        return res
        
        
nums = [1,2,3,4]
s1 = Solution() 
print(s1.productExceptSelf(nums))


#Given an integer array nums and an integer k, return true if 
#nums has a continuous subarray of size at least two whose elements 
#sum up to a multiple of k, or false otherwise.
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        adict = {0:-1}
        prefix = [0]
        n = len(nums)
        for i in range(0, n):               
            v = (nums[i] + prefix[-1]) % k

            prefix.append(v)
            if v in adict:
                if i - adict[v] >=2:
                    return True
            
            else:
                adict[v] = i
        return False

        
nums = [23,2,4,6,7]
k = 6
s1 = Solution() 
print(s1.checkSubarraySum(nums, k))


#Leetcode 560
#Given an array of integers nums and an integer k, 
#return the total number of continuous subarrays whose sum equals to k.
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=cumSum=0
        maps={0:1}
        for ele in nums:
            cumSum += ele
            print(cumSum)
            count += maps.get(cumSum-k,0)

            maps[cumSum] = maps.get(cumSum,0)+1
            print(maps)
        return count
        
nums = [1,1,1]
k = 2
s1 = Solution() 
print(s1.subarraySum(nums, k))

#Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count=0
        i=1
        while True:
            if i not in arr:
                count+=1
            if count==k:
                break
            i=i+1
        return i
    

arr = [1,2,3,4]
k = 2
s1 = Solution() 
print(s1.findKthPositive(arr, k))

# Leetcode 986
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1 = 0
        p2 = 0
        res = []
        while p1 < len(firstList) and p2 < len(secondList):
            first = max(firstList[p1][0], secondList[p2][0])
            second = min(firstList[p1][1], secondList[p2][1])
            if first <= second:
                res.append([first,second])
            
            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return res
    
firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
s1 = Solution() 
print(s1.intervalIntersection(firstList, secondList))


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0 
        j = 1
        n = len(nums)
        
        if n == 1 or n == 0:
            return n
        
        while j < n:
            if nums[i] != nums[j]:
                i+=1
                nums[i] = nums[j]
            j+=1
        
        print(nums)
        return i+1
            
nums = [1,1,2]
s1 = Solution() 
print(s1.removeDuplicates(nums))

#Leercode 349
# Given two integer arrays nums1 and nums2, 
# return an array of their intersection. 
# Each element in the result must be unique and you may return the result in any order.
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        Alo, Ahi = 0, len(nums1)
        Blo, Bhi = 0, len(nums2)
        res1=[]
        nums1.sort()
        nums2.sort()
        while Alo < Ahi and Blo < Bhi:
            if nums1[Alo] == nums2[Blo]:
                if nums1[Alo] not in res1:
                    res1.append(nums1[Alo])
                Alo += 1 
                Blo += 1
            elif nums1[Alo] < nums2[Blo]:
                Alo+=1
            else:
                Blo+=1
                
        return res1
                            
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
s1 = Solution() 
print(s1.intersection(nums1, nums2))


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
          
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
            


nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [1,2,2]
n = 3
s1 = Solution() 
print(s1.merge(nums1, m, nums2, n))


# LC: 905
print("parity")
# Given an integer array nums, move all the even integers at the 
# beginning of the array followed by all the odd integers.
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        even = []
        odd = []
        for i in nums:
            print(i)
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)        

        res = even + odd
        return res
        
nums = [3,1,2,4]        
s1 = Solution() 
print(s1.sortArrayByParity(nums))
        

# LC 27:  Remove Element
print("Remove element")
#Given an integer array nums and an integer val, remove all occurrences 
#of val in nums in-place. The relative order of the elements may be changed.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        lo  = 0
        n  = len(nums)
        indx = 0
        while lo < n:
            if nums[lo] == val:
                lo += 1
            else:
                nums[indx] = nums[lo]
                indx  += 1
                lo += 1
    
        return indx
        
        
nums=[0,1,2,2,3,0,4,2]
val=2
s1 = Solution() 
print(s1.removeElement(nums, val))
        

# LC 1929
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        res = []
        n = len(nums)
        for i in range(0, n):
            res.append(nums[i])
        
        for i in range(0, n):
            res.append(nums[i])
            
        return res

nums = [1,2,1]
s1 = Solution() 
print(s1.getConcatenation(nums))



# LC 34. Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        lo = 0
        hi = len(nums)-1
        op_list = [-1,-1]
        res = -1
        while lo <= hi:
            mid = (lo + hi) // 2 
            if nums[mid] == target:
                res = mid
                hi = mid - 1
            elif target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid+1
        

        op_list[0] = res
            
        lo = 0
        hi = len(nums)-1
        res= -1
        while lo <= hi:
            mid = (lo + hi) // 2 
            if nums[mid] == target:
                res = mid
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid-1
            else:
                lo = mid+1
                
        op_list[1] = res
        
        return op_list
        
nums= []
target = 8
s1 = Solution() 
print(s1.searchRange(nums, target))


#33. Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1
    
        while lo <= hi:
            mid = lo + (hi-lo)//2
        
            if nums[mid] == target:
                return mid
        
            if nums[lo] <= nums[mid]:
                if target < nums[mid] and target >= nums[lo]:
                    hi = mid - 1
                else:
                    lo = mid + 1
                
            if nums[mid] <= nums[hi]:
                if target > nums[mid] and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = hi - 1
                
        return -1 
        
nums = [4,5,6,7,0,1,2]
target = 0
s1 = Solution() 
print(s1.search(nums, target))


# 35. Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mid = (lo + hi) // 2 
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid+1
        
        if nums[lo] < target:
            return lo + 1
        else:
            return lo
        
        

nums=[1,3,5,6]
target = 2

s1 = Solution() 
print(s1.searchInsert(nums, target))

# 1389. Create Target Array in the Given Order
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:

        res = []
        for i in range(len(nums)):
            res.insert(index[i],nums[i])
        
        return res

nums = [0,1,2,3,4]
index = [0,1,2,2,1]
s1 = Solution() 
print(s1.createTargetArray(nums, index))
#output [0, 4, 1, 3, 2]


#448. Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        m=set(nums)

        res=[]
        for i in range(1,len(nums)+1):
            if i not in m:
                res.append(i)
        return res
        
nums = [4,3,2,7,8,2,3,1]
#nums = [1,1]
s1 = Solution() 
print(s1.findDisappearedNumbers(nums))
        

#169. Majority Element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]

nums = [2,2,1,1,1,2,2]
s1 = Solution() 
print(s1.majorityElement(nums))
        
import math
#204. Count Primes
class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n <= 2: return 0
        
        # boolean array to keep track of primes
        isPrime = [True] * n
        # Since 0 and 1 are not primes
        isPrime[0] = isPrime[1] = False
        
        # Why we loop only till int(sqrt(n)) + 1 is since in the inner loop we are
        # checking all multiples starting from square of that num, numbers which are
        # not prime from int(sqrt(n)) + 1 will already be covered and only primes are
        # remained from int(sqrt(n)) + 1 to n
        for i in range(2, int(math.sqrt(n)) + 1):
            if isPrime[i]:
                # Why we start at i * i, but not i * 2 is, at every index i, multiples
                # of i - 1, i - 2 and so on already noted (i - 1) * i, (i - 2) * i 
                # and so on. So they are already visited and therefore no need to again
                # loop through them. So we start at i * i
                for j in range(i * i, n, i):
                    isPrime[j] = False
        
        return sum(isPrime)
            
        
        
n = 10
s1 = Solution() 
print(s1.countPrimes(n))



#217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       
        return len(set(nums)) != len(nums)

        
nums = [1,2,3,1] 
s1 = Solution() 
print(s1.containsDuplicate(nums))
 
# 219. Contains Duplicate II

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        adict = {}
        for i, v in enumerate(nums):
            if v not in adict:
                adict[v] = i
            elif abs(adict[v] - i) <= k:
                return True
            else:
                adict[v] = i
        return False

nums =  [1,0,1,1]
k = 1
s1 = Solution() 
print(s1.containsNearbyDuplicate(nums,k))


# 152. Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums) 
        currMin, currMax = 1,1
        for n in nums:
            if n==0:
                currMin, currMax = 1,1
            else:
                tmp = currMax * n
                currMax = max(n*currMin,n*currMax,n)
                currMin = min(n*currMin,tmp,n)
                res = max(res,currMax)
        return res



nums = [2,3,-2,4]
s1 = Solution() 
print(s1.maxProduct(nums))

# 287. Find the Duplicate Number
# only 1 dup #. 
#You must solve the problem without modifying the array nums and uses only constant extra space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        fast = slow = nums[0]
        while fast < len(nums): 
            fast = nums[nums[fast]]
            print(fast)
            slow = nums[slow]
            if slow == fast:
                break    #means there is a cycle in the array or a duplicate element
                        # Here, the while loop above can break in two cases, 
                       #(i) if there are no duplicates in the array, (ii) if slow == fast
        if slow == fast: #we are checking the case where cycle is detected
            slow = nums[0]
            while fast != slow:
                slow = nums[slow]
                fast = nums[fast]
            return slow
        else: # case of no duplicates in the array
            return
    
nums =  [1,3,4,2,2]
s1 = Solution() 
print(s1.findDuplicate(nums))


# 373. Find K Pairs with Smallest Sums

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                res.append((nums1[i]+nums2[j],nums1[i],nums2[j]))
        ans = sorted(res)

        final_ans = []
        for second in ans:
            final_ans.append(second[1:])
        return final_ans[:k]

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
s1 = Solution() 
print(s1.kSmallestPairs(nums1, nums2, k))
#Return first [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

