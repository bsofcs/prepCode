#subarraySumsEqualK
#Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
#
#Example 1:
#
#Input: nums = [1,1,1], k = 2
#Output: 2
#Example 2:
#
#Input: nums = [1,2,3], k = 3
#Output: 2
#
#Constraints:
#
#1 <= nums.length <= 2 * 104
#-1000 <= nums[i] <= 1000
#-107 <= k <= 107

class Solution:
    def subarraySum(self, nums, k):
        if None in (nums,k):
            return None
        n=len(nums)
        result=0
        preSum=0
        d={}
        d[0]=1
        for i in nums:
            preSum+=i
            if preSum-k in d:
                result+=d[preSum-k]
            d[preSum]=d.get(preSum,0)+1
        return result
        
s=Solution()
nums = [1,1,1]
k = 2
print(nums,k,s.subarraySum(nums,k))
nums = [1,2,3]
k = 3
print(nums,k,s.subarraySum(nums,k))