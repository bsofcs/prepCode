"""
indexSubstringPalindrome
"""
def count(m):
	n=len(m)
	c=0
	for i in range(n):
		c+=sum(m[i])
	return c

def indexSubstringPalindromeDP(arr,start,end):
	if arr is None:
		return None
	n=len(arr)
	if start<0 and end>=n:
		return None
	m=[[0 for _ in range(n)] for _ in range(n)]
	allStr=[]
	for i in range(n):
		m[i][i]=1
		if start==0:
			allStr.append(arr[i])
	for l in range(2,n+1):
		for i in range(n-l+1):
			j=i+l-1
			if arr[i]==arr[j] and (m[i+1][j-1]==1 or l==2):		# we can use l==2 or i+1>j-1
				m[i][j]=1
				if arr[i:j+1] not in allStr and (i>=start and j<=end): allStr.append(arr[i:j+1])
	#for i in range(n):
	#	print(m[i])
	return allStr

def noOfSubstringPalindromeWithLenKDP(arr,ln):
	if arr is None and l==0:
		return None
	n=len(arr)
	m=[[0 for _ in range(n)] for _ in range(n)]
	allStr=[]
	for i in range(n):
		m[i][i]=1
		if ln==1:
			allStr.append(arr[i])
	for l in range(2,n+1):
		for i in range(n-l+1):
			j=i+l-1
			if arr[i]==arr[j] and (m[i+1][j-1]==1 or l==2):		# we can use l==2 or i+1>j-1
				m[i][j]=1
				if arr[i:j+1] not in allStr and (j-i+1)==ln: allStr.append(arr[i:j+1])
	#for i in range(n):
	#	print(m[i])
	return allStr

a=["a","abaab","abaxabaxabb","abaxabaxabybaxabyb","Bhanuaun","geeksforskeeg","geeksforrofskeeg","geeksforgeekkeegs"]
for arr in a:
	print(arr)
	print("In range of Index:",indexSubstringPalindromeDP(arr,3,8))
	print("of Length 5:",noOfSubstringPalindromeWithLenKDP(arr,5))