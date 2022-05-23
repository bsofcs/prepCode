#burstballon
#You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.
#
#If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
#
#Return the maximum coins you can collect by bursting the balloons wisely.
#
# 
#
#Example 1:
#
#Input: nums = [3,1,5,8]
#Output: 167
#Explanation:
#nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
#coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
#Example 2:
#
#Input: nums = [1,5]
#Output: 10

class Solution:
    def maxCoinsBT(self, nums):
        if nums is None:
            return 0
        if len(nums)==1:
            return nums[0]
        return self.maxCoinsUtil(nums)
    
    def maxCoinsUtil(self, nums):
        if nums is None:
            return 0
        if len(nums)==1:
            return nums[0]
        n=len(nums)
        result=float("-INF")
        left=right=1
        for i in range(n):
            left=1 if i==0 else nums[i-1]
            right=1 if i==n-1 else nums[i+1]
            val=nums[i]
            nums.pop(i)
            result=max(result,left*val*right+self.maxCoinsUtil(nums))
            nums.insert(i,val)
        return result
        
    def maxCoins(self, nums):
        if nums is None:
            return 0
        n=len(nums)
        if n==1:
            return nums[0]
        tmp=[i for i in nums]
        tmp.insert(len(nums),1)
        tmp.insert(0,1)
        print(tmp)
        dp=[[0 for _ in tmp] for _ in tmp]
        for window in range(1,n+1):
            for left in range(1,n-window+2):
                right=left+window-1
                for i in range(left,right+1):
                    dp[left][right]=max(dp[left][right],(tmp[left-1]*tmp[i]*tmp[right+1])+dp[left][i-1]+dp[i+1][right])
                print(window,left,right,dp[left][right])
        for i in range(n+2):
            print(dp[i])
        return dp[1][n]
s=Solution()
nums = [3,1,5,8]
print(s.maxCoins(nums))
nums = [1,5]
print(s.maxCoins(nums))
#nums = [7,9,8,0,7,1,3,5,5,2,3]
#print(s.maxCoins(nums))