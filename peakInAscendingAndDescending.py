def peakInAscendingAndDescending(arr,low,high):
 if low>high:
  return
 if low==high:
  return low
 mid=low+int((high-low)/2)
 if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
  return mid
 if arr[mid]<arr[mid-1] and arr[mid]>arr[mid+1]:
  return peakInAscendingAndDescending(arr,low,mid-1)
 return peakInAscendingAndDescending(arr,mid+1,high)

arr=[45,47,57,68,90,100,65,43,32,12,10]
low,high=0,len(arr)-1
print(arr)
print(arr[peakInAscendingAndDescending(arr,low,high)])
arr=[i for i in range(100)]
low,high=0,len(arr)-1
print(arr)
print(arr[peakInAscendingAndDescending(arr,low,high)])
arr=[i for i in range(99,0,-1)]
arr[0]=100
low,high=0,len(arr)-1
print(arr)
print(arr[peakInAscendingAndDescending(arr,low,high)])