"""
wordBreak
Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. See following examples for more details
Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice, cream, icecream, man, go, mango}
Input: ilike
Output: Yes
explanantion: "i like"

Input: idontlike
Output: No
Explanation: "i dont like" AND "dont is not present"
"""

def wordbreak(str,dictionary):
	if str is None or dictionary is None:
		return None
	if str in dictionary:
		return True
	n=len(str)
	for i in range(1,n):
		#print(str[:i],str[i:])
		if wordbreak(str[:i],dictionary) and wordbreak(str[i:],dictionary):
			return True
	return False
global m
def wordBreakDP(str,dictionary):
	if str is None or dictionary is None:
		return None
	n=len(str)
	m=[[0 for _ in range(n)] for _ in range(n)]
	for i in range(n):
		m[i][i]= 1 if str[i] in dictionary else 0
	for l in range(2,n+1):
		for i in range(n-l+1):
			j=i+l-1
			if str[i:j+1] in dictionary:
				m[i][j]=1
			else:
				for k in range(i+1,j):
					if m[i][k-1]==1 and m[k][j]==1:
						m[i][j]=1
						break
	#for i in range(n):
	#	print(m[i])
	return m[0][n-1]

dd=" like, i, sam, sung, samsung, mobile, ice, cream, icecream, man, go, mango"
print("Dictionary:",dd,"\n")
dictionary=list(map(lambda x: x.strip(),dd.split(",")))
s=["i","ilike","idontlike","ilikesamng","icecreamgoman","mangoman","igolikesunsg","gogogogo"]
for str in s:
	print(str," :\nRecursive:",wordbreak(str,dictionary),"\nDP:",wordBreakDP(str,dictionary),"\n")
dictionary="Bhanu"
print("Dictionary:",dictionary,"\n")
str="BhanuBhanu"
print(str," :\nRecursive:",wordbreak(str,dictionary),"\nDP:",wordBreakDP(str,dictionary),"\n")