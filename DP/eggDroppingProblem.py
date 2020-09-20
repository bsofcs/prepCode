"""
eggDroppingProblem
Suppose you have N eggs and you want to determine from which floor in a K-floor building you can drop an egg such that it doesn't break. You have to determine the minimum number of attempts you need in order find the critical floor in the worst case while using the best strategy.There are few rules given below. 

An egg that survives a fall can be used again.
A broken egg must be discarded.
The effect of a fall is the same for all eggs.
If the egg doesn't break at a certain floor, it will not break at any floor below.
If the eggs breaks at a certain floor, it will break at any floor above.
For more description on this problem see wiki page

Input:
The first line of input is  T denoting the number of testcases.Then each of the T lines contains two positive integer N and K where 'N' is the number of eggs and 'K' is number of floor in building.

Output:
For each test case, print a single line containing one integer the minimum number of attempt you need in order find the critical floor.


Explanation:
~~~~~~~~~~
Let us assume that Input given is "N" floor and "K" eggs.
in any situation on the i'th floor with j'th eggs left, we will have two situation:
	1. if we drop the next egg from this floor, then it breaks and
	2. it doesn't break.
So we have three point to note:
	1. the floor attempt counts so we take 1 for this drop
	2. if this eggs breaks then we are left with all the floor below i'th i.e. in total (i-1) floors with one less egg i.e. (j-1) eggs
	3. if it doesn't breaks then we take all the floors above that floor i.e. in total (N-i) floors with exact number of eggs i.e. j eggs
but here we have a catch that 
	- for point at every floor we take max of both 2 and 3 for every floor below it and 1 to each values.
	- then we find the minimum of all the values calculated in the previous step
We take a lookup 2D matrix with rows(=number of eggs from 1 to K) and columns(=number of floors from 1 to N)
So pseudo code is:
	for i from 0 to K:
		for j from 0 to N:
			if i>j then m[i][j]=m[i-1][j]
			else m[i][j]=1+min(max(T[i-1][k-1],T[i][j-k] for k from 0 to j))
	then return m[N][K]
recursive
def eggDrop(N,K):
	if N is None or K is None:
		return None
	if N in [0,1]:
		return N
	if K==1:
		return N
	mn=float("INF")
	for x in range(1,N+1):
		mn=min(mn,max(eggDrop(N-1,K-1),eggDrop(N-x,K)))
	return mn+1
"""
def eggDroppingDP(N,K):
	if N is None or K is None:
		return None
	if N==0 or K==0:
		return 0
	m=[[0 for i in range(N+1)] for i in range(K+1)]
	for i in range(K+1):
		m[i][1]=1
		m[i][0]=0
	for i in range(N+1):
		m[1][i]=i
	for i in range(2,K+1):
		for j in range(2,N+1):
			mn=float("INF")
			for k in range(1,j+1):
				if i>j:
					mn=m[i-1][j]
				else:
					mn=min(mn,max(m[i-1][k-1],m[i][j-k]))
			m[i][j]=1+mn
	#for i in range(K+1):
	#	print(m[i])
	return m[K][N]
N=36
K=2
print(eggDroppingDP(N,K))
N=6
print(eggDroppingDP(N,K))