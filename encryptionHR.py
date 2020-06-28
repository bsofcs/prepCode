import math
def encryption(s):
 len_s=len(s)
 s_arr=list(s)
 if len_s<1 or len_s>81:
  return
 row=math.floor(math.sqrt(len_s))
 col=math.ceil(math.sqrt(len_s))
 while (row*col)<len_s:
  row+=1
 i,x,y=0,0,0
 cipher=[['' for i in range(col)] for j in range(row)]
 while i<len_s and x<row:
  y=0
  while i<len_s and y<col:
   cipher[x][y]=s_arr[i]
   i+=1
   y+=1
  x+=1
 x,y=0,0
 result=""
 for y in range(col):
  for x in range(row):
   result=result + cipher[x][y]
  result=result+" "
 print(result)

s="askjhd"
print(s)
encryption(s)
s="feedthedog"
print(s)
encryption(s)
s="haveaniceday"
print(s)
encryption(s)
s="ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"
print(s)
encryption(s)
