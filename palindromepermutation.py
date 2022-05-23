#palindromepermutation.py
class Solution:
    def canPermutePalindrome(self, s):
        if s is None:
            return False
        d=dict()
        n=len(s)
        for i in range(n):
            if s[i] in d:
               d[s[i]]+=1
            else:
                d[s[i]]=1
        count_even=0
        count_odd=0
        for i in d.keys():
            if d[i]%2==0:
                count_even+=1
            else:
                count_odd+=1
        if count_odd<=1:
            return True
        else:
            return False
            
s=['code','aab','carerac','a','ab']
l=Solution()
for i in s:
    print(i,l.canPermutePalindrome(i))