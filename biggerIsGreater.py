def smallestButGreaterThan(lst,char):
 f_list=list(filter(lambda x:x>char, lst))
 min_list=min(f_list)
 min_index=f_list.index(min_list)
 return(min_list,min_index)

def biggerIsGreater(w):
 len_w=len(w)
 list_w=list(w)
 if len_w<1 or len_w>100:
  return
 for i in range(len_w-1,0,-1):
  if list_w[i]<=list_w[i-1]:
   continue
  rest=list_w[i:len_w]
  if len(rest)==1:
   small,index= list_w[i],int(i)  
  else: 
   small,index= smallestButGreaterThan(rest,list_w[i-1])
  if len(rest)==1: 
   result=list_w[0:i-1]
   result.append(list_w[i])
   result.append(list_w[i-1])
   return "".join(result)
  rest.pop(index)
  rest.append(list_w[i-1])
  rest=sorted(rest)
  result=list_w[0:i-1]+[small]+rest
  result="".join(result)
  return(result)
 #nothing matches
 return("No answer")

w="efgabdc"
print(w,end=" :")
print(biggerIsGreater(w))
w="dca"
print(w,end=" :")
print(biggerIsGreater(w))
w="ab"
print(w,end=" :")
print(biggerIsGreater(w))
w="bb"
print(w,end=" :")
print(biggerIsGreater(w))
w="hefg"
print(w,end=" :")
print(biggerIsGreater(w))
w="dhck"
print(w,end=" :")
print(biggerIsGreater(w))
w="dkhc"
print(w,end=" :")
print(biggerIsGreater(w))
w="lmno"
print(w,end=" :")
print(biggerIsGreater(w))
w="dcba"
print(w,end=" :")
print(biggerIsGreater(w))
w="dcbb"
print(w,end=" :")
print(biggerIsGreater(w))
w="abdc"
print(w,end=" :")
print(biggerIsGreater(w))
w="abcd"
print(w,end=" :")
print(biggerIsGreater(w))
w="fedcbabcd"
print(w,end=" :")
print(biggerIsGreater(w))