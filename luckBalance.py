def findPivot(arr,low,high):
 pivot=arr[high]
 i=low-1
 for j in range(low,high):
  if arr[j]>=pivot:
   i+=1
   arr[i],arr[j]=arr[j],arr[i]
 arr[i+1],arr[high]=arr[high],arr[i+1]
 return(i+1)

def QuickSort(arr,low,high):
 if low>=high:
  return
 pivot=findPivot(arr,low,high)
 QuickSort(arr,low,pivot-1)
 QuickSort(arr,pivot+1,high)

def luckBalance(k, contests):
 n=len(contests)
 if n not in range(1,101) or k not in range(n+1) or any(x[0] not in range(1,1+(10**4)) or x[1] not in range(2) for x in contests):
  return
 one=[contests[i][0] for i in range(n) if contests[i][1]==1]
 zero=[contests[i][0] for i in range(n) if contests[i][1]==0]
 QuickSort(one,0,len(one)-1)
 return(sum(one[0:k])-sum(one[k:])+sum(zero))
 

contests=[[5,1],[2,1],[1,1],[8,1],[10,0],[5,0]]
k=3
print(luckBalance(k, contests))