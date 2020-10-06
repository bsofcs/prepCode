"""
moveZerosToEnd
Input: 4,7,0,1,3,0,-1,0,0
Output: 4,7,1,3,-1,0,0,0,0

Input: 0,0,-1,2,0,0
Output: -1,2,0,0,0,0
"""
def moveZerosToEnd(arr):
	if arr is None:
		return
	n=len(arr)
	count=0
	i=0
	while i<len(arr):
		if arr[i]==0:
			arr.pop(i)
			count+=1
		else:
			i+=1
	for i in range(count):
		arr.append(0)
	return arr

def moveZerosToEndTry1(arr):
	if arr is None:
		return
	n=len(arr)
	i=0
	for j in range(n):
		if arr[j]!=0:
			arr[i],arr[j]=arr[j],arr[i]
			i+=1
	return arr

def moveZerosToEndTry2(arr):
	return [i for i in arr if i!=0]+[i for i in arr if i==0]

def moveZerosToEndTry3(arr):
	n=len(arr)
	j=0
	for i in range(n):
		if arr[i]!=0 and arr[j]==0:
			arr[i],arr[j]=arr[j],arr[i]
			i+=1
		if arr[j]!=0:
			j+=1
	return arr
arr=[4,7,0,1,3,0,-1,0,0]
print(arr)
print(moveZerosToEnd(arr))
print(moveZerosToEndTry1(arr))
print(moveZerosToEndTry2(arr))
print(moveZerosToEndTry3(arr))
arr=[0,0,-1,2,0,0]
print(arr)
print(moveZerosToEnd(arr))
print(moveZerosToEndTry1(arr))
print(moveZerosToEndTry2(arr))
print(moveZerosToEndTry3(arr))