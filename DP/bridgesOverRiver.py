"""
bridgesOverRiver
There is long river having "n" cities on the either side. The left side cities are arranged in a sorted manner whereas the cities on the right are not.
We need to construct as many bridges as possible over the river, but with following two conditions:
	1. The bridge should connect from the i'th city on the left side to the respective i'th city on the right side
	2. There can be no bridge constructed over another
for example:
	1 |	|8
	2 |	|4
	3 |	|2
	4 |	|5
	5 |	|6
	6 |	|3
	7 |	|1
	8 |	|7

Here maximum 4 bridges can be made i.e. for cities 4,5,6,7
"""

def buildMaximumBridges(leftCities,rightCities):
	if leftCities is None and rightCities is None or len(leftCities)!=len(rightCities):
		return None
	n=len(leftCities)
	table=[1]*n
	for i in range(n):
		for j in range(i):
			if rightCities[j]<rightCities[i]:
				table[i]=max(table[i],table[j]+1)
	return max(table)

def buildMaximumBridgesLCS(leftCities,rightCities):
	if leftCities is None and rightCities is None or len(leftCities)!=len(rightCities):
		return None
	n=len(leftCities)
	m=[[float("INF") for i in range(n+1)] for j in range(n+1)]
	for i in range(n+1):
		for j in range(n+1):
			if i==0 or j==0:
				m[i][j]=0
			elif leftCities[i-1]==rightCities[j-1]:
				m[i][j]=m[i-1][j-1]+1
			else:
				m[i][j]=max(m[i-1][j],m[i][j-1])
	i=j=n
	s=[]
	while i>0 and j>0:
		if m[i][j]==m[i-1][j-1]+1 and m[i][j]!=max(m[i-1][j],m[i][j-1]):
			s.append(leftCities[i-1])
			i-=1
			j-=1
		elif m[i][j]==m[i-1][j]:
			i-=1
		else:
			j-=1
	print(s[::-1])
	return m[n][n]

leftCities=[1,2,3,4,5,6,7,8]
rightCities=[8,4,2,5,6,3,1,7]
print(buildMaximumBridges(leftCities,rightCities))
print(buildMaximumBridgesLCS(leftCities,rightCities))