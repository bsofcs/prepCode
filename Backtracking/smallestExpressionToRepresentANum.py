"""
smallestExpressionToRepresentANum
Given a digit D, a number N and set of expression {+,-,*,/}, with a limit of 10 expression, find the smallest Expression to represent the number.
Input: D=3 and N=7
Output: 3/3+3+3

Input: D=4 and N=7
Output: 4+4-4/4
"""
LIMIT=10
minimum=LIMIT
seen={}
operators=[]
def minLevel(total,N,D,level):
	global minimum
	if total==N:
		minimum=min(minimum,level)
		return
	if level==minimum:
		return
	if total%D==0:
		minLevel(total//D,N,D,level+1)
	minLevel(total+D,N,D,level+1)
	if total-D==0:
		minLevel(total-D,N,D,level+1)
	minLevel(total*D,N,D,level+1)

def generate(total,N,D,level):
	if total==N:
		return True
	if level==minimum:
		return False
	if seen.get(total) is None or seen.get(total)>=level:
		seen[total]=level
		divide=-1
		if total%D==0:
			divide=total//D
			if seen.get(divide) is None:
				seen[divide]=level+1
		addition=total+D
		if seen.get(addition) is None:
			seen[addition]=level+1
		substraction=-1
		if total-D>0:
			substraction=total-D
			if seen.get(substraction) is None:
				seen[substraction]=level+1
		multiplication=total*D
		if seen.get(multiplication) is None:
			seen[multiplication]=level+1
		if divide!=-1 and generate(divide,N,D,level+1):
			operators.append("/")
			return True
		if generate(addition,N,D,level+1):
			operators.append("+")
			return True
		if substraction!=-1 and generate(substraction,N,D,level+1):
			operators.append("-")
			return True
		if generate(multiplication,N,D,level+1):
			operators.append("*")
			return True
	return False

def smallestExpressionToRepresentANum(D,N):
	minLevel(D,N,D,1)
	if generate(D,N,D,1):
		expression=""
		if len(operators)>0:
			expression=str(D)+operators.pop()
			while len(operators)>0:
				popped=operators.pop()
				if popped in ["*","/"]:
					expression="("+expression+str(D)+")"+popped
				else:
					expression=expression+str(D)+popped
			expression+=str(D)
		print("\nFor N(",N,") and D(",D,"):\nExpression:",expression)
		print(seen)
	else:
		print("\nNo Expression Found")
if __name__=="__main__":
	N=[7,7,100,200]
	D=[3,4,7,9]
	for i in range(4):
		minimum=LIMIT
		seen={}
		smallestExpressionToRepresentANum(D[i],N[i])