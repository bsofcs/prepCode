def repeatedString(s, n):
 s_len=len(s)
 if n not in range(1,10**12+1) or s_len not in range(1,101):
  return
 occ=s.count("a")
 count=(n//s_len)*occ
 remain=n%s_len
 s_left=s[:remain:] if remain>0 else ""
 count+=s_left.count('a')
 return count


s="gfcaaaecbg"
n=547602
print(repeatedString(s, n))