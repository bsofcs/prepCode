#sortCharactersByFrequency
import collections
class Solution:
    def frequencySort(self, s):
        if s is None:
            return None
        x=dict()
        for i in s:
            if i in x:
                x[i]+=1
            else:
                x[i]=1
        s_dict=sorted(x.items(),key = lambda i:i[1],reverse=True)
        print(s_dict)
        res=[]
        for i in s_dict:
            t=i[0]*i[1]
            res.append(t)
        print("".join(res))
        
        
if __name__=='__main__':
    s="bhanusaurabh"
    sol=Solution()
    sol.frequencySort(s)
    