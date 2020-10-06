"""
inFlightMovies
"""
def quickSort(arr,start,end):
	if start<end:
		pivot=partition(arr,start,end)
		quickSort(arr,start,pivot-1)
		quickSort(arr,pivot+1,end)

def partition(arr,start,end):
	pivot=arr[end]
	i=start-1
	for j in range(start,end):
		if arr[j]<=pivot:
			i+=1
			arr[i],arr[j]=arr[j],arr[i]
	arr[i+1],arr[end]=arr[end],arr[i+1]
	return i+1

def inFlightMovies(arr,k):
	if arr is None or k is None:
		return
	n=len(arr)
	quickSort(arr,0,n-1)
	i,j=0,n-1
	mn=float("INF")
	f1=f2=None
	while i<j:
		if arr[i]==K:
			return arr[i],None
		elif arr[j]==K:
			return arr[j],None
		elif arr[i]+arr[j]==K:
			return arr[i],arr[j]
		elif arr[i]+arr[j]>K:
			j-=1
		else:
			if mn>(K-arr[i]-arr[j]):
				mn=K-(arr[i]+arr[j])
				f1,f2=arr[i],arr[j]
			#print(mn,f1,f2,arr[i])
			i+=1
	return f1,f2

arr=[27, 1,10, 39, 12, 52, 32, 67, 76]
k=[57,45,23,12,77,32,0]
for K in k:
	print(K,":",inFlightMovies(arr,K))