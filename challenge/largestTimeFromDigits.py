"""
largestTimeFromDigits
"""
maxTime=0

def numberFromArr(arr):
	su=0
	for i in arr:
		su=su*10+i
	return su
def isTime(N):
	hh=N//100
	mm=N%100
	if hh in range(24) and mm in range(60):
		return True
	return False

def compareTime(a,b):
	if None in (a,b):
		return False
	if b==float("-INF") and isTime(a):
		return True
	if isTime(a) and isTime(b):
		hhA,mmA=a//100,a%100
		hhB,mmB=b//100,b%100
		if hhA>hhB or (hhA==hhB and mmA>=mmB):
			return True
	return False

def permutation(arr,l,r):
	global maxTime
	if l==r:
		tmp=numberFromArr(arr)
		#print(maxTime,tmp)
		if compareTime(tmp,maxTime):
			maxTime=tmp
	else:
		for i in range(l,r+1):
			arr[l],arr[i]=arr[i],arr[l]
			permutation(arr,l+1,r)
			arr[l],arr[i]=arr[i],arr[l]

def largestTimeFromDigits(arr,index=0):
	global maxTime
	if arr is None:
		return None
	n=len(arr)
	permutation(arr,0,n-1)

arr=[5,4,0,2]
largestTimeFromDigits(arr)
print("Maximum Time possible:",maxTime)
maxTime=0
arr=[9,9,9,9]
largestTimeFromDigits(arr)
print("Maximum Time possible:",maxTime)
