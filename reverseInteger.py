#reverseInteger.py
import math
class Solution:
    def reverse(self,x):
        x=(-1 if x<0 else 1)*int("".join(list(str(abs(x)))[::-1])) 
        return x if x>=-1*(2**31) and x<2**31 else 0
        
    def reverseInt(self,x):
        if x is None:
            return None
        flag=0
        if x<0:
            flag=1
            x*=-1
        tmp=x
        result=0
        while tmp>0:
            result*=10
            result+=(tmp%10)
            tmp//=10
        result=result if flag==0 else -1*result
        return result if result in range(-1*(2**31),(2**31)) else 0


s=Solution()
print(123,s.reverseInt(123),s.reverse(123))
print(-123,s.reverseInt(-123),s.reverse(-123))
print(0,s.reverseInt(0),s.reverse(0))
print(-0,s.reverseInt(-0),s.reverse(-0))
print(s.reverseInt(1534236469),s.reverse(1534236469))