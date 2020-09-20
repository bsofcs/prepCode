"""
anyTwoSubsetWithSameSum
"""

def allPossibleSubset(arr):
	if arr is None:
		return None
	n=len(arr)
	allPoss=[[]]
	for i in range(2**n):
		tmp=[]
		a_i=(list(bin(i))[2:])[::-1]
		for j in range(len(a_i)):
			if a_i[j]=="1":
				tmp.append(arr[n-1-j])
		if len(tmp):
			allPoss.append(tmp[::-1])
	return allPoss

def anyTwoSubsetWithSameSum(arr):
	allPoss=allPossibleSubset(arr)
	print("Input Array:",arr)
	n=len(allPoss)
	flag=0
	for i in range(n):
		for j in range(1,i):
			if sum(allPoss[i])==sum(allPoss[j]):
				print("Sets:",allPoss[i]," & ",allPoss[j])
				flag+=1
	if flag==0:
		print("No such pair of set")
	else:
		print(f"There are {flag} such pairs")

arr=[11,4,2,5]
anyTwoSubsetWithSameSum(arr)
arr=[11,4,5,3,6,7,2,9]
anyTwoSubsetWithSameSum(arr)