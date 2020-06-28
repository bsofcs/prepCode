"""
boyerMoore.py
"""
NO_OF_CHAR=256
def badCharHeuristic(strng,sze):
 badChar=[-1]*NO_OF_CHAR
 for i in range(sze):
  badChar[ord(strng[i])]=i
 return badChar

def searchBadChar(txt,pattern):
 n,m=len(txt),len(pattern)
 badChar=badCharHeuristic(pattern,m)
 s=0
 while(s<=(n-m)):
  j=m-1
  while j>=0 and pattern[j]==txt[s+j]:
   j-=1
  if j<0:
   print("Pattern occurs at shift:",s)
   s+=(m-badChar[ord(txt[s+m])]) if s+m<n else 1
  else:
   s+=max(1,j-badChar[ord(txt[s+j])])
txt="gcaatgcctatgcgacc"
pattern="tatgcg"
searchBadChar(txt,pattern)
sze=len(pattern)
badChar=badCharHeuristic(pattern,sze)
for i in range(len(badChar)):
 if badChar[i]!=-1:
  print(i,":",badChar[i],":",chr(i))