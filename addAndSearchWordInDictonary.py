#addAndSearchWordInDictonary
#Design a data structure that supports adding new words and finding if a string matches any previously added string.
#
#Implement the WordDictionary class:
#
#WordDictionary() Initializes the object.
#void addWord(word) Adds word to the data structure, it can be matched later.
#bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
# 
 
class Trie:
    def __init__(self, endOfWord=False):
        self.child = [None]*26
        self.endOfWord = endOfWord

class WordDictionary:
    def index(self, c):
        return(ord(c)-97)
    
    def __init__(self):
        self.root=Trie()
    
    def addWord(self,word):
        if word is None:
            return
        node=self.root
        for i in range(len(word)):
            if node.child[self.index(word[i])]==None:
                node.child[self.index(word[i])]=Trie()
            node=node.child[self.index(word[i])]
        node.endOfWord=True
        
    def searchWord(self,word):
        if word is None:
            return False
        return self.searchUtil(word,self.root,0)
        
    def searchUtil(self, word, node, pos):
        if node is None:
            return False
        ans= False
        if pos==len(word):
            return node.endOfWord
        if word[pos]=='.':
            for i in range(26):
                ans = ans or self.searchUtil(word,node.child[i],pos+1)
        else:
            if node.child[self.index(word[pos])]==None:
                ans= False
            else:
                ans=self.searchUtil(word,node.child[self.index(word[pos])],pos+1)
        return ans

if __name__=="__main__":
    command=["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    inputData=[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    s=WordDictionary()
    for i in range(1,len(command)):
        if command[i]=="addWord":
            s.addWord(inputData[i][0])
            print(inputData[i][0]," is added")
        else:
            print(inputData[i][0],":",s.searchWord(inputData[i][0]))