"""
coinArrangement

There are N piles of coins each containing  Ai (1<=i<=N) coins.  Now, you have to adjust the number of coins in each pile such that for any two pile,
 if a be the number of coins in first pile and b is the number of coins in second pile then |a-b|<=K. In order to do that you can remove coins from 
different piles to decrease the number of coins in those piles but you cannot increase the number of coins in a pile by adding more coins. 
Now, given a value of N and K, along with the sizes of the N different piles you have to tell the minimum number of coins to be removed in order to 
satisfy the given condition.

Note: You can also remove a pile by removing all the coins of that pile.

Input 
The first line of the input contains T, the number of test cases. Then T lines follow. Each test case contains two lines. The first line of a test case 
contains N and K. The second line of the test case contains N integers describing the number of coins in the N piles.

Output 
For each test case output a single integer containing the minimum number of coins needed to be removed in a new line.

Constraints              
1<=T<=50
1<=N<=100
1<=Ai<=1000
0<=K<=1000    

Example
Input           
3
4 0
2 2 2 2
6 3
1 2 5 1 1 1
6 3
1 5 1 2 5 1

Output        
0
1
2
"""

def arrangeCoins(coins,n,k):
	if coins is None:
		return None
	minCoins=0
	for i in range(1,n):
		diff=coins[i]-coins[i-1]
		if abs(diff)>k:
			minCoins+=(abs(diff)-k)
			val= -1 if diff>0 else 1
			print(coins[i],i)
			coins[i]+=val*(abs(diff)-k)
			coins[i-1]-=val*(abs(diff)-k)
	for i in range(n-2,-1,-1):
		diff=coins[i]-coins[i+1]
		print(coins[i],coins[i+1],diff,i)
		if abs(diff)>k:
			minCoins+=(abs(diff)-k)
			val= -1 if diff>0 else 1
			print(coins[i],i)
			coins[i]+=val*(abs(diff)-k)
			coins[i+1]-=val*(abs(diff)-k)
	return minCoins
"""
if __name__=='__main__':
	noOfInput=int(input())
	for i in range(noOfInput):
		cred=input()
		n=int(cred.split()[0])
		k=int(cred.split()[1])
		c_ip=input()
		coins=[int(i) for i in c_ip.split()]
		result=arrangeCoins(coins,n,k)
		print(result)
"""
n=42
k=468
#2337
c_ip="335 501 170 725 479 359 963 465 706 146 282 828 962 492 996 943 828 437 392 605 903 154 293 383 422 717 719 896 448 727 \
772 539 870 913 668 300 36 895 704 812 323 334"
coins=[int(i) for i in c_ip.split()]
result=arrangeCoins(coins,n,k)
print(result)