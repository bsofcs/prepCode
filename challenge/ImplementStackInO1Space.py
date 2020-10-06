"""
ImplementStackInO1Space
"""
global mn
def push(arr,ele):
	global mn
	if arr is None:
		arr=[ele]
		mn=ele
	elif ele<mn:
		arr.append(2*ele-mn)
		mn=ele
	else:
		arr.append(ele)
def pop(arr):
	global mn
	if len(arr)==0:
		return None
	else:
		ele=arr.pop()
		if mn>ele:
			mn=2*mn-ele
		return ele

def isFull(n,arr):
	return len(arr)==n
def isEmpty(arr):
	return len(arr)==0
def getMin(n,arr):
	global mn
	if len(arr)==0:
		return None
	else:
		return mn
if __name__=="__main__":
	t=int(input("Enter Number of Test Cases:"))
	for i in range(t):
		mn=float("INF")
		arr=list(map(int,input("Enter the array:").strip().split()))
		n=len(arr)
		stck=[]
		for i in range(n):
			push(stck,arr[i])
		print(getMin(n,stck))
		pop(stck)
		n-=1
		print(getMin(n,stck))