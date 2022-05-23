#multiplyAllExceptSelf
class Solution:
    def productExceptSelf(self, nums):
        output = [1] * len(nums)
        L = len(output)
        for i in range(1,L):
            output[i] = output[i-1] * nums[i-1]
            print(output)
        r = 1
        for i in reversed(range(L)):
            print(output)
            output[i] = output[i] * r
            r = r * nums[i]
        return output
    
    def productExceptSelfSimple(self, nums: List[int]) -> List[int]:
        if nums is None:
            return
        def multiplyAll(arr):
            t=1
            for i in arr:
                t*=i
            return t
        total=multiplyAll(nums)
        n=len(nums)
        ans=[]
        for i in range(n):
            if nums[i]==0:
                t=nums[:i]
                t.extend(nums[i+1:])
                ans.append(multiplyAll(t))
            else:
                ans.append(int(total/nums[i]))
        return ans

arr=[1,2,3,4]
s=Solution()
print(s.productExceptSelf(arr))