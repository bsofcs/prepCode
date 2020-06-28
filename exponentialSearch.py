def binarySearch(arr,value,low=0,high=-1):
 if arr is None:
  return -1
 if high==-1:
  high=len(arr)-1
 if high==low:
  if arr[low]==value:
   return low
  else:
   return -1
 mid=low+((high-low)//2)
 if arr[mid]<value: return binarySearch(arr,value,mid+1,high)
 elif arr[mid]>value: return binarySearch(arr,value,low,mid-1)
 else: return mid

def eponentialSearch(arr,value):
 if arr is None:
  return -1
 high=len(arr)
 if arr[0]==value:
  return 0
 i=1
 while i<high and arr[i]<=value:
  i=i*2
 return(binarySearch(arr,value,int(i/2),min(i,high)))

arr=[i for i in range(1,13)]
value=9
print(arr,value)
print(eponentialSearch(arr,value))