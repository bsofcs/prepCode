"""
booleanParanthesis
Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true. 
Given that there are three operators:
	1. AND	-	&
	2. OR	-	|
	3. XOR	-	^
where as the operands are True(T) and False(F)

Input: For example: T^F|T&F
there are following ways to get True:
1. (T^F)|(T&F)
2. T^(F|(T&F))
3. T^((F|T)&F)
"""
global m

def booleanParanthesisRecusion(str):
	if str is None:
		return None
	n=len(str)
	return bPUtil(str,0,n-1,True)

def bPUtil(str,i,j,isTrue):
	if i>j:
		return False
	if i==j:
		return isTrue==True if str[i]=="T" else isTrue==False
	k=i+1
	ans=0
	while k<j:
		leftTrue=bPUtil(str,i,k-1,True)
		leftFalse=bPUtil(str,i,k-1,False)
		rightTrue=bPUtil(str,k+1,j,True)
		rightFalse=bPUtil(str,k+1,j,False)
		if str[k]=="&":
			ans+=(leftTrue*rightTrue) if isTrue==True else (leftFalse*rightTrue)+(leftFalse*rightFalse)+(leftTrue*rightFalse)
		elif str[k]=="|":
			ans+=(leftFalse*rightTrue)+(leftTrue*rightFalse)+(leftTrue*rightTrue) if isTrue==True else (leftFalse*rightFalse)
		else:
			ans+=(leftFalse*rightTrue)+(leftTrue*rightFalse) if isTrue==True else (leftTrue*rightTrue)+(leftFalse*rightFalse)
		k+=2
	return ans		
		

def booleanParanthesisDP(str):
	global m
	if str is None:
		return None
	n=len(str)
	m=[[[-1,-1] for i in range(n)] for i in range(n)]
	#m[i][j][0]=True and m[i][j][1]=False
	bPDPUtil(str,0,n-1,True)
#	for i in range(n):
#		print(m[i])
	return m[0][n-1][0]

def bPDPUtil(str,i,j,isTrue):
	global m
	if i>j:
		return False
	if i==j:
		return isTrue==True if str[i]=="T" else isTrue==False
	index=0 if isTrue else 1
	if m[i][j][index]!=-1:
		return m[i][j][index]
	else:
		k=i+1
		ans=0
		while k<j:
			leftTrue=bPDPUtil(str,i,k-1,True)
			leftFalse=bPDPUtil(str,i,k-1,False)
			rightTrue=bPDPUtil(str,k+1,j,True)
			rightFalse=bPDPUtil(str,k+1,j,False)
			if str[k]=="&":
				ans+=(leftTrue*rightTrue) if isTrue==True else (leftFalse*rightTrue)+(leftFalse*rightFalse)+(leftTrue*rightFalse)
			elif str[k]=="|":
				ans+=(leftFalse*rightTrue)+(leftTrue*rightFalse)+(leftTrue*rightTrue) if isTrue==True else (leftFalse*rightFalse)
			else:
				ans+=(leftFalse*rightTrue)+(leftTrue*rightFalse) if isTrue==True else (leftTrue*rightTrue)+(leftFalse*rightFalse)
			k+=2
	m[i][j][index]=ans
	return ans

str="T|T&F^T"
print(str, end="-")
print(booleanParanthesisRecusion(str))
print(booleanParanthesisDP(str))
str="T^F|T&F"
print(str, end="-")
print(booleanParanthesisRecusion(str))
print(booleanParanthesisDP(str))