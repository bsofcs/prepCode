"""
count=Count of 5s in prime factors of n!
     =floor(n/5) + floor(n/25) + floor(n/125) + ....
"""
def trailingZerosInFactorial(n):
 count=0
 if n<0:
  return -1
 i=5
 while n/i>0:
  count+=n//i
  i*=5
 return count
print(trailingZerosInFactorial(100))