#medianOfTwoSortedArray
#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
#The overall run time complexity should be O(log (m+n)).
#
#Example 1:
#
#Input: nums1 = [1,3], nums2 = [2]
#Output: 2.00000
#Explanation: merged array = [1,2,3] and median is 2.
#Example 2:
#
#Input: nums1 = [1,2], nums2 = [3,4]
#Output: 2.50000
#Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if None in (nums1,nums2):
            return None
        arr=self.mergeArray(nums1,nums2)
        n=len(arr)
        print(arr,n)
        result=0
        if n%2==0:
            for i in range(n):
                if abs(i-(n-1-i))==1:
                    result+=arr[i]
        return result/2 if n%2==0 else arr[n//2]
    
    def mergeArray(self,nums1,nums2):
        if None in (nums1,nums2):
            return None
        n1,n2=len(nums1),len(nums2)
        i,j=0,0
        result=[]
        while i<n1 and j<n2:
            if nums1[i]<=nums2[j]:
                result.append(nums1[i])
                i+=1
            else:
                result.append(nums2[j])
                j+=1
        while i<n1:
            result.append(nums1[i])
            i+=1
        while j<n2:
            result.append(nums2[j])
            j+=1
        return result
        
class Solution1:
    def findMedianSortedArrays(self, nums1, nums2):
        if None in (nums1,nums2):
            return None
        n1,n2=len(nums1),len(nums2)
        if n1>n2:
            return self.findMedianSortedArrays(num2,num1)
        low,high=0,n1
        while low<=high:
            cut1=(low+high)//2
            cut2=(n1+n2+1)//2-cut1
            left1=float("-inf") if cut1==0 else nums1[cut1-1]
            right1=float("inf") if cut1==n1 else nums1[cut1]
            left2=float("-inf") if cut2==0 else nums2[cut2-1]
            right2=float("inf") if cut2==n2 else nums2[cut2]
            
            if left1<=right2 and left2<=right1:
                if (n1+n2)%2==0:
                    return (max(left1,left2)+min(right1,right2))/2
                else:
                    return max(left1,left2)
            elif left1>right2:
                high=cut1-1
            else:
                low=cut1+1
 
s= Solution1()
nums1 = [1,3]
nums2 = [2]
print(nums1, nums2, s.findMedianSortedArrays(nums1, nums2))
nums1 = [1,2]
nums2 = [3,4]
print(nums1, nums2, s.findMedianSortedArrays(nums1, nums2))
nums1 = [1]
nums2 = [2]
print(nums1, nums2, s.findMedianSortedArrays(nums1, nums2))
nums1 = [1,2,3]
nums2 = [2,4]
print(nums1, nums2, s.findMedianSortedArrays(nums1, nums2))