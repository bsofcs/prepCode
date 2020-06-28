"""
occurenceOfRepeat
two functions
i/p: sorted array with duplicates
firstOccurence: gives the first occurence of the repeating element
lastOccurence: give the last occurence of the repeating element
"""

def firstOccurence(arr,val,low,high,n):
 if high>=low:
  mid=low+(high-low)//2
  if (mid==0 or val>arr[mid-1]) and arr[mid]==val:
   return mid
  elif val>arr[mid]:
   return firstOccurence(arr,val,mid+1,high,n)
  else:
   return firstOccurence(arr,val,low,mid-1,n)
 return -1
def lastOccurence(arr,val,low,high,n):
 if high>=low:
  mid=low+(high-low)//2
  if (mid==n-1 or val<arr[mid+1]) and arr[mid]==val:
   return mid
  elif val<arr[mid]:
   return lastOccurence(arr,val,low,mid-1,n)
  else:
   return lastOccurence(arr,val,mid+1,high,n)
 return -1

def firstOccIterative(arr,val):
 n=len(arr)
 if n==0:
  return
 low,high=0,n-1
 result=-1
 while high>=low:
  mid=low+(high-low)//2
  if arr[mid]==val:
   result=mid
   high=mid-1
  elif arr[mid]<val:
   low=mid+1
  else:
   high=mid-1
 return result

def lastOccIterative(arr,val):
 n=len(arr)
 if n==0:
  return
 low,high=0,n-1
 result=-1
 while high>=low:
  mid=low+(high-low)//2
  if arr[mid]==val:
   result=mid
   low=mid+1
  elif arr[mid]<val:
   low=mid+1
  else:
   high=mid-1
 return result

def findFrequencyUsingOCC(arr,val):
 if arr is None:
  return
 l=lastOccIterative(arr,val)
 f=firstOccIterative(arr,val)
 print(l,f)
 result= (l-f+1) if(l!=-1 and f!=-1) else 0
 return result

def findFrequencyUsingBinary(arr,val,low,high):
 n=len(arr)
 if n==0:
  return 0
 if low==high:
  if arr[low]==val:
   return 1
  else:
   return 0
 count=0
 if high>=low:
  mid=low+(high-low)//2
  if arr[mid]==val:
   left=findFrequencyUsingBinary(arr,val,low,mid-1)
   right=findFrequencyUsingBinary(arr,val,mid+1,high)
   return(left+right+1)
  elif arr[mid]<val:
   return findFrequencyUsingBinary(arr,val,mid+1,high)
  else:
   return findFrequencyUsingBinary(arr,val,low,mid-1)
 return 0

arr=[1,2,3,4,5,6,7,8,8,8,8,9,10]
n=len(arr)
high=n-1
low=0
while(1):
 print(arr)
 val=input("Enter a num to search (char to exit)=>")
 if val.isnumeric():
  val=int(val)
  print("Recursive:\nFirst:",firstOccurence(arr,val,low,high,n),"\tLast:",lastOccurence(arr,val,low,high,n))
  print("Iterative:\nFirst:",firstOccIterative(arr,val),"\tLast:",lastOccIterative(arr,val))
  print(val,low,high)
  print("Frequency:\nOccurence:",findFrequencyUsingOCC(arr,val),"\tBinaryCount:",findFrequencyUsingBinary(arr,val,low,high))
  continue
 else:
  break