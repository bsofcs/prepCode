"""
frogJumpWaysUpTheRod
A frog jumps either 1, 2 or 3 steps to go to top. In how many ways can it reach the top.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains one line of input N denoting the total number of steps.

Output:
For each testcase, in a new line, print the number of ways to reach the top.

This is the case of permutation. Here the hops taken and the position of the hops taken counts.
For example: for N=3, total ways are:
1,1,1
1,2
2,1
3
so answer is 4

N=5
1,1,1,1,1
2,1,1,1
1,2,1,1
1,1,2,1
1,1,1,2
2,2,1
2,1,2
1,2,2
1,1,3
1,3,1
3,1,1
3,2
2,3

so answer is 13
code: frogJumpWays
"""

def frogJumpWays(N):
	if N is None:
		return None
	if N<3:
		return N
	m=[1 for i in range(N+1)]
	m[0]=1
	m[1]=1
	m[2]=2
	for i in range(3,N+1):
		m[i]=m[i-1]+m[i-2]+m[i-3]
	return m[N]
arr=[1,2,3]
N=3
print(frogJumpWays(N))
N=5
print(frogJumpWays(N))	