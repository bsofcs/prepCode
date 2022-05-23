"""
sortInExactPattern
Input
arr=a1,a2,a3,...,an,b1,b2,b3,...,bn
Output
arr=a1,b1,a2,b2,a3,b3,...,an,bn
"""
def printInSpecialSort(arr):
 n=len(arr)
 arrA=arr[:n//2]
 arrB=arr[n//2:]
 result=[]
 i=0
 for i in range(n//2):
  result.append(arrA[i])
  result.append(arrB[i])
 return result



n=25
arrA=["a"+str(i) for i in range(1,n+1)]
arrB=["b"+str(i) for i in range(1,n+1)]
arr=arrA+arrB
print("Input:",arr)
print("Output:",printInSpecialSort(arr))