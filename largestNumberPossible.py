"""
largestNumberPossible
"""
def largestNumberPossible(N,S):
	if N is None or S is None:
		return -1	
	if 9*N<S or (N>1 and S==0):
		return -1
	digit=[]
	for i in range(N):
		val=min(9,S)
		digit.append(val)
		S-=val
	result=0
	for i in range(len(digit)):
		result=result*10+digit[i]
	return result

if __name__=='__main__':
	t=int(input())
	for i in range(t):
		ns=list(map(int, input().rstrip().split()))
		N,S=ns[0],ns[1]
		result=largestNumberPossible(N,S)
		print(result)