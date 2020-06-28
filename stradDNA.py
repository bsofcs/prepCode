def count_occ(arr,pattern):
 if arr==None or pattern==None:
  return
 if len(pattern)==1:
  return(arr.count(pattern))
 start=0
 flag=0
 count=0
 last=len(arr)
 while start<last-1:
  flag=arr.find(pattern,start)
  if flag!=-1:
   count+=1
   start=flag+1
  else:
   return(count)

def healthStrad(genes,health,first,last,d):
 tot_health=0
 for i in range(first,last+1):
  occ=count_occ(d,genes[i])
  tot_health+=occ*health[i]
 return tot_health

def get_fun():
# n = int(input())
# genes = input().rstrip().split()
# health = list(map(int, input().rstrip().split()))
# s = int(input())
 n=6
 genes=["a","b","c","aa","d","b"]
 health=[i for i in range(1,7)]
 s=[[1,5,"caaab"],[0,4,"xyz"],[2,4,"bcdybc"]]
 if n not in range(1,10**5+1) or any(map(lambda x: x not in range(1,10**7+1),health)):
  return
 health_strad=[0]*len(s)
 i=0
 for s_itr in s:
  firstLastd = s_itr
  first = int(firstLastd[0])
  last = int(firstLastd[1])
  d = firstLastd[2]
  if first>last or first<0 or last>n:
   return
  health_strad[i]=healthStrad(genes,health,first,last,d)
  if health_strad[i] not in range(1,(2*10**6)+1):
   print("Return here")
   return
  i+=1
 print(min(health_strad)," ",max(health_strad))


if __name__ == '__main__':
    get_fun()