"""
golombSeq
Golomb Sequence is a non-decreasing integer sequence where n-th term is equal to the number of times n appears in the sequence

https://www.geeksforgeeks.org/golomb-sequence/

Input:5
Output:1,2,2,3,3

Input:10
Output:1,2,2,3,3,4,4,4,5,5
"""
def golombSeqRec(N):
	if N==1:
		return 1
	return 1+golombSeqRec(N-golombSeqRec(golombSeqRec(N-1)))
def golombSeqDP(N):
	dp=[0]*(N+1)
	dp[1]=1
	print(dp[1],end=",")
	for i in range(2,N+1):
		dp[i]=1+dp[i-dp[dp[i-1]]]
		print(dp[i],end=",")
	print()
	print(dp)
	

n=[5,10,15,7,9]
for N in n:
	print(N,end=":")
	golombSeqDP(N)
	for i in range(1,N+1):
		print(golombSeqRec(i),end=" ")
	print()