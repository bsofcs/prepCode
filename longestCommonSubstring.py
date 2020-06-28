"""
longestCommonSubstring.py
"""
def swap(arr1,arr2):
 lst=list(arr1)
 temp=[]
 for i in lst:
  temp.append(i)
 arr1=arr2
 arr2="".join(temp)
 return arr1,arr2

def longestCommonSubstring(arr1,arr2):
 if arr1 is None or arr2 is None:
  return
 if len(arr1)>len(arr2):
  arr1,arr2=swap(arr1,arr2)
 len_a1=len(arr1)
 len_a2=len(arr2)
 lst_a1=list(a1)
 lst_a2=list(a2)
 maxlen=0
 low_final=-1
 for i in range(len_a2):
  j=0
  while j<len_a1 and "".join(lst_a1[j:j+t])=="".join(lst_a2[i:i])


arr1="saurabh"
arr2="bhanu"
longestCommonSubstring(arr1,arr2)