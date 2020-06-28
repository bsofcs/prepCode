def kaprekarNumbers(p, q):
 if p<=0 or q>=100000 or p>=q:
  return None
 count=0
 for i in range(p,q+1):
  i_arr=len(str(i))
  if i==1:
   print(i,end=" ")
   continue
  num=str(int(i)*int(i))
  len_s=len(num)
  if len_s==2*i_arr or len_s==2*i_arr-1:
   a=num[:len_s//2]
   b=num[len_s//2:]
   a= 0 if len(a)==0 else int("".join(a))
   b= 0 if len(b)==0 else int("".join(b))
   #print("i:",i,"j:",j,"a:",a,"b:",b)
   if a+b==i:
    count+=1
    print(i,end=" ")
 if count==0:
  print("INVALID RANGE")
p=1000
q=10000
kaprekarNumbers(p, q)
print("")