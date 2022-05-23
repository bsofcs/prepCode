#KdiffPairsInAnArray
#Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
#
#A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
#
#0 <= i < j < nums.length
#|nums[i] - nums[j]| == k
#Notice that |val| denotes the absolute value of val.
#
#Example 1:
#
#Input: nums = [3,1,4,1,5], k = 2
#Output: 2
#Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
#Although we have two 1s in the input, we should only return the number of unique pairs.
#Example 2:
#
#Input: nums = [1,2,3,4,5], k = 1
#Output: 4
#Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
#Example 3:
#
#Input: nums = [1,3,1,5,4], k = 0
#Output: 1
#Explanation: There is one 0-diff pair in the array, (1, 1).
from collections import Counter
class Solution:
    def mergeSort(self,nums):
        if None in (nums):
            return None
        n=len(nums)
        if n==1:
            return nums
        mid=n//2
        left=self.mergeSort(nums[:mid])
        right=self.mergeSort(nums[mid:])
        result=[]
        i,j,nleft,nright=0,0,len(left),len(right)
        while i<nleft and j<nright:
            if left[i]<right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        while i<nleft:
            result.append(left[i])
            i+=1
        while j<nright:
            result.append(right[j])
            j+=1
        return result
    def binarySearch(self,nums,low,high,k):
        if low<=high:
            mid=(low+high)//2
            print("search",nums,low,high,(low+high)//2,k)
            if nums[mid]==k:
                return True
            elif nums[mid]>k:
                return self.binarySearch(nums,low,mid-1,k)
            else:
                return self.binarySearch(nums,mid+1,high,k)
        return False
        
    def findPairs(self, nums, k):
        if None in (nums,k):
            return None
        nums=self.mergeSort(nums)
        n=len(nums)
        i,j,result=0,0,0
        while i<n-1:
            tmp=k+nums[i]
            
            j=i+1
            print(nums[i],nums[j],tmp,result)
            result+=1 if self.binarySearch(nums,j,n-1,tmp) else 0
            j=i
            while nums[j]==nums[i] and i<n-1:
                i+=1
        return result
        

class Solution1:
    def findPairs(self, nums, k):
        if None in (nums,k):
            return None
        i,j,n=0,0,len(nums)
        s=set([(nums[i],nums[j]) for i in range(n) for j in range(n) if i!=j and nums[i]>=nums[j]])
        c=Counter([si[0]-si[1] for si in s])
        return c[k]

class Solution2:
    def findPairs(self, nums, k):
        res = 0
        c = Counter(nums)
        print(c)
        for i in c:
            if (k > 0 and i + k in c) or (k == 0 and c[i] > 1):
                res += 1
        return res
       
s=Solution2()
nums = [3,1,4,1,5]
k = 2
print("Result",nums,k,s.findPairs(nums,k))
nums = [1,2,3,4,5]
k = 1
print("Result",nums,k,s.findPairs(nums,k))
nums = [1,1,1,1,1]
k = 0
print("Result",nums,k,s.findPairs(nums,k))
