def multiply(a,b):
 if a is None or b is None:
  return
 mul=[[0 for i in range(2)] for j in range(2)]
 for i in range(2):
  for j in range(2):
   mul[i][j]=0
   for k in range(2):
    mul[i][j]+=a[i][k]*b[k][j]
 return mul

def power(a,n):
 M=[[1,1],[1,0]]
 if n==1:
  return M
 a=power(a,int(n/2))
 a=multiply(a,a)
 if n%2!=0:
  a=multiply(a,M)
 return a

def fibonacciMatrix(n):
 if n==0:
  return 0
 if n==1 or n==2:
  return 1
 M=[[1,1],[1,0]]
 return(power(M,n-1))

def fibonacci(n):
 if n==0:
  return 0
 if n==1 or n==2:
  return 1
 a=b=1
 for i in range(n-2):
  a,b=b,(a+b)
 return b

#0,1,1,2,3,5,8,13,21,
#0,1,2,3,4,5,6,7, 8,
promt="=>"
n=int(input(promt))
print("In LogN time:",fibonacciMatrix(n)[0][0],"\nIn N time:",fibonacci(n))