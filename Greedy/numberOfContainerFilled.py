"""
numberOfContainerFilled
Given a number N and a time X unit, the task is to find the number of containers that are filled completely in X unit if containers are arranged in pyramid fashion as shown below.
Below example is the pyramid arrangement for N = 3, where N denotes the number of levels in the pyramid-shaped arrangement of containers such that level 1 has 1 container, level 2 has 2 containers and up to level N. The liquid is always poured in the topmost container at the 1st level. When the container of one level overflows from both its sides, the containers of the lower levels are filled. The amount of liquid poured in each second is equal to the volume of the container.
For the following example:
		X	X
		 X     X
		  XXXXX

	X	X	X	X
	 X     X	 X     X
	  XXXXX		  XXXXX

X	X	X	X	X	X
 X     X	 X     X	 X     X
  XXXXX		  XXXXX		  XXXXX

After 1 second, the container at level 1 gets fully filled. 
After 2 seconds, the 2 containers at level 2 are half-filled. 
After 3 seconds, the 2 containers at level 2 are fully filled. 
After 4 seconds, out of the 3 containers at level 3, the 2 containers at the ends are quarter-filled and the container at the center is half-filled. 
After 5 seconds, out of the 3 containers at level 3, the 2 containers at the ends are half-filled and the container at the center is fully filled.
"""

def numberOfContainerFilled(n,x):
	#n levels and x seconds
	if n is None or x is None:
		return None
	if n==0 or x==0:
		return 0
	cont=[[0 for _ in range(2*n)] for _ in range(2*n)]
	cont[1][1]=x
	count=0
	for i in range(1,n+1):
		for j in range(1,i+1):
			if cont[i][j]>=1:
				count+=1
			cont[i+1][j]+=(cont[i][j]-1)/2
			cont[i+1][j+1]+=(cont[i][j]-1)/2
	for i in range(2*n):
		print(cont[i],count)
	print(count)

n=4
x=10
numberOfContainerFilled(n,x)