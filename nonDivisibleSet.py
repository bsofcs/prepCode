def nonDivisibleSubset(k, s):
 n=len(s)
 if n not in range(1,10**5+1) or k not in range(1,101) or any(map(lambda s: s not in range(1,10**9+1),s)):
  return
 mod_arr=[0]*k
 for x in s:
  mod_arr[x%k]+=1
 count=min(mod_arr[0],1)
 for i in range(1,k//2+1):
  if i != k-i:
   count+=max(mod_arr[i],mod_arr[k-i])
 if k%2==0:
  count+=1
 print(count) 
s=[1,2,3,4,5,6,7,8,9,10]
k=4
nonDivisibleSubset(k, s)