#longestPalindrome.py
class Solution:
    def longestPalindromeNum(self, s):
        if s is None:
            return None
        s="$"+"$".join(list(s))+"$"
        n=len(s)
        m=[0]*n
        mn=float("-INF")
        res=""
        for i in range(1,n):
            for j in range(i+1):
                if j==0:
                    m[i]=1
                    temp="".join(s[i:i+1]).replace("$","")
                    if len(res)<len(temp):
                        res=temp
                elif i+j>=n or i-j<0:
                    break
                elif s[i+j]==s[i-j]:
                    m[i]+=2
                    temp="".join(s[i-j:i+j+1]).replace("$","")
                    if len(res)<len(temp):
                        res=temp
                else:
                    break
            mn=max(mn,m[i])
        return res

    def longestPalindrome(self, s):
        if s is None:
            return None
        n=len(s)
        m=[[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            m[i][i]=1
        mx=1
        res=s[0]
        for l in range(2,n+1):
            for i in range(n-l+1):
                j=i+l-1
                if s[i]==s[j] and (m[i+1][j-1]==1 or l==2):
                    m[i][j]=1
                    mx=max(mx,j-i+1)
                    if len(s[i:j+1])>len(res):
                        res=s[i:j+1]
        return res
        
inputStr=['babad','cbbd','a','ac','bb']
print(inputStr)
s=Solution()
for i in inputStr:    
    print(i,":",s.longestPalindromeNum(i),s.longestPalindrome(i))