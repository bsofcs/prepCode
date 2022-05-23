#summaryRanges
#You are given a sorted unique integer array nums.
#
#Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
#
#Each range [a,b] in the list should be output as:
#
#"a->b" if a != b
#"a" if a == b
# 
#
#Example 1:
#
#Input: nums = [0,1,2,4,5,7]
#Output: ["0->2","4->5","7"]
#Explanation: The ranges are:
#[0,2] --> "0->2"
#[4,5] --> "4->5"
#[7,7] --> "7"
#Example 2:
#
#Input: nums = [0,2,3,4,6,8,9]
#Output: ["0","2->4","6","8->9"]
#Explanation: The ranges are:
#[0,0] --> "0"
#[2,4] --> "2->4"
#[6,6] --> "6"
#[8,9] --> "8->9"
# 
#
#Constraints:
#
#0 <= nums.length <= 20
#-231 <= nums[i] <= 231 - 1
#All the values of nums are unique.
#nums is sorted in ascending order.

class Solution:
    def summaryRanges(self, nums):
        if nums is None:
            return None
        n=len(nums)
        result={}
        for i in range(n):
            if nums[i]-i not in result:
                result[nums[i]-i]=[i]
            else:
                result[nums[i]-i].append(i)
        otput=[]
        tmp=""
        for i in sorted(result.keys()):
            if result[i][0]==result[i][-1]:
                tmp=str(nums[result[i][0]])
            else:
                tmp=str(nums[result[i][0]])+"->"+str(nums[result[i][-1]])
            otput.append(tmp)
        return(otput)
        
    def summaryRanges1(self, nums):
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        print(ranges,ranges[-1][1:])
        return ['->'.join(map(str, r)) for r in ranges]

s=Solution()
nums = [0,1,2,4,5,7]
print(nums,s.summaryRanges1(nums))