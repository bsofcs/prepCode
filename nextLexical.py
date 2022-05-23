"""
nextLexical
"""

def nextLexical(arr):
	if arr is None:
		return
	n=len(arr)
	l_arr=list(arr)
	pivot=-1
	for i in range(n-2,-1,-1):
		if l_arr[i]<l_arr[i+1]:
			pivot=i
			break
	if pivot==-1:
		return arr
	result=l_arr[:pivot]
	l_arr[i],l_arr[i+1]=l_arr[i+1],l_arr[i]
	result.append(l_arr[pivot])
	result.extend(sorted(l_arr[pivot+1:]))
	return "".join(result)

arr="ATLAS"
print(nextLexical(arr))
arr="COCHIN"
print(nextLexical(arr))
arr="ALPHA"
print(nextLexical(arr))
arr="BHANU"
print(nextLexical(arr))