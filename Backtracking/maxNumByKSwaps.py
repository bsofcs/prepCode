"""
maxNumByKSwaps
Given a number "N" and a number "K". We need to do K swaps in the digits of N to find the maixmum number generated.
Example:
Input: N=254 K=1
Output: 524	(swaps 5 and 2)
Input: N=254 K=2
Output: 542	(Swap 5&2 and 4&2)
Input: N=98762 K=4
Output: 98762	(No Swaps needed)
"""
def maxNumByKSwaps(N,K):
	if None in (N,K):
		return
	mx=[N]
	Util(str(N),K,mx)
	print(mx[0])

def Util(N,K,mx):
	if None in (N,K,mx):
		return N
	n=len(N)
	if n==1 or K==0:
		print("n=1 or K=0",n,N)
		return N
	for i in range(n-1):
		for j in range(1,n):
			if N[i]<N[j]:
				N=swap(N,i,j)
				if int(N)>mx[0]:
					mx[0]=int(N)
					return Util(N,K,mx)
				N=swap(N,i,j)

def swap(N,i,j):
	tmp=list(N)
	tmp[i],tmp[j]=tmp[j],tmp[i]
	return "".join(tmp)		
	
N=[254,254,98762,68543,7599,129814999]
K=[1,2,4,1,2,4]
n=len(N)
for i in range(n):
	print("Input:",N[i],K[i])
	maxNumByKSwaps(N[i],K[i])