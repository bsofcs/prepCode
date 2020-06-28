def partition(arr,low,high,pivot):
 i=low
 for j in range(low,high):
  if arr[j]<pivot:
   arr[i],arr[j]=arr[j],arr[i]
   i+=1
  if arr[j]==pivot:
   arr[j],arr[high]=arr[high],arr[j]
   j-=1
 arr[i],arr[high]=arr[high],arr[i]
 return i

def matchNutsAndBolts(nuts,bolts,low,high):
 if low<high:
  pivot=partition(nuts,low,high,bolts[high])
  partition(bolts,low,high,nuts[pivot])
  matchNutsAndBolts(nuts,bolts,low,pivot-1)
  matchNutsAndBolts(nuts,bolts,pivot+1,high)

nuts = [1,2,3,4,5,6]
bolts = [3,4,6,5,1,2] 
print(nuts,bolts)
matchNutsAndBolts(nuts,bolts,0,5)
print(nuts,bolts)