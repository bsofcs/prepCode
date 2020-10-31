"""
jobScheduleLossMin
"""
def mergeSort(arr):
	if arr is None or not len(arr):
		return
	if len(arr)==1:
		return arr
	mid=len(arr)//2
	Larr=mergeSort(arr[:mid])
	Rarr=mergeSort(arr[mid:])
	i=j=k=0
	while i<len(Larr) and j<len(Rarr):
		if compare(Larr[i],Rarr[j]):
			arr[k]=Larr[i]
			i+=1
		else:
			arr[k]=Rarr[j]
			j+=1
		k+=1
	while i<len(Larr):
		arr[k]=Larr[i]
		i+=1
		k+=1
	while j<len(Rarr):
		arr[k]=Rarr[j]
		j+=1
		k+=1
	return arr

def compare(X,Y):
	return X[0]*Y[1]>X[1]*Y[0]

def jobScheduleLossMin(L,T):
	if None in (L,T):
		return None
	n=len(T)
	arr=[[L[i],T[i]] for i in range(n)]
	arr=mergeSort(arr)
	print([arr[i][0] for i in range(n)])
	s=0
	L=[arr[i][0] for i in range(n)]
	T=[arr[i][1] for i in range(n)]
	print(L,T)
	for i in range(n):
		tme=sum(T[:i])
		s+=tme*L[i]
	print(s)
L=[3,4,1,2]
T=[4,5,1000,2]
print(L,T)
s=0
for i in range(len(L)):
		tme=sum(T[:i])
		s+=tme*L[i]
print(s)
jobScheduleLossMin(L,T)