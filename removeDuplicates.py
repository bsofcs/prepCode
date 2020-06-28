"""
removeDuplicates
"""
def remove_duplicates(A):
 m=0
 for i in range(len(A)):
  if not elem(A,m,A[i]):
   print(A[m],A[i],m,i)
   A[m]=A[i]
   m+=1
 return m

def elem(A,n,e):
 for i in range(n):
  if A[i]==e:
   return 1
 return 0

def remove_dup(A):
 A.sort()
 j=0
 print(A)
 for i in range(1,len(A)):
  if A[j]!=A[i]:
   print(i,j,A[i],A[j])
   j+=1
   A[j]=A[i]
   print(A)
 print(A[:j+1])

def removeDupInOneGo(A):
 un=[]
 helperSet=set()
 for x in A:
  if x not in helperSet:
   un.append(x)
   helperSet.add(x)
   print(un,helperSet)
 print("A:",A,"\nO/p:",un,"\nHelperSet:",helperSet)

A=[54,26,93,54,77,31,44,55,20,20]
#remove_duplicates(A)
remove_dup(A)

A=[1,2,5,2,4,'a','a','b',51,75,'l']
removeDupInOneGo(A)
