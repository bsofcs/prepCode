"""
fittingSelvesProblem
Given the length of the wall w and shelves of length m and n, find the number of each type of shelf be used and the remaining empty space in the optimal solution so that the empty space is minimum. 
The larger of the two shelves is cheaper so it is pererred. However the cost is secondary and first is to minimize the space left.
Input : w = 24 m = 3 n = 5
Output : 3 3 0
We use three units of both shelves
and 0 space is left.
3 * 3 + 3 * 5 = 24
So empty space  = 24 - 24 = 0
Another solution could have been 8 0 0
but since the larger shelf of length 5
is cheaper the former will be the answer.

Input : w = 29 m = 3 n = 9 
Output : 0 3 2
0 * 3 + 3 * 9 = 27
29 - 27 = 2

Input : w = 24 m = 4 n = 7 
Output : 6 0 0
6 * 4 + 0 * 7 = 24
24 - 24 = 0
"""
def fittingSelvesProblem(w,m,n):
	if None in (w,m,n):
		return None
	num_m,num_n,rem=0,0,w
	p,q,r=0,0,0
	while w>=n:
		p=w/m
		r=w%n
		if rem>=r:
			num_m=p
			num_n=q
			rem=r
		q+=1
		w-=n
	return int(num_m),num_n,rem
		

w=24;m=3;n=5
print(fittingSelvesProblem(w,m,n))