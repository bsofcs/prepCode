"""
singleAndPairingProblem
Find the number of ways where "n" person can be either paired up (combination) or remain single.
For example: n=3
There are following ways:
{1},{2},{3}
{1,2},{3}
{1},{2,3}
{1,3},{2}

f(n)=ways n people can remain single or in pair
and it can be nth person in following ways:
1. nth person remains single and we calculate the rest i.e. f(n-1)
2. nth person is paired up with any of the n-1 person, so we get (n-1)*f(n-2)
f(n)=f(n-1)+(n-1)*f(n-2)
"""

def singleAndPairingProblem(K):
	if K is None:
		return None
	dp=[0]*(K+1)
	for i in range(K+1):
		if i<=2:
			dp[i]=i
		else:
			dp[i]=dp[i-1]+(i-1)*dp[i-2]
	for i in range(K+1):
		print(i,":",dp[i])
	print(dp[K])

K=15
singleAndPairingProblem(K)