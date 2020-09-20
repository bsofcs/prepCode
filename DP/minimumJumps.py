"""
minimumJumps
"""
def minimumJumpRecursive(arr):
	if arr is None:
		return None
	n=len(arr)
	index=0
	return RecursiveUtil(arr,index,n-1)

def RecursiveUtil(arr,l,h):
	if h==l:
		return 0
	if arr[l]==0:
		return float("INF")
	mn=float("inf")
	for i in range(l+1,h+1):
		if i<l+arr[l]+1:
			jump=RecursiveUtil(arr,i,h)
			if jump!=float("INF") and jump+1<mn:
				mn=jump+1
	return mn

def minimumJumps(arr):
	if arr is None:
		return None
	n=len(arr)
	m=[0]*n
	for i in range(n-2,-1,-1):
		if arr[i]==0:
			m[i]=float("INF")
		elif arr[i]+i>n-1:
			m[i]=1
		else:
			mn=float("INF")
			for j in range(i+1,n):
				if j<=arr[i]+i and mn>m[j]:
					mn=m[j]
			if mn!=float("INF"):
				m[i]=mn+1
			else:
				m[i]=mn
	print(arr,"\n",m)
	return(m[0] if m[0]!=float("INF") else -1)

#another way to solve
def minJumps(arr, n): 
    jumps = [0 for i in range(n)] 
  
    if (n == 0) or (arr[0] == 0): 
        return float('inf') 
  
    jumps[0] = 0
  
    # Find the minimum number of  
    # jumps to reach arr[i] from  
    # arr[0] and assign this  
    # value to jumps[i] 
    for i in range(1, n): 
        jumps[i] = float('inf') 
        for j in range(i): 
            if (i <= j + arr[j]) and (jumps[j] != float('inf')): 
                jumps[i] = min(jumps[i], jumps[j] + 1) 
                break
    return jumps[n-1] 

#2 3 1 1 2 4 2 0 1 1
arr=list(map(int,input().split()))
print(minimumJumps(arr))
print(minimumJumpRecursive(arr))