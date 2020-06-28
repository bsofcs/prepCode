"""
largestPalindrome.py
"""
def longestPalindrome(arr):
 if arr is None:
  return
 len_a=len(arr)
 if len_a==1:
  return arr
 maxlen=0
 low_final=-1
 for i in range(len_a):
  low=i-1
  high=i
  while low>=0 and high<len_a and arr[low]==arr[high]:
   temp_len=high-low+1
   if maxlen<temp_len:
    maxlen=temp_len
    low_final=low
   low-=1
   high+=1
  low=i-1
  high=i+1
  while low>=0 and high<len_a and arr[low]==arr[high]:
   temp_len=high-low+1
   if maxlen<temp_len:
    maxlen=temp_len
    low_final=low
   low-=1
   high+=1
 return(arr[low_final:low_final+maxlen] if maxlen>=1 else "No Palindrome")

def allPalindromes(arr):
 if arr is None:
  return
 len_a=len(arr)
 if len_a==1:
  print(arr)
  return
 maxlen=0
 for i in range(len_a):
  low=i-1
  high=i
  while low>=0 and high<len_a and arr[low]==arr[high]:
   print(arr[low:high+1])
   low-=1
   high+=1
  low=i-1
  high=i+1
  while low>=0 and high<len_a and arr[low]==arr[high]:
   print(arr[low:low+high+1])
   low-=1
   high+=1

arr="nksjdhaheawoerjsdlnlnflkjsdlffffjsdsj"
print("String:",arr)
print("Longest Palindrome:",longestPalindrome(arr))
print("All palindromes in the string:")
allPalindromes(arr)
