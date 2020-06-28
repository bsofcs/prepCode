from os import system, name 
import heapq
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def first_defined(a,b):
 if a is None and b is not None:
  return b
 return a

class heap:
 def __init__(self,typ=1):
  self.hq=[]
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
  self.hq.append(value)
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

 def heapPeep(self):
  if self.size>0:
   return self.hq[0]
  return None

hMax=heap()
hMin=heap(-1)
while(1):
 if hMin.size==0 and hMax.size==0:
  med=None
 elif hMin.size==0 or hMax.size==0:
  med=first_defined(hMin.heapPeep(),hMax.heapPeep())
 elif hMin.size!=hMax.size:
  med=hMin.heapPeep() if hMin.size>hMax.size else hMax.heapPeep()
 else:
  med=(hMin.heapPeep()+hMax.heapPeep())/2
 print("Current Median:",med)
 print("Max Heap")
 hMax.printHeap()
 print("Min Heap")
 hMin.printHeap()
 ip=input("Enter a number (char to escape):")
 if ip.isnumeric():
  ip=int(ip) 
  if hMax.size==0 and hMin.size==0:
   hMax.heapPush(ip)
  elif hMax.size==0 and ip>hMin.heapPeep():
   hMax.heapPush(hMin.heapPop())
   hMin.heapPush(ip)
  elif hMax.size==0 and ip<=hMin.heapPeep():
   hMax.heapPush(ip)
  elif hMin.size==0 and ip<hMax.heapPeep():
   hMin.heapPush(hMax.heapPop())
   hMax.heapPush(ip)
  elif hMin.size==0 and ip>=hMax.heapPeep():
   hMin.heapPush(ip)
  elif hMax.size>hMin.size and ip>hMax.heapPeep():
   hMin.heapPush(ip)
  elif hMax.size>hMin.size and ip<=hMax.heapPeep():
   hMin.heapPush(hMax.heapPop())
   hMax.heapPush(ip)
  elif hMin.size>hMax.size and ip<hMin.heapPeep():
   hMax.heapPush(ip)
  elif hMin.size>hMax.size and ip>=hMin.heapPeep():
   hMax.heapPush(hMin.heapPop())
   hMin.heapPush(ip)
  elif hMin.size==hMax.size and ip>=hMin.heapPeep():
   hMin.heapPush(ip)
  else:
   hMax.heapPush(ip)
 else:
  break
clear()
print(":::::Final Output:::::")
print("Median:",med)  
print("Max Heap")
hMax.printHeap()
print("Min Heap")
hMin.printHeap()
