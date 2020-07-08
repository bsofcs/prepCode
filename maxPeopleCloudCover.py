"""
maxPeopleCloudCover
n: number of towns in the city
p: n separated values indicating population of i'th town
x: n separated values indicating the location of i'th town
m: number of cloud cover
y: m separated values indicating the location of i'th cloud
r: m separated values indicating the range of i'th cloud

def findIndexInTown(x,minIndex,maxIndex):
def maximumPeople(p, x, y, r):
"""
def findIndexInTown(x,minIndex,maxIndex):
 n=len(x)
 result=[]
 for i in range(n):
  if x[i] in range(minIndex,maxIndex+1):
   result.append(i)
 #print(x,minIndex,maxIndex,result)
 return result

def maximumPeople(p, x, y, r):
 n=len(p)
 m=len(y)
 if p is None or x is None or y is None or r is None or\
 n not in range(1,(2*10**5)+1) or m not in range(1,1+(10**5)) or \
 any(i not in range(1,1+(10**9)) for i in x) or any(i not in range(1,1+(10**9)) for i in y) or \
 any(i not in range(1,1+(10**9)) for i in r) or any(i not in range(1,1+(10**9)) for i in p):
  return None
 totPopUnderCover=[0]*m
 maxPopUnderCover=0
 totPop=0
 cloud=-1
 sunPop={}
 for i in range(m):
  indx=findIndexInTown(x,y[i]-r[i],y[i]+r[i])
  tmp=0
  for j in indx:
   totPop+=p[j]
   tmp+=p[j]
   if j in sunPop:
    sunPop[j]+=1
   else:
    sunPop[j]=1
  totPopUnderCover[i]=tmp
  if tmp>maxPopUnderCover:
   maxPopUnderCover=tmp
   cloud=i
 if totPop==0:
  return(sum(p))
 else:
  indx=findIndexInTown(x,(y[cloud]-r[cloud]),(y[cloud]+r[cloud]))
  #print("Cloud:",cloud,sunPop,indx,y[cloud],y)
  for i in indx:
   if i in sunPop: 
     sunPop[i]-=1
  #print(sunPop)
  totSun=0
  for i in range(n):
   if i not in sunPop or (i in sunPop and sunPop[i]==0):
    totSun+=p[i]
 print(totSun)
 return totSun

p=[10,1,8,3]
x=[4,5,7,2]
y=[3,9,3,5]
r=[11,10,8,7]
print(maximumPeople(p, x, y, r))


p=[10,100]
x=[5,100]
y=[4]
r=[1]
print(maximumPeople(p, x, y, r))