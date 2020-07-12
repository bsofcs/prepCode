"""
minimumHeightDiff
"""
def minimumHeightDiff(arr,n,k):
	if arr is None or n is None or k is None:
		return None
	if n==1:
		return 0
	arr.sort()
	result=arr[n-1]-arr[0]
	small=arr[0]+k
	big=arr[n-1]-k
	if small>big:
		small,big=big,small
	for i in range(1,n-1):
		substract=arr[i]-k
		add=arr[i]+k
		if substract>=small or add<=big:
			continue
		if (big-substract)<=(add-small):
			small=substract
		else:
			big=add
	return min(result,big-small)

if __name__=='__main__':
	t=int(input())
	for i in range(t):
		k=int(input())
		n=int(input())
		arr=list(map(int,input().rstrip().split()))
		result=minimumHeightDiff(arr,n,k)
		print(result)