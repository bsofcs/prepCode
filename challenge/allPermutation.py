"""
allPermutation
"""
m=[]
def allPermutation(str):
	global m
	if str is None:
		return None
	n=len(str)
	tmp="".join(str)
	if tmp in m:
		return
	else:
		m.append(tmp)
	for i in range(n):
		for j in range(i+1,n):
			str[i],str[j]=str[j],str[i]
			allPermutation(str)
			str[i],str[j]=str[j],str[i]

str=list("ABC")
allPermutation(str)
print(m)