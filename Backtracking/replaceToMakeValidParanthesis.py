"""
replaceToMakeValidParanthesis
Input="()())()"
Output: ()()() (())()

Input="(v)())()"
Output:(v)()()  (v())()
"""

def isValid(str):
	if str is None:
		return 
	n=len(str)
	stk=[]
	for i in range(n):
		if str[i]=="(":
			stk.insert(0,")")
		elif str[i]==")":
			if len(stk)==0:
				return False
			stk.pop(0)
	if len(stk)==0:
		return True
	return False

def replaceToMakeValidParanthesis(str):
	if str is None:
		return None
	if isValid(str):
		print(str)
		return 
	visit=set()
	q=[]
	level=0
	q.append(str)
	visit.add(str)
	while(len(q)):
		str=q[0]
		q.pop(0)
		if isValid(str):
			print(str)
			level=True
		if level:
			continue
		for i in range(len(str)):
			if str[i] not in ("(",")"):
				continue
			tmp=str[:i]+str[i+1:]
			if tmp not in visit:
				q.append(tmp)
				visit.add(tmp)
str="()())()"
replaceToMakeValidParanthesis(str)
str="(v)())()"
replaceToMakeValidParanthesis(str)
str="(v)((((((()"
replaceToMakeValidParanthesis(str)