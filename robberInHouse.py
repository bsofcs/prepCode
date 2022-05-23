#robberInHouse
class Solution:
    def rob(self, nums):
        if nums is None:
            return None
        n=len(nums)
        dp=[0 for _ in range(n)]
        for i in range(n-1,-1,-1):
            if i>n-3:
                dp[i]=nums[i]
            else:
                dp[i]=nums[i]+max(dp[i+2:])
        print(dp,max(dp))
        
class Solution1:
    def rob(self,nums):
        
        
        
s=Solution()
nums=[1,2,3,4,5]
print(nums)
s.rob(nums)
nums=[4,2,3,5]
print(nums)
s.rob(nums)
nums=[4]
print(nums)
s.rob(nums)
nums=[4,4,4,4,4]
print(nums)
s.rob(nums)
nums=[4,1,2,7,5,3,1]
print(nums)
s.rob(nums)