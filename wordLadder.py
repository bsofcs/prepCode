#wordLadder
#A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#
#Every adjacent pair of words differs by a single letter.
#Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#sk == endWord
#Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
#
#Example 1:
#
#Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
#Output: 5
#Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
#Example 2:
#
#Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
#Output: 0
#Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
# 
#
#Constraints:
#
#1 <= beginWord.length <= 10
#endWord.length == beginWord.length
#1 <= wordList.length <= 5000
#wordList[i].length == beginWord.length
#beginWord, endWord, and wordList[i] consist of lowercase English letters.
#beginWord != endWord
#All the words in wordList are unique.

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if None in (beginWord, endWord, wordList):
            return None
        if endWord not in wordList:
            return 0
        if beginWord==endWord:
            return 1
        n=len(wordList[0])
        wordList=set(WordList)                     #convert the list to set thus making it a hashMap
        idx=1
        q=[(beginWord,idx)]
        alpha='abcdefghijklmnopqrstuvwxyz'
        while q:
            #print(q)
            tmpWrd,idx=q.pop(0)
            if tmpWrd==endWord:
                return idx
            for i in range(n):
                for c in alpha:
                    tmp=tmpWrd[:i]+c+tmpWrd[i+1:]
                    if tmp in wordList:
                        wordList.remove(tmp)       #pop(wordList.index(tmp)) takes time so use remove
                        q.append((tmp,idx+1))
        return 0

class Solution1:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0


s=Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(beginWord, endWord, wordList,s.ladderLength(beginWord, endWord, wordList))