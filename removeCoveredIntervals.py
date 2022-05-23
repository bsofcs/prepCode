#removeCoveredIntervals
#Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.
#
#The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.
#
#Return the number of remaining intervals.
#
#Example 1:
#
#Input: intervals = [[1,4],[3,6],[2,8]]
#Output: 2
#Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
#Example 2:
#
#Input: intervals = [[1,4],[2,3]]
#Output: 1
# 
#Constraints:
#
#1 <= intervals.length <= 1000
#intervals[i].length == 2
#0 <= li <= ri <= 105
#All the given intervals are unique.

class Solution1:         
    def removeCoveredIntervals(self, intervals):
        if intervals is None:
            return None
        intervals.sort(key=lambda a:(a[0]))
        left=right=-1
        count=0
        for i in intervals:
            if i[0]>left and i[1]>right:
                count+=1
                left=i[0]
            right=max(i[1],right)
        return count

class Solution:
    def removeCoveredIntervals(self, A):
        res = right = 0
        #print("BEFORE:",A)
        A.sort(key=lambda a: (a[0], -a[1]))
        #print(A)
        for i, j in A:
            #print(i,j,res,res,j>right)
            res += j > right
            right = max(right, j)
        return res
        
s=Solution()
s1=Solution1()
intervals=[[1,4],[3,6],[2,8]]
print(intervals,s.removeCoveredIntervals(intervals),s1.removeCoveredIntervals(intervals))
intervals = [[1,4],[2,3]]
print(intervals,s.removeCoveredIntervals(intervals),s1.removeCoveredIntervals(intervals))
intervals = [[1,4],[2,10],[3,4],[6,7],[1,3]]
print(intervals,s.removeCoveredIntervals(intervals),s1.removeCoveredIntervals(intervals))
intervals = [[3,10],[4,10],[5,11]]
print(intervals,s.removeCoveredIntervals(intervals),s1.removeCoveredIntervals(intervals))
intervals=[[34335,39239],[15875,91969],[29673,66453],[53548,69161],[40618,93111]]
print(intervals,s.removeCoveredIntervals(intervals),s1.removeCoveredIntervals(intervals))