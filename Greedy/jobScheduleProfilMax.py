"""
jobScheduleProfilMax
Given an array of jobs where every job has a deadline and associated profit if the job is finished before the deadline. It is also given that every job takes single unit of time, so the minimum possible deadline for any job is 1. How to maximize total profit if only one job can be scheduled at a time


Solution is as:
	1. we schedule the job in descending order of their profit
	2. from the sorted job we take each job and check if there is any slot available before the deadline of the job mention.
	3. place the job in the slot and ignore if there is no job
"""
def jobScheduleProfilMaxtry(arr):
	if arr is None:
		return None
	arr.sort(key=lambda x: x[2],reverse=True)
	n_max=max([i[1] for i in arr])
	print(n_max)
	n=len(arr)
	res=[]
	timer=1
	for i in range(n):
		if arr[i][1] in range(timer,n_max+1):
			res.append(arr[i][0])
			timer+=1
		if n_max==timer:
			break
	print(res)

def jobScheduleProfilMax(arr):
	n=len(arr)
	arr.sort(key=lambda x: x[2],reverse=True)
	result=[False]*n
	job=['-1']*n
	for i in range(n):
		for j in range(min(t-1,arr[i][1]-1),-1,-1):
			if result[j]==False:
				result[i]=True
				job[j]=arr[i][0]
				break
	print(job)

arr = [['a', 2, 100], # Job Array 
       ['b', 1, 19], 
       ['c', 2, 27], 
       ['d', 1, 25], 
       ['e', 3, 15]]
jobScheduleProfilMax(arr)