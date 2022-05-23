#longestSubArrayWithEqual01
#Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
#
#Example 1:
#
#Input: nums = [0,1]
#Output: 2
#Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
#Example 2:
#
#Input: nums = [0,1,0]
#Output: 2
#Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# 
#Constraints:
#
#1 <= nums.length <= 105
#nums[i] is either 0 or 1.

class Solution:
    def findMaxLength(self, nums):
        if nums is None:
            return None
        n=len(nums)
        d={}
        d[0]=[-1]
        tmp=[]
        sumSoFar=0
        for i in range(n):
            sumSoFar+=1 if nums[i]==1 else -1
            tmp.append(sumSoFar)
            if sumSoFar in d:
                d[sumSoFar].append(i)
            else:
                d[sumSoFar]=[i]
        #print(d,tmp)
        for i in d:
            if len(d[i])==1:
                d[i]=0
            else:
                d[i]=d[i][-1]-d[i][0]
        return max(d.values())


class Solution1:
    def findMaxLength(self, nums):
        if nums is None:
            return None
        n=len(nums)
        d={}
        sumSoFar=0
        maxLength=float("-inf")
        for i in range(n):
            sumSoFar+=1 if nums[i]==1 else -1
            if sumSoFar==0:
                maxLength=max(maxLength,i+1)
            elif sumSoFar in d:
                maxLength=max(maxLength,i-d[sumSoFar])
            else:
                d[sumSoFar]=i
        return maxLength
        
s=Solution()
p=Solution1()
nums = [0,1]
print(nums,s.findMaxLength(nums),p.findMaxLength(nums))
nums = [0,1,0]
print(nums,s.findMaxLength(nums),p.findMaxLength(nums))
nums = [1,1,0,0,1,1,0,1,0]
print(nums,s.findMaxLength(nums),p.findMaxLength(nums))
nums = [1,1,0,0,1,1,0,1,0,0]
print(nums,s.findMaxLength(nums),p.findMaxLength(nums))
nums = [1,1,0,0,1,1,0,1,0,1,1]
print(nums,s.findMaxLength(nums),p.findMaxLength(nums))