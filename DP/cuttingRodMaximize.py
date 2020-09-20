"""
cuttingRodMaximize
Cut the rod in the pieces given to maximize the profit
R=5
P=[1,2,3,4]
V=[2,5,7,8]
"""
def cuttingRodMaximize(R,P,V):
	if R is None or P is None or V is None:
		return None
	n=len(P)
	m=[[0 for i in range(R+1)] for j in range(n+1)]
	for i in range(1,n+1):
		for j in range(1,R+1):
			if P[i-1]<=j:
				m[i][j]=max(m[i-1][j],m[i][j-P[i-1]]+V[i-1])
			else:
				m[i][j]=m[i-1][j]
	for i in range(n+1):
		print(m[i])
	return m[n][R]


R=5
P=[1,2,3,4]
V=[2,5,7,8]
print(cuttingRodMaximize(R,P,V))

R=5
P=[5,2,1]
V=[1,1,1,1]
print(cuttingRodMaximize(R,P,V))