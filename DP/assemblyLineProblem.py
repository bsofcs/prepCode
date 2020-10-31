"""
assemblyLineProblem
https://www.geeksforgeeks.org/assembly-line-scheduling-dp-34/
Inputs given: 
a : 2D list of length "n" with cost at each station in each assembly line
t : 2D list of length "n" with cost to move from one assembly line's i'th station to other assembly line's (i+1)'th station
e : list of length 2 having the cost to enter the assembly lines
x : list of length 2 having the cost to exit the assembly lines
"""
def assemblyLineProblem(a,t,e,x):
	if None in (a,t,e,x):
		return None
	n=len(a[0])
	Work=[[0 for _ in range(n)] for _ in range(2)]
	Path=[[0 for _ in range(n)] for _ in range(2)]
	#entry to the two assembly lines
	Path[0][0],Path[1][0]=0,1
	Work[0][0],Work[1][0]=e[0]+a[0][0],e[1]+a[1][0]
	for i in range(1,n):
		#for assembly line 1
		Work[0][i]=min((Work[1][i-1]+t[1][i]+a[0][i]),(Work[0][i-1]+a[0][i]))
		Path[0][i]=1 if (Work[1][i-1]+t[1][i]+a[0][i])<(Work[0][i-1]+a[0][i]) else 0
		#for assembly line 2
		Work[1][i]=min((Work[0][i-1]+t[0][i]+a[1][i]),Work[1][i-1]+a[1][i])
		Path[1][i]=0 if (Work[0][i-1]+t[0][i]+a[1][i])<(Work[1][i-1]+a[1][i]) else 1
	Work[0][n-1]+=x[0]
	Work[1][n-1]+=x[1]
	print("Work\tPath")
	for i in range(2):
		print(Work[i],Path[i])
	return min(Work[0][n-1],Work[1][n-1])
		

a=[[4,5,3,2],[2,10,1,4]]
t=[[0,7,4,5],[0,9,2,8]]
e=[10,12]
x=[18,7]
print(assemblyLineProblem(a,t,e,x))