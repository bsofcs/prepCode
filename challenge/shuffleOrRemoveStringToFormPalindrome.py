"""
shuffleOrRemoveStringToFormPalindrome
"""

def shuffleOrRemoveStringToFormPalindrome(str):
	if str is None:
		return
	n=len(str)
	d=dict()
	for i in range(n):
		if str[i] in d:
			d[str[i]]+=1
		else:
			d[str[i]]=1
	keys=[i for i in d.keys()]
	values=[i for i in d.values()]
	nC=len(keys)
	evenChar=[[keys[i],values[i]] for i in range(nC) if values[i]%2==0]
	oddChar=[[keys[i],values[i]] for i in range(nC) if values[i]%2]
	if oddChar:
		oddChar.sort(key=lambda x:x[1], reverse=True)
		evenChar.append(oddChar[0])
	strLR=""
	nC=len(evenChar)
	for i in range(nC-1):
		strLR+=string_append(evenChar[i][0],int(evenChar[i][1]/2))
	return(strLR+string_append(evenChar[nC-1][0],evenChar[nC-1][1])+strLR[::-1])

def string_append(a,n):
	o=""
	for i in range(n):
		o+=a
	return o


s=["geeksforgeeks","abc","abrakadabra","aaacccccdoodle"]
for str in s:
	print(str,":",shuffleOrRemoveStringToFormPalindrome(str))