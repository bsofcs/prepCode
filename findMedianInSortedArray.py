#findMedianInSortedArray.py
def findMedianLinear(ar1,ar2):
 if ar1 is None or ar2 is None:
  return
 i=j=0
 n1,n2=len(ar1),len(ar2)
 result=[]
 while i<n1 and j<n2:
  if ar1[i]<ar2[j]:
   result.append(ar1[i])
   i+=1
  else:
   result.append(ar2[j])
   j+=1
 while i<n1:
  result.append(ar1[i])
  i+=1
 while j<n2:
  result.append(ar2[j])
  j+=1
 if (n1+n2)%2==0:
  median=(result[int((n1+n2)/2)]+result[int((n1+n2)/2)-1])/2
 else:
  median=result[(n1+n2)//2]
 return int(median)


"""
here we create a partition in X(smaller array) aka partX and in Y(larger array) aka partY
such that left to partX is less the right to partY and vice versa
in case X+Y is even the max of the left half's element of both array is median
in case X+Y is odd we take the avg of the max of the left half with the min of right half
""" 
def findMediamLog(ar1,ar2):
 high1,high2=len(ar1),len(ar2)
 if high1>high2:
  return findMediamLog(ar2,ar1)
 low,high=0,high1
 while low<=high:
  partX=int((high+low)/2)
  partY=int((high1+high2+1)/2)-partX
  maxLeftX=float("-INF") if partX==0 else ar1[partX-1]
  minRightX=float("INF") if partX==len(ar1) else ar1[partX]
  maxLeftY=float("-INF") if partY==0 else ar2[partY-1]
  minRightY=float("INF") if partY==len(ar2) else ar2[partY]
  #print("maxLeftX:",maxLeftX,"minRightX:",minRightX,"maxLeftY:",maxLeftY,"minRightY:",minRightY)
  if maxLeftX>minRightY:
   high=partX-1
  elif maxLeftY>minRightX:
   low=partX+1
  else:
   break
 if (high1+high2)%2==0:
  median=(max(maxLeftX,maxLeftY)+min(minRightX,minRightY))/2
 else:
  median=max(maxLeftX,maxLeftY)
 return int(median)
 

ar1=[1,12,15,26,38]
ar2=[2,13,17,30,45]
print(findMedianLinear(ar1,ar2))
print(findMediamLog(ar1,ar2))
ar1=[1,12,15,26,80]
ar2=[2,13,17,30,45,56,76]
print(findMedianLinear(ar1,ar2))
print(findMediamLog(ar1,ar2))