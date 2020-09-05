"""
longestIncreasingSubsequence
Given a sequence of n number A1,A2,...,An; determine a subsequence (not necessarily contiguous) of maximum length in which the values in the subsequence from a strictly increasing sequence.

Approach 1: Using Recursion
Here we create a tree, where every node at level one represents the starting point of every increasing subsequence.
Every Node returns the value of the branch which starts at the node with the largest lenght.
While backtracking we reach the root with the longest subsequence value.
Code: longestIncreasingSubsequenceBT
Complexity: Exponential

Approach 2: Using DP
We create the array of length equal to input and calucalting the longest increasing subsequence of the array till that element.
We must initialize the new array because at a single length sub-array each element is the longest subsequence in itself.
Code: longestIncreasingSubsequenceDP
Complexity: O(n**2)

Approach 3: Using Patience Sorting Technique
In this approach, we create two arrays "T" and "R" of the same length that of the input array. T will store the temporary results whereas R will store the final results. We keep another variable "len" that will keep the length of the longest increasing subsequence till now. We store in T the end of the each longest increasing sequences' index value.
Code: longestIncreasingSubsequencePS
Complexity: O(nlogn)
"""
global maximum
def longestIncreasingSubsequence(arr):
	if arr is None:
		return None
	n=len(arr)
	m=[1]*n
	for i in range(n):
		for j in range(i):
			if arr[j]<arr[i]:
				m[i]=max(m[i],m[j]+1)
	return max(m)

def BTUtil(arr,n):
	global maximum
	if arr is None:
		return None
	if n==1:
		return 1
	maxEndingHere=1
	for i in range(1,n):
		res=BTUtil(arr,i)
		if arr[i-1]<arr[n-1] and res+1>maxEndingHere:
			maxEndingHere=res+1
	maximum=max(maximum,maxEndingHere)
	return maxEndingHere

def longestIncreasingSubsequenceBT(arr):
	global maximum
	maximum=1
	if arr is None:
		return None
	n=len(arr)
	BTUtil(arr,n)
	print(maximum)

def ceilIndex(arr,T,l,val):
	if arr is None or T is None or l is None or val is None:
		return None
	start=0
	end=l
	while(start<=end):
		mid=start+(end-start)//2
		if arr[T[mid]]<val and arr[T[mid+1]]>=val:
			return mid+1
		elif arr[T[mid]]<val:
			start=mid+1
		else:
			end=mid-1
	return -1

def longestIncreasingSubsequencePS(arr):
	if arr is None:
		return None
	n=len(arr)
	R=[-1]*n
	T=[-1]*n
	l=T[0]=0
	print(arr)
	print(l,arr[0],T[:l+1],R)
	for i in range(1,n):
		if arr[T[0]]>arr[i]:
			T[0]=i
			#print("arr[T[0]]>arr[i]")
		elif arr[T[l]]<arr[i]:
			l+=1
			T[l]=i
			R[T[l]]=T[l-1]
			#print("arr[T[l]]<arr[i]")
		else:
			index=ceilIndex(arr,T,l,arr[i])
			T[index]=i
			R[T[index]]=T[index-1]
			#print("else",index)
		#print(i,arr[i],T[:l+1],R)
	index=T[l]
	temp=[]
	while(index>-1):
		temp.append(arr[index])
		index=R[index]
	print(temp[::-1])
	return l+1

arr=[5,6,2,3,4,1,9,9,8,9,5]
print(longestIncreasingSubsequence(arr))
longestIncreasingSubsequenceBT(arr)
print(longestIncreasingSubsequencePS(arr))

arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]
print(longestIncreasingSubsequence(arr))
longestIncreasingSubsequenceBT(arr)
