"""
maximumToys

"""
def MergeSort(arr):
	if arr is None:
		return None
	n=len(arr)
	if n<=1:
		return
	mid=n//2
	L=arr[:mid]
	R=arr[mid:]
	MergeSort(L)
	MergeSort(R)
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
		i+=1
		k+=1
	while j<len(R):
		arr[k]=R[j]
		j+=1
		k+=1
	

def maximumToys(n,k,toys):
	MergeSort(toys)
	print(n,k,toys)
	result=0
	for i in range(n):
		if toys[i]<=k:
			result+=1
			k-=toys[i]
	return result
n=7
k=50
t_ip="1 12 5 111 200 1000 10"
toys=[int(i) for i in t_ip.split()]
result=maximumToys(n,k,toys)
print(result)

"""
if __name__=='__main__':
	t=int(input())
	for i in range(t):
		cred=input()
		n=int(cred.split()[0])
		k=int(cred.split()[1])
		t_ip=input()
		toys=[int(i) for i in t_ip.split()]
		result=maximumToys(n,k,toys)
		print(result)
"""