"""
allPossibleSubset
"""
class Solution:
    def subsets(self, nums):
        if nums is None:
            return None
        n=len(nums)
        ni=2**n
        result=[]
        for i in range(ni):
            #con=list(bin(i))[2:]
            #while(len(con)<n):
            #    con.insert(0,'0')
            con=list(bin(i)[2:].zfill(n))       #very Important zfill which does left padding
            tmp=[]
            print(con)
            jn=len(con)
            for j in range(jn):
                print(j,con[j],nums[j])
                if con[j]=='1':
                    tmp.append(nums[j])
            print("TMP:",tmp)
            result.append(tmp)
        return result

class Solution1:
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result

s=Solution()
nums = [1,2,3]
print(nums,s.subsets(nums))
print([[nums[j] for j in range(len(nums)) if i >> j & 1] for i in range(2 ** len(nums))])
#>>> print ("'%-6s'"%'hi')
#'hi    '
#>>> print ("'%6s'"%'hi')
#'    hi'