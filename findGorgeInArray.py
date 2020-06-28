def findGorgeInArray(arr):
 n=len(arr)
 low,mid,high=0,0,n-1
 while arr[low]>=arr[high]:
  if high-low<=1:
   return arr[high+1]
  mid=low+(high-low)//2
  if arr[mid]>arr[low] and arr[mid+1]>arr[low]:
   low=mid+1
  if arr[mid]<arr[low] and arr[mid+1]<arr[low]:
   high=mid-1
  if arr[mid]>arr[low] and arr[mid+1]<arr[low]:
   return arr[mid+1]


arr=[5,6,7,8,9,2,3,4]
print(findGorgeInArray(arr))