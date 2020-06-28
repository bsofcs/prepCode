"""
frequencyCounter.py
find frequencies of elements without using extra space
"""
def frequencyCounter(A):
 pos=0
 n=len(A)
 print(A)
 while pos<n:
  expectedPos=A[pos]-1g
  print("ExpectedPos,Pos,A:",expectedPos,pos,A)
  if A[pos]>0 and A[expectedPos]>0:
   A[pos],A[expectedPos]=A[expectedPos],A[pos]
   A[expectedPos]=-1
  elif A[pos]>0:
   A[expectedPos]-=1
   A[pos]=0
   pos+=1
  else:
   pos+=1
  print("ExpectedPos,Pos,A:",expectedPos,pos,A,"\n")
 print(A)
 for i in range(n):
  print(i+1,"-->",abs(A[i]))

A=[10,1,9,4,7,6,5,5,1,2,1]
frequencyCounter(A)