"""
policeAndThieves
Given an array of size n that has the following specifications:
1. Each element in the array contains either a policeman or a thief.
2. Each policeman can catch only one thief.
3. A policeman cannot catch a thief who is more than K units away from the policeman.
We need to find the maximum number of thieves that can be caught.
"""

def policeAndThieves(arr,K):
	if arr is None or K is None:
		return None
	count=0
	pol=[];thi=[]
	n=len(arr)
	for i in range(n):
		if arr[i]=="P":
			pol.append(i)
		else:
			thi.append(i)
	i,j=0,0
	print(pol,thi)
	while i<len(pol) and j<len(thi):
		if abs(pol[i]-thi[j])<=K:
			i+=1
			j+=1
			count+=1
		elif pol[i]>thi[j]:
			j+=1
		else:
			i+=1
	return count
	

arr=['T', 'T', 'P', 'P', 'T', 'P']
K=1
print(arr,K)
print(policeAndThieves(arr,K))
