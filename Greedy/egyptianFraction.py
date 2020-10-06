"""
egyptianFraction
Every positive fraction can be represented as sum of unique unit fractions. A fraction is unit fraction if numerator is 1 and denominator is a positive integer, for example 1/3 is a unit fraction. Such a representation is called Egyptian Fraction as it was used by ancient Egyptians.
Egyptian Fraction Representation of 2/3 is 1/2 + 1/6
Egyptian Fraction Representation of 6/14 is 1/3 + 1/11 + 1/231
Egyptian Fraction Representation of 12/13 is 1/2 + 1/3 + 1/12 + 1/156
"""
import math
def egyptianFraction(p,q):
	if p>q and p==1:
		return
	res=[]
	print(p,"/",q,end=" = ")
	tmp=math.ceil(q/p)
	while tmp:
		res.append(tmp)
		#print(p,q,tmp)
		p=tmp*p-q
		if p==0:
			break
		q=tmp*q
		tmp=math.ceil(q/p)
	for i in res:
		print("1/",i,end=" ")
	print()

p=[2,6,12,4]
q=[3,14,13,4]
for i in range(len(p)):
	egyptianFraction(p[i],q[i])
