#nonOverlappingIntervals
#Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
#
#Example 1:
#
#Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
#Output: 1
#Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
#Example 2:
#
#Input: intervals = [[1,2],[1,2],[1,2]]
#Output: 2
#Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
#Example 3:
#
#Input: intervals = [[1,2],[2,3]]
#Output: 0
#Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
# 
#Constraints:
#
#1 <= intervals.length <= 105
#intervals[i].length == 2
#-5 * 104 <= starti < endi <= 5 * 104

class Solution:
    def eraseOverlapIntervals(self, intervals):
        if intervals is None:
            return None
        print(intervals)
        intervals.sort(key=lambda a:a[0])
        left,right,count=0,1,0
        n=len(intervals)
        result=[]
        while right<n:
            if intervals[left][1]<=intervals[right][0]:
                left=right
                right+=1
            elif intervals[left][1]<=intervals[right][1]:
                count+=1
                right+=1
            elif intervals[left][1]>intervals[right][1]:
                count+=1
                left=right
                right+=1
        return count

s=Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
print("RESULT for ",intervals," : ",s.eraseOverlapIntervals(intervals))
intervals = [[1,2],[1,2],[1,2]]
print("RESULT for ",intervals," : ",s.eraseOverlapIntervals(intervals))
intervals = [[1,3],[2,6],[1,4],[2,10],[1,10],[15,18]]
print("RESULT for ",intervals," : ",s.eraseOverlapIntervals(intervals))