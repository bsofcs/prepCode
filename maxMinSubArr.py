def findPivot(arr,low,high):
 pivot=arr[high]
 i=low-1
 for j in range(low,high):
  if arr[j]<=pivot:
   i+=1
   arr[i],arr[j]=arr[j],arr[i]
 arr[i+1],arr[high]=arr[high],arr[i+1]
 return(i+1)

def QuickSort(arr,low,high):
 if low>=high:
  return
 mid=findPivot(arr,low,high)
 QuickSort(arr,low,mid-1)
 QuickSort(arr,mid+1,high)

def maxMin(k, arr):
 n=len(arr)
 if n not in range(2,1+(10**5)) or k not in range(2,n+1) or any(x not in range(0,1+(10**9)) for x in arr):
  print("Here")
  return
 QuickSort(arr,0,n-1)
 diff=arr[n-1]-arr[0]
 for i in range(n-k+1):
  t_diff=arr[i+k-1]-arr[i]
  if t_diff<diff:
   diff=t_diff
 return diff

k=3
arr=[1]*123
print(maxMin(k, arr))