#zigzagConversion.py
class Solution:
    def convert(self, s, numRows):
        if numRows <=1:
            return s
        it=1
        change=1
        d=dict()
        result=""
        for i in s:
            if it==numRows:
                change=-1
            if it==1:
                change=1
            if it in d: 
                d[it].append(i) 
            else:
                d[it]=[i]
            it=it+change
            print(i,it,change,d)
        for i in range(1,min(numRows+1,len(s)+1)):
            result+="".join(d[i])
        return result
        
    def convert1(self,s,numRows):
        if numRows<=1:
            return s
        l=[""]*numRows
        it,step=1,1
        for i in s:
            if it==numRows:
                step=-1
            if it==1:
                step=1
            l[it-1]+=i
            it+=step
        return "".join(l)
        


s=Solution()
print(s.convert1("PAYPALISHIRING",3))