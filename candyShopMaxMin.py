"""
candyShopMaxMin

In a candy store there are N different types of candies available  and the prices of all the N different types of candies are provided to you.
You are now provided with an attractive offer.
You can buy a single candy from the store and get atmost K other candies ( all are different types ) for free.
Now you have to answer two questions. Firstly, you have to tell what is the minimum amount of money you have to spend to buy all the N different candies. Secondly, you have to tell what is the maximum amount of money you have to spend to buy all the N different candies.
In both the cases you must utilize the offer i.e. you buy one candy and get K other candies for free.
 

Input  
The first line of the input contains T the number of test cases. Each test case consists of two lines. The first line of each test case contains the values of N and K as described above.  Then in the next line N integers follow denoting the price of each of the N different candies.

n,k=42,29
candy="35 1 70 25 79 59 63 65 6 46 82 28 62 92 96 43 28 37 92 5 3 54 93 83 22 17 19 96 48 27 72 39 70 13 68 100 36 95 4 12 23 34"
mini,maxi=candyShopMaxMin(candy,n,k)
print(mini," ",maxi)
"""
import math
if __name__=='__main__':
	t=int(input())
	for i in range(t):
		nk=list(map(int,input().rstrip().split()))
		n,k=nk[0],nk[1]
		candy=sorted(list(map(int,input().rstrip().split())))
		print(candy)
		val=math.ceil(n/(k+1))
		mini,maxi=sum(candy[:val]),sum(candy[:-val-1:-1])
		print(mini," ",maxi)

