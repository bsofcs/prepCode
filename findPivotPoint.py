def findPivotPoint(arr,low,high):
 if arr is None or low>high:
  return -1
 if low==high:
  if arr[low]==low:
   return low
  else:
   return -1
 mid=low+(high-low)//2
 if arr[mid]==mid:
  return mid
 mid=findPivotPoint(arr,low,mid-1)
 if mid is None:
  mid=findPivotPoint(arr,mid+1,high)
 else:
  return mid
 result=mid if mid is not None else -1
 return result

arr=[2,0,1,3,5,7,8,6,9,10]
low=3
high=len(arr)-1
print(findPivotPoint(arr,low,high))