"""
allPossibleSubset
"""
a=[1,4,2,5]
n=len(a)
allPoss=[[]]
for i in range(2**n):
	tmp=[]
	a_i=(list(bin(i))[2:])[::-1]
	for j in range(len(a_i)):
		if a_i[j]=="1":
			tmp.append(a[n-1-j])
	if len(tmp):
		allPoss.append(tmp[::-1])
print(sorted(allPoss))
print(len(allPoss))
	