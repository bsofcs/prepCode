"""
LongestSubstringPalindrome
Approaches:
1. BruteForce: LongestSubstringPalindrome
2. DP: LongestSubstringPalindromeDP
"""

def LongestSubstringPalindrome(arr):
	if arr is None:
		return None
	arr="$"+"$".join(list(arr))+"$"
	n=len(arr)
	m=[0]*n
	mn=float("-INF")
	for i in range(1,n):
		for k in range(i+1):
			#print(i,k,i+k,i-k,m[i])
			if k==0:
				m[i]=1
			elif i+k>=n or i-k<0:
				break
			elif arr[i+k]==arr[i-k]:
				m[i]+=2
			else:
				break
		mn=max(mn,m[i])
	return mn//2

def count(m):
	n=len(m)
	c=0
	for i in range(n):
		c+=sum(m[i])
	return c

def LongestSubstringPalindromeDP(arr):
	if arr is None:
		return None
	n=len(arr)
	m=[[0 for _ in range(n)] for _ in range(n)]
	for i in range(n):
		m[i][i]=1
	mx=1
	allStr=list(arr)
	for l in range(2,n+1):
		for i in range(n-l+1):
			j=i+l-1
			if arr[i]==arr[j] and (m[i+1][j-1]==1 or l==2):		# we can use l==2 or i+1>j-1
				m[i][j]=1
				mx=max(mx,j-i+1)
				if arr[i:j+1] not in allStr: allStr.append(arr[i:j+1])
	#for i in range(n):
	#	print(m[i])
	print("Count:",count(m))
	print("All Substring Palindrome:",allStr)
	return mx

a=["a","abaab","abaxabaxabb","abaxabaxabybaxabyb","Bhanuaun","geeksforskeeg","geeksforrofskeeg","geeksforgeekkeegs"]
for arr in a:
	print(arr)
	print("BF:",LongestSubstringPalindrome(arr))
	print("DP:",LongestSubstringPalindromeDP(arr))