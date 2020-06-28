def findPivot(arr,low,high):
 if low==high:
  return low
 mid=low+(high-low)//2
 if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
  return mid
 if arr[mid]>arr[mid-1] and arr[mid]<arr[mid+1]:
  return findPivot(arr,mid+1,high)
 return findPivot(arr,low,mid-1)

def interpolationAscSearch(arr,low,high,target):
 if low<=high and target>=arr[low] and target<=arr[high]:
  mid=low+(target-arr[low])*int((high-low)/(arr[high]-arr[low]))
  if arr[mid]>target:
   return interpolationAscSearch(arr,low,mid-1,target)
  elif arr[mid]<target:
   return interpolationAscSearch(arr,mid+1,high,target)
  else:
   return mid
 else:
  return -1

def interpolationDscSearch(arr,low,high,target):
 if low<=high and target<=arr[low] and target>=arr[high]:
  mid=low+(target-arr[high])*int((high-low)/(arr[low]-arr[high]))
  if arr[mid]>target:
   return interpolationDscSearch(arr,mid+1,high,target)
  elif arr[mid]<target:
   return interpolationDscSearch(arr,low,mid-1,target)
  else:
   return mid
 else:
  return -1

def isBitonic(arr):
 n=len(arr)
 if n==0:
  return False
 for i in range(1,n):
  if arr[i]<arr[i-1]:
   break
 if i==n:
  return True
 for j in range(i,n):
  if arr[i]>arr[i-1]:
   break
 if j==n:
  return True
 return False

def BitonicSearch(arr,value):
 if not isBitonic:
  print("Not Bitonic")
  return -1
 low,high=0,len(arr)-1
 pivot=findPivot(arr,low,high)
 if arr[pivot]==value:
  return pivot
 result=interpolationAscSearch(arr,low,pivot-1,value)
 if result!=-1:
  return result
 return(interpolationDscSearch(arr,pivot+1,high,value))

def SortRotatedSearch(arr,low,high,target):
 if low>high:
  return -1
 mid=(low+high)//2
 if arr[mid]==target:
  return mid
 if arr[low]<arr[mid]:
  if arr[low]<=target<arr[mid]:
   return SortRotatedSearch(arr,low,mid-1,target)
  return SortRotatedSearch(arr,mid+1,high,target)
 elif arr[low]>arr[mid]:
  if arr[mid]<target<=arr[high]:
   return SortRotatedSearch(arr,mid+1,high,target)
  return SortRotatedSearch(arr,low,mid-1,target)
 else:
  if arr[mid]!=arr[high]:
   return SortRotatedSearch(arr,mid+1,high,target)
  result=SortRotatedSearch(arr,low,mid-1,target)
  if result!=-1:
   return result
  return SortRotatedSearch(arr,mid+1,high,target)

arr=[10,21,32,44,52,66,78,82,97,2,3,4,5,8]
low,high=0,len(arr)-1
target=5
print(arr,target)
print(SortRotatedSearch(arr,low,high,target))
arr=[1,2,12,42,53,64,74,86,97,67,52,45,34,23,12,1]
target=52
print(arr,target)
print(BitonicSearch(arr,target))
arr=[1,2,12,42,53,64,74,86,97]
target=53
print(arr,target)
print(BitonicSearch(arr,target))
