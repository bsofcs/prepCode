def countRotation(arr,low,high):
 if high<low:
  return
 if high==low:
  return low
 mid=low+int((high-low)/2)
 if mid<high and arr[mid]>arr[mid+1]:
  return mid+1
 if mid>low and arr[mid]<arr[mid-1]:
  return mid
 if arr[mid]<arr[high]:
  return countRotation(arr,low,mid-1)
 return countRotation(arr,mid+1,high)


arr=[5,6,7,8,9,2,3,4]
print(countRotation(arr,0,7))