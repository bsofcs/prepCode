"""
bruijnSeq
Given an interger "n", print the first "n" terms of the Moser-de Bruijn Sequence.
The Moser-de Bruijn Sequence is the sequence obtained by adding up the distinct power of the number 4 (ex: 1,4,16,64,etc)
Input: 5
Output: 0,1,4,5,16
Input: 10
Output: 0,1,4,5,16,17,20,21,64,65
"""
def bruijnSeq(N):
	if N is None:
		return
	dp=[0]*(N+1)
	dp[1]=1
	for i in range(2,N+1):
		if i%2==0:
			dp[i]=dp[i//2]*4
		else:
			dp[i]=dp[i//2]*4+1
	return dp[:N]
n=[5,10]
for N in n:
	print(N,":",bruijnSeq(N))