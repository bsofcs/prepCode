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
 if arr is None or low>=high:
  return
 pivot=Partition(arr,low,high)
 QuickSort(arr,low,pivot-1)
 QuickSort(arr,pivot+1,high)

def findNumWithExactDiff(arr,val):
 low=0;high=len(arr)-1
 QuickSort(arr,low,high) 
 i=0;j=1;size=len(arr)
 while i<size and j<size:
  if i!=j and arr[j]-arr[i]==val:
   print("Pairs:",arr[i],arr[j])
   return
  elif arr[j]-arr[i]<val:
   j+=1
  else:
   i+=1
 print("No pairs")

arr=[5,3,7,23,4,2,7,8] 
print(arr)
val=19
findNumWithExactDiff(arr,val)