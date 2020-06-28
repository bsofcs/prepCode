def bubbleSort(arr):
 n = len(arr)
 for i in range(n):
  swap=False
  for j in range(0,n-i-1):
   print(i,j,arr)
   if arr[j]>arr[j+1]:
    arr[j],arr[j+1]=arr[j+1],arr[j]
    swap=True
  if swap==False:
   break
 return arr

arr=[2,3,7,1,4,0,-1]
print(bubbleSort(arr))