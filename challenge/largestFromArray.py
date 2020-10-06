"""
largestFromArray
"""
def greaterThan(x,y):
	sX=list(str(x))
	sY=list(str(y))
	if len(sX)>len(sY):
		while len(sX)!=len(sY):
			sY.append(str(0))
	if len(sX)<len(sY):
		while len(sX)!=len(sY):
			sX.append(str(0))
	while sX and sY:
		if int(sY.pop())>int(sX.pop()):
			return False
	return True
def mergeSort(arr):
	n=len(arr)
	if n==1:
		return arr
	mid=n//2
	larr=mergeSort(arr[:mid])
	rarr=mergeSort(arr[mid:])
	lf,lr=len(larr),len(rarr)
	i=j=k=0
	while i<lf and j<lr:
		if greaterThan(larr[i],rarr[j]):
			arr[k]=larr[i]
			i+=1
		else:
			arr[k]=rarr[j]
			j+=1
		k+=1
	while i<lf:
		arr[k]=larr[i]
		i+=1
		k+=1
	while j<lr:
		arr[k]=rarr[j]
		j+=1
		k+=1
	return arr
def printLargest(arr):
	if arr is None:
		return
	n=len(arr)
	arr=mergeSort(arr)
	return "".join(map(str,arr))

a=[[3, 30, 34, 5, 9],[54, 546, 548, 60]]
print("Output should be 9534330 and 6054854654")
for arr in a:
	print(arr)
	print(printLargest(arr))