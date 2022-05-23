#permutationInStringWindow
class Solution:
    def findIndex(self,c):
        #print(c,int(ord(c)-ord('a')))
        return int(ord(c)-ord('a'))
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if None in (s1,s2):
            return None
        s1Hash=[0]*26
        s2Hash=[0]*26
        n1,n2=len(s1),len(s2)
        if n1>n2:
            return False
        for i in s1:
            s1Hash[self.findIndex(i)]+=1
        left,right=0,0
        while left<n2 and right<n2:
            s2Hash[self.findIndex(s2[right])]+=1
            if right-left+1==n1:
                if s1Hash==s2Hash:
                    return True
                else:
                    s2Hash[self.findIndex(s2[left])]-=1
                    left+=1
            right+=1                    
        return False


s=Solution()
s1 = "i"
s2 = "ei"
print(s1,s2,s.checkInclusion(s1,s2))