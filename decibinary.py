#decibinary
class Solution:
 def minPartitions(self, n: str) -> int:
  arr=list(n);
  arr=[int(x) for x in arr];
  print(arr);
  count=0;
  while any(x>0 for x in arr):
   count+=1;
   print(arr);
   for i in range(len(arr)):
    if arr[i]>0:
     arr[i]-=1;
  return count;

if __name__=='__main__':
 n="1112212212211221212";
 s=Solution();
 print(s.minPartitions(n))