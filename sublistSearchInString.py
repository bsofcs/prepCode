def longestPrefixSuffix(pattern):
 if pattern is None:
  return
 p_arr=list(pattern)
 len_a=len(p_arr)
 result=[0]*len_a
 i=0;j=1
 while j<len_a:
  if p_arr[j]==p_arr[i]:
   result[j]=i+1
   i+=1
  j+=1
 return result

def sublistSearchString(statement,pattern):
 if statement is None or pattern is None:
  return
 i=j=0 
 len_s=len(statement)
 lst_s=list(statement)
 len_p=len(pattern)
 lst_p=list(pattern)
 lps=longestPrefixSuffix(pattern)
 match_flag=False
 while i<len_s and j<len_p:
  if lst_s[i]!=lst_p[j] and match_flag==True:
   match_flag=False
   j=lps[j-1]
  if lst_s[i]==lst_p[j]:
   match_flag=True
   j+=1
  i+=1
 if j==len_p:
  return True
 else:
  return False


pattern="abcaby"
statement="abcabcabxabcaby"
print(sublistSearchString(statement,pattern))
pattern="fixprefixsuffix"
statement="abcabcabxabcaby"
print(sublistSearchString(statement,pattern))
statement="abcabcabfixprefixsuffixxabcaby"
print(sublistSearchString(statement,pattern))


#fixprefixsuffix
#000000123000000
