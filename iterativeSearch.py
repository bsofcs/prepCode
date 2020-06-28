def BinarySearch(arr,value):
 len_a=len(arr)
 if len_a==0: return
 low=0
 high=len_a-1
 i=0
 while low<=high:
  i+=1
  mid=(low+high)//2
  print(f"At iteration {i} the search list is {arr[low:high+1]} and the mid is {mid}")
  if arr[mid]>value: high=mid-1
  elif arr[mid]<value: low=mid+1
  else: return mid
 return -1

def interpolationSearch(arr,value):
 len_a=len(arr)
 if len_a==0: return
 low=0
 high=len_a-1
 i=0
 while low<=high and arr[low]<=value and arr[high]>=value:
  i+=1
  print(f"The search list is {arr[low:high+1]} \n")
  if low==high:
   if arr[low]==value:
    return low
   else:
    return -1
  mid=low+int((float(high-low)*(value-arr[low]))/(arr[high]-arr[low]))
  print(f"At iteration {i} the search list is {arr[low:high+1]} and the mid is {mid}\n")
  if arr[mid]==value:
   return mid
  elif arr[mid]<value:
   low=mid+1
  else:
   high=mid-1

arr=[1,10,12,14,23,24,26,35,36,37,47,48,51,54,57,58,59,61,63,65,66,70]
print(len(arr))
value=47
#print("Result of Binary Search:",BinarySearch(arr,value))
print("Result of Interpolation:",interpolationSearch(arr,value))
value=48
#print("Result of Binary Search:",BinarySearch(arr,value))
print("Result of Interpolation:",interpolationSearch(arr,value))
value=70
#print("Result of Binary Search:",BinarySearch(arr,value))
print("Result of Interpolation:",interpolationSearch(arr,value))