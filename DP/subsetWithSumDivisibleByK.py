"""
subsetWithSumDivisibleByK
"""
def subsetWithSumDivisibleByK(arr,K):
	if None in (arr,K):
		return
	n=len(arr)
	if n>K:
		return "NO"
	DP=[False for i in range(K)]
	for i in range(n):
		if DP[0]:
			return "YES"
		temp=[False for _ in range(K)]
		for j in range(K):
			if DP[j]==True:
				if DP[(j+arr[i])%K]==False:
					temp[(j+arr[i])%K]=True
		for j in range(K):
			if temp[j]:
				DP[j]=True
		DP[arr[i]%K]=True
	return DP[0]
arr=[3, 1, 7, 5]
K=10
print(subsetWithSumDivisibleByK(arr,K))