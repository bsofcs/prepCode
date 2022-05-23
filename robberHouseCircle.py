#robberHouseCircle
class Solution:
    def rob(self,nums):
        if nums is None:
            return None
        print("Input:",nums)
        n=len(nums)
        if n<=3:
            return max(nums)
        dp=[0]*n
        for i in range(n):
            tmp=[nums[x] for x in range(n) if x not in [(i-1)%n,i,(i+1)%n]]
            mx=self.robLinear(tmp)
            dp[i]=nums[i]+mx
            print(i,tmp,mx,dp)
        return max(dp)
        
    def robLinear(self,nums):
        if nums is None:
            return 0
        n=len(nums)
        if n<3:
            return max(nums)
        dp=[0]*n
        for i in range(n-1,-1,-1):
            if i>n-3:
                dp[i]=nums[i]
            else:
                dp[i]=nums[i]+max(dp[i+2:])
        return max(dp)
        

class Solution1:
    def rob(self, nums):
        if len(nums) == 0 or nums is None:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))

    def rob_simple(self, nums):
        t1 = 0
        t2 = 0
        for current in nums:
            temp = t1
            t1 = max(current + t2, t1)
            t2 = temp

        return t1

s=Solution()
y=Solution1()
nums=[1,2,3]
print(nums," : ",s.rob(nums),y.rob(nums),"done")
nums=[1,2,3,1]
print(nums," : ",s.rob(nums),y.rob(nums),"done")
nums=[2,1,1,2]
print(nums," : ",s.rob(nums),y.rob(nums),"done")
nums=[200,3,140,20,10]
print(nums," : ",s.rob(nums),y.rob(nums),"done")
nums=[1,7,9,2]
print(nums," : ",s.rob(nums),y.rob(nums),"done")
nums=[2,4,8,9,9,3]
print(nums," : ",s.rob(nums),y.rob(nums),"done")
nums=[6,3,10,8,2,10,3,5,10,5,3]
print(nums," : ",s.rob(nums),y.rob(nums),"done")