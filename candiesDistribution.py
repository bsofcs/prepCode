"""
there are following situations that can arise:
i.	arr[i-1]>=arr[i]>arr[i+1]	=> hike = r[i+1]+1
ii.	arr[i-1]<arr[i]<=arr[i+1]	=> hike = r[i-1]+1
iii.	arr[i-1]>=arr[i]<=arr[i+1]	=> hike = 1
iv.	arr[i-1]<arr[i]>arr[i+1]	=> hike = max(r[i-1],r[i+1])+1

But the problem with this type of problem is when the number are decreasing from arr[i-2] i.e.:
arr[i-2]>arr[i-1]>=arr[i]>arr[i+1]

Thus we use the approach of two-traversal where all initial hike is 1 and the steps goes twice i.e 
i.	from left to right comparing every previous element for smaller than current and incrementing the current hike
ii.	from right to left comparing every previous element for smaller than current and incrementing the current hike
Then we take every position hike value to be the greater value of the two array in the corresponding position
"""

def candies(n,arr):
 if n not in range(1,1+(10**5)) or any(x not in range(1,1+(10**5)) for x in arr):
  return
 if n==1:
  return 1 
 left=[1]*n
 right=[1]*n
 for i in range(1,n):
  if arr[i]>arr[i-1]:
   left[i]=left[i-1]+1
 for i in range(n-2,-1,-1):
  if arr[i]>arr[i+1]:
   right[i]=right[i+1]+1
 sumTotal=0
 print(left,right)
 for i in range(n):
  sumTotal+=max(left[i],right[i])
 return sumTotal

def candiesStepWise(n, arr):
 if n not in range(1,1+(10**5)) or any(x not in range(1,1+(10**5)) for x in arr):
  return
 if n==1:
  return 1
 result=[0]*(n+2)
 arr.insert(0,float("INF"))
 arr.append(float("INF"))
 for i in range(1,n+1):
  if arr[i-1]>=arr[i]>arr[i+1]:
   result[i]=result[i+1]+1
 for i in range(1,n+1):
  if arr[i-1]<arr[i]<=arr[i+1]:
   result[i]=result[i-1]+1
 for i in range(1,n+1):
  if arr[i-1]>=arr[i]<=arr[i+1]:
   result[i]=1
 for i in range(1,n+1):
  if arr[i-1]<arr[i]>arr[i+1]:
   result[i]=max(result[i-1],result[i+1])+1

 print(result)
 return(sum(result[1:n+1]))

arr=[2,4,2,6,1,7,8,9,2,1]
n=len(arr)
print(candies(n, arr))