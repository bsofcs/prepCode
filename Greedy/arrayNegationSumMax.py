"""
arrayNegationSumMax
Given an array of size n and a number k. We must modify array K number of times. 
Here modify array means in each operation we can replace any array element arr[i] by -arr[i]. 
We need to perform this operation in such a way that after K operations, sum of array must be maximum
"""
def arrayNegationSumMax(arr,K):
	if None in (arr,K):
		return
	arr.sort()
	print(arr)
	while K>0:
		index=arr.index(min(arr))
		if arr==0:
			K=0
		else:
			arr[index]=-1*arr[index]
			K-=1
	return sum(arr)

arr=[9,8,8,5]
K=3
print(arr,arrayNegationSumMax(arr,K))
arr=[-2, 0, 5, -1, 2]
K=4
print(arr,arrayNegationSumMax(arr,K))