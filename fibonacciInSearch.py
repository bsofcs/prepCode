def fibonacciSearch(arr,x):
 n=len(arr)
 finM2=0
 finM1=1
 fin=finM1+finM2
 offset=-1
 print(fin,finM1,finM2,offset,n)
 while fin<n:
  fin=finM1+finM2
  finM2,finM1=finM1,fin

 while fin>1:
  i=min(offset+finM2,n-1)
  print("fin:",fin,"finM1:",finM1,"finM2:",finM2,"offset:",offset,"i:",i)
  if arr[i]<x:
   fin=finM1
   finM1=finM2
   finM2=fin-finM1
   offset=i
  elif arr[i]>x:
   fin=finM2
   finM1=finM1-finM2
   finM2=fin-finM1
  else:
   return i
 if (finM1 and arr[offset+1]==x):
  return(offset+1)
 return -1

#       0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10
arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100] 
x = 85
print(fibonacciSearch(arr,x))