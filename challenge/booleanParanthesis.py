"""
booleanParenthesis
"""
global m
def booleanParanthesisRec(arr,i,j,isTrue):
	if arr is None or i is None or j is None or isTrue is None:
		return None
	if i==j:
		return isTrue=="T" if arr[i]=="T" else isTrue=="F"
	tmp=0
	for k in range(i+1,j,2):
		leftTrue=booleanParanthesisRec(arr,i,k-1,"T")
		leftFalse=booleanParanthesisRec(arr,i,k-1,"F")
		rightTrue=booleanParanthesisRec(arr,k+1,j,"T")
		rightFalse=booleanParanthesisRec(arr,k+1,j,"F")
		if arr[k]=="|":
			tmp+= leftTrue*rightFalse + leftTrue*rightTrue + leftFalse*rightTrue if isTrue=="T" else leftFalse*rightFalse
		if arr[k]=="&":
			tmp+= leftTrue*rightTrue if isTrue=="T" else leftFalse*rightFalse + leftTrue*rightFalse + leftFalse*rightTrue
		if arr[k]=="^":
			tmp+= leftTrue*rightFalse + leftFalse*rightTrue if isTrue=="T" else leftTrue*rightTrue + leftFalse*rightFalse
	return tmp

def booleanParanthesis(arr):
	global m
	if arr is None:
		return None
	n=len(arr)
	if n==1:
		return 1 if arr[0]=="T" else 0
	#first is True and second is False
	m=[[[-1,-1] for _ in range(n)] for _ in range(n)]
	boolUtil(arr,0,n-1,"T")
	return m[0][n-1][0]

def boolUtil(arr,i,j,isTrue):
	global m
	if i>j:
		return False
	if i==j:
		return isTrue=="T" if arr[i]=="T" else isTrue=="F"
	index=0 if isTrue=="T" else 1
	if m[i][j][index]!=-1:
		return m[i][j][index]
	tmp=0
	for k in range(i+1,j,2):
		leftTrue=boolUtil(arr,i,k-1,"T")
		leftFalse=boolUtil(arr,i,k-1,"F")
		rightTrue=boolUtil(arr,k+1,j,"T")
		rightFalse=boolUtil(arr,k+1,j,"F")
		if arr[k]=="|":
			tmp+= leftTrue*rightFalse + leftTrue*rightTrue + leftFalse*rightTrue if isTrue=="T" else leftFalse*rightFalse
		if arr[k]=="&":
			tmp+= leftTrue*rightTrue if isTrue=="T" else leftFalse*rightFalse + leftTrue*rightFalse + leftFalse*rightTrue
		if arr[k]=="^":
			tmp+= leftTrue*rightFalse + leftFalse*rightTrue if isTrue=="T" else leftTrue*rightTrue + leftFalse*rightFalse
	m[i][j][index]=tmp
	return tmp

def booleanParanthesisDP(arr):
	if arr is None:
		return None
	symb=[]
	oper=[]
	n_arr=len(arr)
	for i in range(n_arr):
		if arr[i] in ["T","F"]:
			symb.append(arr[i])
		else:
			oper.append(arr[i])
	n=len(symb)
	F=[[0 for i in range(n+1)] for i in range(n+1)]
	T=[[0 for i in range(n+1)] for i in range(n+1)]
	for i in range(n):
		if symb[i]=="F":
			F[i][i]=1
		else:
			F[i][i]=0
		if symb[i]=="T":
			T[i][i]=1
		else:
			T[i][i]=0
	for gap in range(1,n):
		i=0
		for j in range(gap+1,n):
			T[i][j]=F[i][j]=0
			for g in range(gap):
				k=i+g
				tik=T[i][k]+F[i][k]
				tjk=T[j][k]+F[j][k]
				if oper[k]=="&":
					T[i][j]+=T[i][k]*T[k+1][j]
					F[i][j]+=(tik*tjk-T[i][k]*T[k+1][j])
				if oper[k]=="|":
					F[i][j]+=F[i][k]*F[k+1][j]
					T[i][j]+=(tik*tjk-F[i][k]*F[k+1][j])
				if oper[k]=="^":
					T[i][j]+=(F[i][k]*T[k+1][j]+T[i][k]*F[k+1][j])
					F[i][j]+=(F[i][k]*F[k+1][j]+T[i][k]*T[k+1][j])
			i+=1
#	print(T)
	return T[0][n-1]


arr="T^F|T&F"
print(booleanParanthesisDP(list(arr)))
arr="T|F^F&T|F^F^F^T|T&T^T|F^T^F&F^T|T^F"
print(booleanParanthesisDP(list(arr)))
arr="T&T|F|F^F^T^T^T&T^F^T&F|F^F^F&F&F|F|F^F^T|T&T"
print(booleanParanthesisDP(list(arr)))
arr="T"
print(booleanParanthesisDP(list(arr)))