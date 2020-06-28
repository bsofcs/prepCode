"""
patternMatchingUnix.py
"""
def prefix_table(pat):
 pattern=list(pat)
 m=len(pattern)
 F=[0]*m
 k=0
 for q in range(1,m):
  while k>0 and pattern[k]!=pattern[q]:
   k=F[k-1]
  if pattern[k]==pattern[q]:
   k+=1
  F[q]=k
 return F

def KMP(arr,pat):
 n=len(arr)
 m=len(pat)
 text=list(arr)
 pattern=list(pat)
 F=prefix_table(pat)
 q=0
 for i in range(n):
  while q>0 and pattern[q]!=text[i]:
   q=F[q-1]
  if pattern[q]==text[i]:
   q+=1
  if q==m:
   return(i-m+1)
 return -1

"""
arr="bhanusaurabh"
pat="anu"
print(KMP(arr,pat))

"""
def patternMatchingUnix(arr,pat):
 if arr is None or pat is None:
  return
 if pat=="*":
  return arr
 lst_p=list(pat)
 lst_a=list(arr)
 low=-1
 high=0
 count_star=lst_p.count("*")
 if count_star==0:
  return(arr if arr==pat else None)
 elif pat=="*":
  return arr
 else:
  i,flag,tmp,last_low=0,False,0,0
  pos=[-1]
  pos.extend([i for i in range(len(lst_p)) if lst_p[i]=="*"])
  if pos[-1]!=(len(lst_p)-1):
   pos.append(len(lst_p))
   flag=True
  while i<len(pos)-1:
   if pos[i]==0:
    low=0  
   pat1="".join(lst_p[pos[i]+1:pos[i+1]])
   if len(pat1)==0:
    i+=1
    continue
   tmp=KMP("".join(lst_a[high:]),pat1)
   if tmp==-1:
    return None
   if low==-1:
    low=tmp
   high+=tmp+len(pat1)
   last_low+=tmp
   tmp+=len(pat1)
   i+=1
  if flag==False:
   high=len(arr)
  return arr[low:high]

pat="is*is"
arr="A thread is an entity within a process that can be scheduled for execution. Also, it is the smallest unit of processing that can be performed in an OS (Operating System)"
print("Searching pattern:",pat,"\n\nString:",arr,"\n\nOutput:",patternMatchingUnix(arr,pat))
