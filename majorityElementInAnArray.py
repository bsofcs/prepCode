#majorityElementInAnArray
#Given an array nums of size n, return the majority element.
#
#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
#
#Example 1:
#
#Input: nums = [3,2,3]
#Output: 3
#Example 2:
#
#Input: nums = [2,2,1,1,1,2,2]
#Output: 2
# 
#Constraints:
#
#n == nums.length
#1 <= n <= 5 * 104
#-231 <= nums[i] <= 231 - 1

class Solution:
    def majorityElement(self, nums):
        if nums is None:
            return None
        n=len(nums)
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        val=max(d.values())
        for i in d:
            if d[i]==val:
                return i
                
    def majorityElement1(self, nums):
        nums.sort()
        return nums[len(nums)//2]
        
    def majorityElement2(self, nums):
        candidate, count = nums[0], 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate, count = num, 1
            else:
                count -= 1
        return candidate

s=Solution()
nums = [3,2,3]
print(nums,s.majorityElement(nums))
nums = [2,2,1,1,1,2,2]
print(nums,s.majorityElement(nums))