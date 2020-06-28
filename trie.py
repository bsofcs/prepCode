from collections import defaultdict

class TrieNode:
 def __init__(self):
  self.children=defaultdict()
  self.terminating=False

class Trie:
 def __init__(self):
  self.root=self.get_node()

 def returnChild(self):
  return self.root.children
 
 def isTerminate(self):
  return self.root.terminating

 def get_node(self):
  return TrieNode()

 def get_index(self,ch):
  return ord(ch)-ord('a')

 def insert(self,word):
  root=self.root
  len1=len(word)
  for i in range(len1):
   index=self.get_index(word[i])
   if index not in root.children:
    root.children[index]=self.get_node()
   root=root.children.get(index)
  root.terminating=True

 def search(self,word):
  root=self.root
  len1=len(word)
  for i in range(len1):
   index=self.get_index(word[i])
   if not root:
    return False
   root=root.children.get(index)
  return(True if root and root.terminating else False)

 def delete(self,word):
  root=self.root
  len1=len(word)
  for i in range(len1):
   index=self.get_index(word[i])   
   if not root:
    print("Word not found")
    return -1
   root=root.children.get(index)
  if not root:
   print("Word not found")
   return -1
  else:
   root.termianting=False
   return 0

 def update(self,old_word,new_word):
  val=self.delete(old_word)
  if val==0:
   self.insert(new_word)

 
def printAllElements(trieNode,word=""):
 lst_word=list(word)
 len_word=len(lst_word)
 if trieNode is None:
  print("Return")
  return
 child=trieNode.children
 for i in child.keys():
  ch=child[i]
  lst_word.append(chr(i+ord('a')))
  if ch.terminating==True:
   print("".join(lst_word))
  printAllElements(ch,"".join(lst_word))
  lst_word.pop(len_word)

strngs=["pqrs","pprt","psst","qqrs","pqrst","bhanu"]
t=Trie()
for i in strngs:
 t.insert(i)
"""
print("pqrs:",t.search("pqrs"))
print("pset:",t.search("pset"))
print("pqrst:",t.search("pqrst"))
print("pqrst:",t.search("pqrst"))
print("update psst to pset")
t.update("psst","pset")
print("pset:",t.search("pset"))
"""
print("All Elements:")
printAllElements(t.root)
