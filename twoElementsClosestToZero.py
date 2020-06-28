import sys
def twoElementsClosestToZero(arr):
 n=len(arr)
 arr.sort()
 if n<2:
  return
 l=0
 r=n-1
 minLeft=1
 minRight=(n-1)
 minSum=float("INF")
 while l<r:
  sum=arr[l]+arr[r]
  if abs(minSum)>abs(sum):
   minSum=sum
   minLeft=l
   minRight=r
  if sum<0:
   l+=1
  else: r-=1
 print(arr[minLeft],arr[minRight])


arr=[1,60,-10,70,-80,85]
twoElementsClosestToZero(arr)
arr=[108,3,5,-9,-7,6]
twoElementsClosestToZero(arr)