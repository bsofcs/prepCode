"""
printAllBalancedParathesisStrings
"""

def printAllBalancedParathesisStrings(N):
	if N is None:
		return 
	if N==0:
		return[]
	if N==1:
		return["{}"]
	result=printAllBalancedParathesisStrings(N-1)
	res=[]
	for i in result:
		if "{}"+i not in res:
			res.append("{}"+i)
		if i+"{}" not in res:
			res.append(i+"{}")
		if "{"+i+"}" not in res:
			res.append("{"+i+"}")
	return res

N=11
arr=[]
c=0
for i in range(N):
	temp=printAllBalancedParathesisStrings(i)
	arr.append(len(temp))
	c+=1
	print(i,len(temp))