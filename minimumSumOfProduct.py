"""
minimumSumOfProduct
"""
def MergeSortAsc(arr):
	if A is None:
		return None
	n=len(arr)
	if n<2:
		return
	mid=n//2
	L=arr[mid:]
	R=arr[:mid]
	MergeSortAsc(L)
	MergeSortAsc(R)
	i=j=k=0
	while i<len(L) and j<len(R):
		if L[i]<R[j]:
			arr[k]=L[i]
			i+=1
		else:
			arr[k]=R[j]
			j+=1
		k+=1
	while i<len(L):
		arr[k]=L[i]
		i+=1;k+=1
	while j<len(R):
		arr[k]=R[j]
		j+=1;k+=1

def MergeSortDsc(arr):
	if A is None:
		return None
	n=len(arr)
	if n<2:
		return
	mid=n//2
	L=arr[mid:]
	R=arr[:mid]
	MergeSortDsc(L)
	MergeSortDsc(R)
	i=j=k=0
	while i<len(L) and j<len(R):
		if L[i]>R[j]:
			arr[k]=L[i]
			i+=1
		else:
			arr[k]=R[j]
			j+=1
		k+=1
	while i<len(L):
		arr[k]=L[i]
		i+=1;k+=1
	while j<len(R):
		arr[k]=R[j]
		j+=1;k+=1

def minimumSumOfProduct(A,B,n):
	MergeSortAsc(A)
	MergeSortDsc(B)
	result=A[0]*B[0]
	for i in range(1,n):
		result+=A[i]*B[i]
	return result

if __name__=='__main__':
	t=int(input())
	for i in range(t):
		n=int(input())
		A=list(map(int,input().rstrip().split()))
		B=list(map(int,input().rstrip().split()))
		result=minimumSumOfProduct(A,B,n)
		print(result)