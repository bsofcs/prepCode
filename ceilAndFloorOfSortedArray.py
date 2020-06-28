def ceilAndFloorOfSortedArray(arr,low,high,val):
 floor=None
 ceil=None
 if arr is None or low>high or val is None:
  return
 if arr[low]>val:
  ceil=arr[low]
 elif arr[high]<val:
  floor=arr[high]
 elif arr[high]==val and arr[low]==val:
  floor=val
  high=val
 else:
  mid=low+(high-low)//2
  if arr[mid]<=val and arr[mid+1]>=val:
   floor=arr[mid]
   ceil=arr[mid+1]
  elif arr[mid]<val and arr[mid+1]<val:
   return ceilAndFloorOfSortedArray(arr,mid+2,high,val)
  else:
   return ceilAndFloorOfSortedArray(arr,low,mid-1,val)
 return floor,ceil


arr=[2,3,5,6,7,9,10,23,210]
while(1):
 print(arr)
 ip=input("Enter the val=>")
 if not ip.isnumeric():
  break
 val=int(ip)
 low=0
 high=len(arr)-1
 print(ceilAndFloorOfSortedArray(arr,low,high,val))