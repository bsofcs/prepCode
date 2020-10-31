"""
arrangeNumbersInSpecificManner
Given a number "n", we need to create an array of "2*n" elements. The array will have every element between from 1 to n with occurence of 2.
The gap between the two occurence should be equal to the number of the element as that of the value:. Example:
Input: 4
Output: 4 1 3 1 2 4 3 2
Input: 5
Output: Not possible 
"""
def fill(res,curr,n):
	if curr==0:
		return True
	for i in range(2*n-curr-1):
		if res[i]==0 and res[i+curr+1]==0:
			res[i]=res[i+curr+1]=curr
			if fill(res,curr-1,n):
				return True
			res[i]=res[i+curr+1]=0
	return False

def arrangeNumbersInSpecificManner(n):
	if n is None:
		return None
	res=[0]*(2*n)
	if fill(res,n,n):
		for i in range(2*n):
			print(res[i],end=" ")
		print()
	else:
		print("Not Possible")

for N in range(1<<4):
	print(N,":",end="")
	arrangeNumbersInSpecificManner(N)