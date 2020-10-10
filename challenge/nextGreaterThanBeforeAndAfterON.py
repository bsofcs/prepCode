"""
nextGreaterThanBeforeAndAfterON
We need to find the "next-Greater-than", before and after the number in an array in one pass i.e. O(n).
Put -1 if there is any for a given element.
"""
def nextGreaterOn2(arr):
	if arr is None:
		return None,None
	n=len(arr)
	after=[-1]*n
	before=[-1]*n
	for i in range(n):
		for j in range(i+1,n):
			if arr[j]>arr[i]:
				after[i]=arr[j]
				break
	for i in range(n-1,-1,-1):
		for j in range(i-1,-1,-1):
			if arr[j]>arr[i]:
				before[i]=arr[j]
				break
	return after,before

def nextGreaterON(arr):
	if arr is None:
		return None,None
	n=len(arr)
	after=[-1]*n
	before=[-1]*n
	sA=[-1]
	sB=[-1]
	for i in range(n):
		j=n-1-i
		while sA[len(sA)-1]<=arr[j]:
			if len(sA)==1:
				break
			sA.pop()
		after[j]=sA[len(sA)-1]
		sA.append(arr[j])
		while sB[len(sB)-1]<=arr[i]:
			if len(sB)==1:
				break
			sB.pop()
		before[i]=sB[len(sB)-1]
		sB.append(arr[i])
	return after,before
		

a=[[2,5,0,9,6,3,3,5],[1,2,3,4,5,6],[8,7,5,4,3,2,1]]
for arr in a:
	print(arr)
	a,b=nextGreaterOn2(arr)
	print("After:",a,"\nBefore:",b)
	a,b=nextGreaterON(arr)
	print("After:",a,"\nBefore:",b)
	print("\n\n")