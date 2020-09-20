"""
tilingProblem
Assume that we use dominoes measuring 2X1 to tile an infinte strip of height 2.
How many ways can one tile a 2Xn strip of square cells with 1X2 dominoes
for ex:
1. l
2. ll,=
3. lll,=l,l=
4. llll,==,ll=,=ll,l=l
5. lllll,==l,l==,=l=,l=ll,ll=l,lll=,=lll


thus F(n)=F(n-1)+F(n-2)
"""

def tilingProblem(N):
	if N is None:
		return None
	if N==0:
		return 0
	m=[0 for i in range(N+1)]
	m[0],m[1],m[2]=0,1,2
	for i in range(3,N+1):
		m[i]=m[i-1]+m[i-2]
	print(m)
	return m[N]

N=5
print(tilingProblem(N))