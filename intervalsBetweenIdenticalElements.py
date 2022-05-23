#intervalsBetweenIdenticalElements
#You are given a 0-indexed array of n integers arr.
#
#The interval between two elements in arr is defined as the absolute difference between their indices. More formally, the interval between arr[i] and arr[j] is |i - j|.
#
#Return an array intervals of length n where intervals[i] is the sum of intervals between arr[i] and each element in arr with the same value as arr[i].
#
#Note: |x| is the absolute value of x.
#
#Example 1:
#
#Input: arr = [2,1,3,1,2,3,3]
#Output: [4,2,7,2,4,4,5]
#Explanation:
#- Index 0: Another 2 is found at index 4. |0 - 4| = 4
#- Index 1: Another 1 is found at index 3. |1 - 3| = 2
#- Index 2: Two more 3s are found at indices 5 and 6. |2 - 5| + |2 - 6| = 7
#- Index 3: Another 1 is found at index 1. |3 - 1| = 2
#- Index 4: Another 2 is found at index 0. |4 - 0| = 4
#- Index 5: Two more 3s are found at indices 2 and 6. |5 - 2| + |5 - 6| = 4
#- Index 6: Two more 3s are found at indices 2 and 5. |6 - 2| + |6 - 5| = 5
#Example 2:
#
#Input: arr = [10,5,10,10]
#Output: [5,0,3,4]
#Explanation:
#- Index 0: Two more 10s are found at indices 2 and 3. |0 - 2| + |0 - 3| = 5
#- Index 1: There is only one 5 in the array, so its sum of intervals to identical elements is 0.
#- Index 2: Two more 10s are found at indices 0 and 3. |2 - 0| + |2 - 3| = 3
#- Index 3: Two more 10s are found at indices 0 and 2. |3 - 0| + |3 - 2| = 4
#
#Constraints:
#
#n == arr.length
#1 <= n <= 105
#1 <= arr[i] <= 105

class Solution:
    def getDistances(self, arr):
        h,n={},len(arr)
        result=[0]*n
        for i in range(n):
            if arr[i] in h:
                h[arr[i]].append(i)
            else:
                h[arr[i]]=[i]
        #this is slow
        #for i in range(n):
        #    for j in h[arr[i]]:
        #        result[i]+=abs(i-j)
        print(h)
        for j,v in enumerate(h):
            print(j,v,h[v])
            l = h[v]
            pre = [0] * (len(l) + 1)
            for i in range(len(l)):
                pre[i + 1] = pre[i] + l[i]
            print("Pre:",pre)
        return result
        
    def getDistancesFaster(self, arr):
        m, res = {}, [0] * len(arr)
        for i, v in enumerate(arr):
            if v not in m: m[v] = list()
            m[v].append(i)
        
        for x in m:
            l = m[x]
            pre = [0] * (len(l) + 1)
            for i in range(len(l)):
                pre[i + 1] = pre[i] + l[i]
            for i, v in enumerate(l):
                res[v] = (v * (i + 1) - pre[i + 1]) + ((pre[len(l)] - pre[i]) - v * (len(l) - (i)))
        return res
        
s=Solution()        
arr = [2,1,3,1,2,3,3]
print(arr,s.getDistances(arr))