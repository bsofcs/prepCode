"""
findKMaxMin.py
"""
import heapq
class heap:
 def __init__(self,typ=1):
  tmp=float("-INF") if typ==1 else float("INF")
  self.hq=[tmp]*500
  self.maxsize=500
  self.size=0
  self.typ=typ
  #1 for maxheap and -1 for minheap

 def printHeap(self):
  print(self.hq[0:self.size])
 
 def heapify(self):
  if self.typ==1:
   self.heapifyMax()
  else:
   self.heapifyMin()

 def heapifyMax(self):
  parent=(self.size-2)//2
  while(parent>=0):
   childLeft=parent*2+1
   childRight=parent*2+2 if parent*2+2<=self.size-1 else childLeft
   #print("Size,Parent,ChildLeft,ChildRight and Heap:",self.size,parent,childLeft,childRight,self.hq[0:self.size])
   if self.hq[parent]>self.hq[childLeft] and self.hq[parent]>self.hq[childRight]:
    #print("No change")
    parent-=1
   else:
    #print("Change")
    tochg=childLeft if self.hq[childLeft]>self.hq[childRight] else childRight
    self.hq[parent],self.hq[tochg]=self.hq[tochg],self.hq[parent]
    parent-=1

 def heapifyMin(self):
  parent=(self.size-2)//2
  while(parent>=0):
   childLeft=parent*2+1
   childRight=parent*2+2 if parent*2+2<=self.size-1 else childLeft
   #print("Size,Parent,ChildLeft,ChildRight and Heap:",self.size,parent,childLeft,childRight,self.hq[0:self.size])
   if self.hq[parent]<self.hq[childLeft] and self.hq[parent]<self.hq[childRight]:
    #print("No change")
    parent-=1
   else:
    #print("Change")
    tochg=childLeft if self.hq[childLeft]<self.hq[childRight] else childRight
    self.hq[parent],self.hq[tochg]=self.hq[tochg],self.hq[parent]
    parent-=1

 def heapPush(self,value):
  if self.maxsize==self.size+10:
   temp=[0]*500
   self.hq.extend(temp)
   self.size+=500
  self.hq[self.size]=value
  self.size+=1
  self.heapify()

 def heapPop(self):
  if self.size>0:
   temp=self.hq[0]
   self.hq[self.size-1],self.hq[0]=self.hq[0],self.hq[self.size-1]
   self.hq.pop(self.size-1)
   self.size-=1
   self.heapify()
  else:
   print("Heap Empty")
  return temp

def findMaxMinTournamentStyle(arr,low,high):
 if arr is None or low>high:
  return
 if high==low:
  min_arr=arr[low]
  max_arr=arr[low]
  return(max_arr,min_arr)
 elif high==(low+1):
  if arr[high]>arr[low]:
   return(arr[high],arr[low])
  else:
   return(arr[low],arr[high])
 else:
  mid=low+(high-low)//2
  max1,min1=findMaxMinTournamentStyle(arr,low,mid)
  max2,min2=findMaxMinTournamentStyle(arr,mid+1,high)
  return(max(max1,max2),min(min1,min2))

def kthMaxMin(arr,k):
 if arr is None:
  return
 hl=[]
 hs=[]
 for i in arr:
  heapq.heappush(hl,(-i,i))
  heapq.heappush(hs,(i,i))
 for i in range(k):
  w,mx=heapq.heappop(hl)
  m,mi=heapq.heappop(hs)
  if i==k-1:
   break
 return(mx,mi)

def CreatePartitionSmall(arr,low,high):
 pivot=arr[high]
 i=low
 for j in range(low,high):
  if arr[j]<pivot:
   arr[j],arr[i]=arr[i],arr[j]
   i+=1
 arr[i],arr[high]=arr[high],arr[i]
 return(i)

def CreatePartitionLarge(arr,low,high):
 pivot=arr[high]
 i=low
 for j in range(low,high):
  if arr[j]>pivot:
   arr[i],arr[j]=arr[j],arr[i]
   print(arr,i,j)
   i+=1
 arr[high],arr[i]=arr[i],arr[high]
 return(i)

def kthMaxUsingPartition(arr,low,high,k):
 if k<low or k>high+1 or low>high or arr is None:
  print("Return -1:",low,high,k)
  return -1
 if low<high:
  pivot=CreatePartitionLarge(arr,low,high)
  print(pivot,arr[pivot])
  if pivot==k-1:
   print(pivot," is returned")
   return pivot
  elif pivot>k-1:
   return kthMaxUsingPartition(arr,low,pivot-1,k)
  else:
   return kthMaxUsingPartition(arr,pivot+1,high,k)
 

def kthMinUsingPartition(arr,low,high,k):
 if k<low or k>high+1 or low>high or arr is None:
  return -1
 if low<high:
  pivot=CreatePartitionSmall(arr,low,high)
  if pivot==k-1:
   return pivot
  elif pivot>k-1:
   return kthMinUsingPartition(arr,low,pivot-1,k)
  else:
   return kthMinUsingPartition(arr,pivot+1,high,k)

arr1=[23,12,43,3,6,7,213,342,56,68,23,-3,-54,-542,2342]
print(arr1)
arr1.sort()
print(arr1)
arr=[23,12,43,3,6,7,213,342,56,68,23,-3,-54,-542,2342]
print("\nUsing Tournament")
print("(Max and Min):",findMaxMinTournamentStyle(arr,0,len(arr)-1))
k=5;n=len(arr)
print("\nUsing Heap Library")
print(f"kth:{k}th\t(Max and Min):{kthMaxMin(arr,k)}")
print("\nUsing Heap Code")
s=heap(-1)
h=heap(1)
for i in arr:
 s.heapPush(i)
 h.heapPush(i)
for i in range(k):
 mx,mi=h.heapPop(),s.heapPop() 
print(f"kth:{k}th\t(Max and Min):{mx,mi}")
print("\nUsing Quick Sort:")
arr=[23,12,43,3,6,7,213,342,56,68,23,-3,-54,-542,2342]
k,high,low=5,len(arr)-1,0
mi=kthMaxUsingPartition(arr,low,high,k)
print(arr,mi)
print(f"kth:{k}th\tMax:{arr[mi]}")
arr=[23,12,43,3,6,7,213,342,56,68,23,-3,-54,-542,2342]
k,high,low=5,len(arr)-1,0
mi=kthMinUsingPartition(arr,low,high,k)
print(arr,mi)
print(f"kth:{k}th\tMin:{arr[mi]}")