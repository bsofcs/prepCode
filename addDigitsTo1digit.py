# nums = 38
# soln = 3+8 -> 11 -> 1+1 --> 2
# result =2
#
# nums = 0
# result =0
#
#
# nums = 198
# soln = 1+9+8 -> 18 -> 1+8 ->9
# result =9
#

class Solution:
    def addDigits(self, num: int) -> int:
        if num is None:
            return None
        result=0
        if num<10:
            return num
        while num>=10:
            print(result,num)
            while num:
                result+=(num%10)
                num//=10
            
            if result>=10:
                num=result
                result=0
                print("result in if:",result)
        return result
        
class Solution1:
    def addDigits(self, num: int) -> int:
        if(num==0):
            return 0
        elif(num%9==0):
            return 9
        else:
            return num%9
        
        
s=Solution()
num=19
print(s.addDigits(num))