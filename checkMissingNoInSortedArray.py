def checkMissingXOR(arr):
 X=X1=0
 n=len(arr)
 for i in arr:
  X=X^i
 for i in range(n+2):
  X1=X1^i
 print(X^X1)

def checkMissingNoInSortedArray(arr):
 n=len(arr)
 sum_t=int((n+1)*(n+2)/2)
 #sum_a=reduce((lambda x, y: x + y), arr) 
 sum_a=sum(arr)
 print(sum_t-sum_a)

arr=[3,4,1,5,6]
checkMissingNoInSortedArray(arr)
checkMissingXOR(arr)


