"""
knapSack:
1. knapSack01
2. fractionalKnapsack
3. knapSack01Optimized
"""
def knapSack01(knapsackSize,itemValues,itemWeights):
	if knapsackSize is None or itemValues is None or itemWeights is None:
		return None
	n=len(itemValues)
	m=[[0 for i in range(knapsackSize+1)] for j in range(n)]
	for i in range(n):
		for j in range(1,knapsackSize+1):
			if itemWeights[i]>j:
				m[i][j]=m[(i-1)%n][j]
			else:
				m[i][j]=max(itemValues[i]+m[(i-1)%n][j-itemWeights[i]],m[(i-1)%n][j])
	for i in range(n):
		print(itemValues[i],itemWeights[i],m[i])
	res=m[len(itemValues)-1][knapsackSize]
	print(res)
	item=[]
	for i in range(n,0,-1):
		#print(i,end=" ")
		if res<=0:
			#print("Breaks")
			break
		if res==m[i-1][knapsackSize]:
			#print("Continues")
			continue
		else:
			#print("Appends")
			item.append(itemWeights[i])
			res-=itemValues[i]
			knapsackSize-=itemWeights[i]
	print(item)

class Item:
	def __init__(self,value,weight):
		self.value=value
		self.weight=weight
		self.ratio=value/weight

def fractionalKnapsack(knapsackSize,itemValues,itemWeights):
	if knapsackSize is None or itemValues is None or itemWeights is None:
		return None
	n=len(itemValues)
	bags=[]
	for i in range(n):
		bags.append(Item(itemValues[i],itemWeights[i]))
	bags=sorted(bags, key= lambda x:x.ratio)[::-1]
	i,totVal=0,0;item=[]
	while knapsackSize>0:
		if bags[i].weight>knapsackSize:
			totVal+=knapsackSize*(bags[i].ratio)
			knapsackSize=0
		else:
			totVal+=bags[i].value
			knapsackSize-=bags[i].weight
		item.append(bags[i].weight)
		i+=1
	print(totVal)
	print(item)

def knapSack01Optimized(knapsackSize,itemValues,itemWeights,n):
	if knapsackSize is None or itemValues is None or itemWeights is None or n is None:
		return None
	dp=[0]*(knapsackSize+1)
	for i in range(n):
		for j in range(knapsackSize,itemWeights[i]-1,-1):
			dp[j]=max(dp[j],itemValues[i]+dp[j-itemWeights[i]])
		print(dp)

knapsackSize,itemValues,itemWeights=7,[1,4,5,7],[1,3,4,5]
knapSack01(knapsackSize,itemValues,itemWeights)
fractionalKnapsack(knapsackSize,itemValues,itemWeights)
knapSack01Optimized(knapsackSize,itemValues,itemWeights,len(itemValues))