"""
jobSchedulingWth2StationAllowed
We are given N jobs, and their starting and ending times. We can do two jobs simultaneously at a particular moment. If one job ends at the same moment some other show starts then we cant do them. We need to check if all jobs are possible to be done or not.
"""

def jobSchedulingWth2StationAllowed(start,end):
	if None in (start,end) or len(start)!=len(end):
		return
	n=len(start)
	arr=[[start[i],end[i]] for i in range(n)]
	arr=sorted(arr,key=lambda x:x[1])
	j1=arr[0][1]
	j2=arr[1][1]
	for i in range(2,n):
		if j1>arr[i][0] and j2>arr[i][0]:
			return False
		elif j1<arr[i][0]:
			j1=arr[i][1]
		elif j2<arr[i][0]:
			j2=arr[i][1]	
	return True

start=[2, 4, 1]
end=[3, 5, 2]
print(jobSchedulingWth2StationAllowed(start,end))
start=[1,2,2,1]
end=[5,4,6,7]
print(jobSchedulingWth2StationAllowed(start,end))