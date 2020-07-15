"""
maximumValuesContiguousSubsequence
In an array a small section having maximum sum needs to be found:
for example:
A=[-2,11,-4,13,-5,2]=20 i.e. [11,-4,13]
A=[1,-3,4,-2,-1,6]=7 i.e. [4,-2,-1,6]
Initialize:
	max_so_far = 0
	max_ending_here = 0
Loop for each element of the array
	(a) max_ending_here = max_ending_here + a[i]
	(b) if(max_so_far < max_ending_here)
		max_so_far = max_ending_here
	(c) if(max_ending_here < 0)
		max_ending_here = 0
return max_so_far
"""

def maxSubArraySum(arr):
 sze=len(arr)
 if sze==0:
  return
 max_so_far=float("-INF")
 max_ending_here=0
 strt=0
 end=0
 s=0
 for i in range(sze):
  max_ending_here+=arr[i]
  if max_so_far<max_ending_here:
   max_so_far=max_ending_here
   strt=s
   end=i
  if max_ending_here<0:
   max_ending_here=0
   s=i+1
 return(max_so_far,strt,end)

arr=[100,-4,13,-100,-5,-1,-2,-2,0,-15,-3,-5,-2,70]
max_so_far,strt,end=maxSubArraySum(arr)

print(arr,len(arr),"\n",max_so_far,strt,end,arr[strt:end+1])