#mergeIntervals
#Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
#Example 1:
#
#Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#Example 2:
#
#Input: intervals = [[1,4],[4,5]]
#Output: [[1,5]]
#Explanation: Intervals [1,4] and [4,5] are considered overlapping. 
#
#Constraints:
#
#1 <= intervals.length <= 104
#intervals[i].length == 2
#0 <= starti <= endi <= 104

class Solution:
    def merge(self, intervals):
        if intervals is None:
            return None
        #print(intervals)
        intervals.sort(key=lambda a:(a[0],a[1]))
        left=right=-1
        result=[]
        for i in intervals:
            #print(i,end=" ")
            if i[0]>right:
                #print("Hi")
                left=i[0]
                right=i[1]
                result.append(i)
            elif i[0]>=left and i[1]>=right:
                #print("Hello")
                result.pop(-1)
                left=min(left,i[0])
                right=max(right,i[1])
                result.append([left,right])
            #print(result)
        return result
    
    def merge1(self, intervals):
        out = []
        for i in sorted(intervals, key=lambda i: i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += i,
        return out

s=Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print("RESULT for \n",intervals,":\n",s.merge(intervals))
intervals = [[1,4],[4,5]]
print("RESULT for \n",intervals,":\n",s.merge(intervals))
intervals = [[1,3],[2,6],[1,4],[2,10],[1,10],[15,18]]
print("RESULT for \n",intervals,":\n",s.merge(intervals))
intervals=[[1,2],[3,4],[5,6]]
print("RESULT for \n",intervals,":\n",s.merge(intervals))