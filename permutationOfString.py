def permutationOfAllChar(arr,size):
 if size==1:
  return(list(arr))
 lst_arr=list(arr)
 result=[i+j for i in lst_arr for j in permutationOfAllChar(arr,size-1)]
 return result

def swap(arr,i,j):
 lst_a=list(arr)
 lst_a[i],lst_a[j]=lst_a[j],lst_a[i]
 return("".join(lst_a))

def permutationString(arr,i=0):  #prints all o/p one by one
 n=len(arr)
 if i==n:
  print(arr,end=",")
  return
 for j in range(i,n):
  arr=swap(arr,i,j)
  permutationString(arr,i+1)
  arr=swap(arr,i,j)

result=[]
def permutationOfString(arr,level=0):  #appends to a global list
 if level==len(arr):
  result.append(arr)
 else:
  for j in range(level,len(arr)):
   arr=swap(arr,level,j)
   permutationOfString(arr,level+1)
   arr=swap(arr,level,j)

def permutationStringLexicographically(arr):
 l_arr=list(arr)
 count_map={}
 for ch in l_arr:
  if ch in count_map.keys():
   count_map[ch]+=1
  else:
   count_map[ch]=1
 keys=sorted(count_map)
 str=[]
 count=[]
 for key in keys:
  str.append(key)
  count.append(count_map[key])
 result=[0 for x in range(len(arr))]
 premute_util(str,count,result,0)

def premute_util(str,count,result,level):
 if level==len(result):
  print("".join(result),end=", ")
  return
 for i in range(len(str)):
  if count[i]==0:
   continue
  result[level]=str[i]
  count[i]-=1
  premute_util(str,count,result,level+1)
  count[i]+=1

arr="bhanu"
size=len(arr)
#print(permutationOfAllChar(arr,size))
print("Direct Print")
permutationString(arr)
print("\nPrints in global List")
permutationOfString(arr)
print(result)
print("Lexicographical Order:")
permutationStringLexicographically(arr)