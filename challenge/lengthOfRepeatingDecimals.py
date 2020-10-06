"""
lengthOfRepeatingDecimals
"""
def lengthOfRepeatingDecimals(p,q):
	remainder=p%q
	r=str(p//q)
	r+="."
	res=[]
	while remainder!=0 and remainder not in res:
		res.append(remainder)
		remainder*=10
		r+=str(remainder//q)
		remainder%=q
	if remainder!=0:
		return len(res)-res.index(remainder),r+"..."
	return 0,r
P=[1,1,2,9,7,1,1,22,1,1,1,1]
Q=[9,3,3,11,12,7,81,7,44,43,31,23]
n=len(P)
for i in range(n):
	l,r=lengthOfRepeatingDecimals(P[i],Q[i])
	print(P[i],Q[i],r,l)