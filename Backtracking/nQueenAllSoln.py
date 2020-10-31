"""
nQueenAllSoln
"""
count=0
def nQueenAllSoln(N):
	if N is None:
		return
	solutions=[]
	curr=1
	nQueen(N,solutions,curr)

def isSafe(solutions,x,y):
	n=len(solutions)
	for i in range(n):
		if i==x or solutions[i]==y or abs(i-x)==abs(solutions[i]-y):
			return False
	return True

def nQueen(N,solutions,curr): 
	global count
	if curr>N:
		count+=1
		print(solutions,end="")
		return
	for i in range(N):
		if isSafe(solutions,curr-1,i):
			solutions.append(i)
			nQueen(N,solutions,curr+1)
			solutions.pop()

for N in range(9):
	count=0
	nQueenAllSoln(N)
	print("\n",N,":",count,"\n")