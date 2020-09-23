"""
longestAlternatingSequence
A sequence {x1, x2, .. xn} is alternating sequence if its elements satisfy one of the following relations
x1<x2>x3<x4>x5<...xn
x1>x2<x3>x4<x5>...xn
"""

def longestAlternatingSequence(arr):
	if arr is None:
		return None
	n=len(arr)
	las=[[1,1] for i in range(n)]
	res=1
	for i in range(1,n):
		for j in range(i):
			if arr[j]<arr[i] and las[i][0]<las[j][0]+1:
				las[i][0]=las[j][1]+1
			if arr[j]>arr[i] and las[i][1]<las[j][0]+1:
				las[i][1]=las[j][0]+1
			print(i,j,arr[i],arr[j],las[i])
		res=max(res,max(las[i]))
	for i in range(n):
		print(las[i])
	print(res)
arr=[1,5,4]
print(arr)
print(longestAlternatingSequence(arr))
print(arr)
arr=[10,22,9,33,49,50,31,60]
print(longestAlternatingSequence(arr))	