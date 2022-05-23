#longestSubstringWithoutRepeatingCharacter
#Given a string s, find the length of the longest substring without repeating characters.
#
#Example 1:
#
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.
#Example 2:
#
#Input: s = "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
#Example 3:
#
#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 
#
#Constraints:
#
#0 <= s.length <= 5 * 104
#s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s):
        if s is None:
            return None
        left,right,maxLength=0,0,0
        n=len(s)
        idx=set()
        idx_val={}
        newLeft=0
        while left<n and right<n:
            #print(left,right,s[right],idx,idx_val)
            if s[right] not in idx:
                idx.add(s[right])
                idx_val[s[right]]=right
                maxLength=max(maxLength,right-left+1)
                right+=1
            else:
                newLeft=idx_val[s[right]]
                while left<=newLeft:
                    idx_val[s[left]]=right
                    idx.remove(s[left])
                    left+=1
        return maxLength
        
        
s=Solution()
v="abcabcbb"
print(v,s.lengthOfLongestSubstring(v))
v="bbbbb"
print(v,s.lengthOfLongestSubstring(v))
v="pwwkew"
print(v,s.lengthOfLongestSubstring(v))
v="a"
print(v,s.lengthOfLongestSubstring(v))
v="1234567891"
print(v,s.lengthOfLongestSubstring(v))