#minimizeDeviationInArray
#You are given an array nums of n positive integers.
#
#You can perform two types of operations on any element of the array any number of times:
#
#If the element is even, divide it by 2.
#For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
#If the element is odd, multiply it by 2.
#For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
#The deviation of the array is the maximum difference between any two elements in the array.
#
#Return the minimum deviation the array can have after performing some number of operations.
#
#Example 1:
#
#Input: nums = [1,2,3,4]
#Output: 1
#Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.
#Example 2:
#
#Input: nums = [4,1,5,20,3]
#Output: 3
#Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.
#Example 3:
#
#Input: nums = [2,10,8]
#Output: 3
#
#n == nums.length
#2 <= n <= 105
#1 <= nums[i] <= 10

from collections import Counter
import heapq

class Solution:
    def minimumDeviation(self, A):
        pq = []
        for a in A:
            heapq.heappush(pq, -a * 2 if a % 2 else -a)
        res = float('inf')
        mi = -max(pq)
        while len(pq) == len(A):
            a = -heapq.heappop(pq)
            res = min(res, a - mi)
            if a % 2 == 0:
                mi = min(mi, a / 2)     #this was important
                heapq.heappush(pq, -a / 2)
        print(a,pq)
        return int(res)
            

s=Solution()
nums=[1,2,3,4]
print("RESULT for ",nums,":",s.minimumDeviation(nums))
nums = [4,1,5,20,3]
print("RESULT for ",nums,":",s.minimumDeviation(nums))
nums = [2,10,8]
print("RESULT for ",nums,":",s.minimumDeviation(nums))
nums = [1,2]
print("RESULT for ",nums,":",s.minimumDeviation(nums))
nums = [i for i in range(1,105)]
print("RESULT for ",nums,":",s.minimumDeviation(nums))