"""
minimumOperation
Given there are two following ways to increase a number X:
	1. Increment by 1, i.e. X+1
	2. Multiply by 2, i.e. 2*X
Find the minimum number of operations needed to reach to a given number "N" from 0.
For ex:
N=8
0+1=1,1+1=2,2*2=4,4*2=8
o/p:4

N=7
0+1=1,1+1=2,2+1=3,3*2=6,6+1=7
o/p=5
Code: minimumOperation2Operator
"""

def minimumOperation2Operator(N):
	if N is None:
		return None
	m=[0]*(N+1)
	for i in range(1,N+1):
		pls=m[i-1]+1
		mul=float("INF") if i%2 else m[i//2]+1
		m[i]=min(pls,mul)
	print([str(i)+":"+str(m[i]) for i in range(N+1)])
	return m[N]

N=300
print(minimumOperation2Operator(N))