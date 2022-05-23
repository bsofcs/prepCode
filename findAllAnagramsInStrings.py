#findAllAnagramsInStrings
#Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
#
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
#Example 1:
#
#Input: s = "cbaebabacd", p = "abc"
#Output: [0,6]
#Explanation:
#The substring with start index = 0 is "cba", which is an anagram of "abc".
#The substring with start index = 6 is "bac", which is an anagram of "abc".
#Example 2:
#
#Input: s = "abab", p = "ab"
#Output: [0,1,2]
#Explanation:
#The substring with start index = 0 is "ab", which is an anagram of "ab".
#The substring with start index = 1 is "ba", which is an anagram of "ab".
#The substring with start index = 2 is "ab", which is an anagram of "ab".

class Solution:
    def indexHash(self,s):
        return ord(s)-ord('a')
    def findAnagrams(self, s, p):
        if None in (s,p):
            return None
        if len(p)>len(s):
            return None
        shash=[0]*26
        phash=[0]*26
        for i in p:
            phash[self.indexHash(i)]+=1
        ls=len(s)
        lp=len(p)
        left,right=0,lp-1
        result=[]
        for i in range(lp):
            shash[self.indexHash(s[i])]+=1
        if shash==phash:
            result.append(0)
        while right<ls-1:
            shash[self.indexHash(s[left])]-=1
            left+=1
            right+=1
            shash[self.indexHash(s[right])]+=1
            if shash==phash:
                result.append(left)
        return result


st=Solution()
s = "cbaebabacd" 
p = "abc"
print(st.findAnagrams(s,p))
s = "abab"
p = "ab"
print(st.findAnagrams(s,p))