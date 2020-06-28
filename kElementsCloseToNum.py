def Partition(arr,low,high):
 pivot=arr[high]
 i=low-1
 for j in range(low,high):
  if arr[j]<=pivot:
   i+=1
   arr[i],arr[j]=arr[j],arr[i]
 arr[i+1],arr[high]=arr[high],arr[i+1]
 return(i+1)

def QuickSort(arr,low,high):
 if low<high:
  pivot=Partition(arr,low,high)
  QuickSort(arr,low,pivot-1)
  QuickSort(arr,pivot+1,high)

def CrossOverPoint(arr,val,low,high):
 if arr[high]<val:
  return high
 if arr[low]>val:
  return low
 if low>high or arr is None:
  return -1
 mid=low+(high-low)//2
 if arr[mid]<=val and arr[mid+1]>val:
  return mid
 if arr[mid]>val:
  return CrossOverPoint(arr,val,low,mid-1)
 else:
  return CrossOverPoint(arr,val,mid+1,high)

def kElementsCloseToNum(arr,val,k):
 low,high=0,len(arr)-1
 QuickSort(arr,low,high)
 print("Sorted Input array:",arr,"\nVal:",val,"\nk:",k)
 pivot=CrossOverPoint(arr,val,low,high)
 i,j=pivot-1,pivot+1
 result=[]
 count=0
 while i>=low and j<=high and count<k:
  if arr[pivot]-arr[i]<arr[j]-arr[pivot]:
   result.append(arr[i])
   i-=1
  else:
   result.append(arr[j])
   j+=1
  count+=1
 while i>=low and count<k:
  result.append(arr[i])
  i-=1
  count+=1
 while j<=high and count<k:
  result.append(arr[j])
  j+=1
  count+=1
 return result

arr=[12,16,22,30,35,39,42,45,58,48,50,53,55,56]
val,k=-100,14
print(kElementsCloseToNum(arr,val,k))