def findPivot(arr,low,high):
 pivot=arr[high]
 i=low-1
 for j in range(low,high):
  if arr[j]>=pivot:
   i+=1
   arr[i],arr[j]=arr[j],arr[i]
 arr[high],arr[i+1]=arr[i+1],arr[high]
 return(i+1)

def QuickSort(arr,low,high):
 if low>=high:
  return
 pivot=findPivot(arr,low,high)
 QuickSort(arr,low,pivot-1)
 QuickSort(arr,pivot+1,high)


def maximumPerimeterTriangle(sticks):
 n=len(sticks)
 if n not in range(3,51) or any(x not in range(1,1+(10**9)) for x in sticks):
  return -1
 QuickSort(sticks,0,n-1)
 maxPeri=-1
 result=(-1,-1,-1)
 for j in range(n-2):
  if sticks[j]<(sticks[j+1]+sticks[j+2]) and (sticks[j]+sticks[j+1]+sticks[j+2])>maxPeri:
   maxPeri=(sticks[j]+sticks[j+1]+sticks[j+2])
   result=(sticks[j+2],sticks[j+1],sticks[j])
 return (result if maxPeri!=-1 else maxPeri)


sticks=[1,1,1,2,3,5]
print(maximumPerimeterTriangle(sticks))