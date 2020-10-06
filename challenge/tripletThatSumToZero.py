"""
tripletThatSumToZero
"""
def QuickSort(arr,low,high):
	if low<high:
		pivot=partition(arr,low,high)
		QuickSort(arr,pivot+1,high)
		QuickSort(arr,low,pivot-1)

def partition(arr,low,high):
	pivot=arr[high]
	i=low-1
	for j in range(low,high):
		if arr[j]<=pivot:
			i+=1
			arr[i],arr[j]=arr[j],arr[i]
	arr[i+1],arr[high]=arr[high],arr[i+1]
	return i+1

def tripletThatSumToZero(arr):
	if arr is None:
		return
	n=len(arr)
	QuickSort(arr,0,n-1)
	print(arr)
	for pivot in range(n-2):
		i=pivot+1
		j=n-1
		while i<j:
			tmp=arr[pivot]+arr[i]+arr[j]
			if tmp==0:
				print(arr[pivot],arr[i],arr[j])
				break
			elif tmp<0:
				i+=1
			else:
				j-=1
arr=[0,1,2,-3,-1]
tripletThatSumToZero(arr)
arr=[97,-27,2,-34,61,-39]
tripletThatSumToZero(arr)