def Cloning(li1): 
    li_copy = [i for i in li1] 
    return li_copy

def beautifulTriplets(d, arr):
 n=len(arr)
 s_arr=sorted(arr)
 if n<1 or n>10**4 or d<1 or d>20 or any(map(lambda x:x<0 or x>2*10*4,arr)) or arr!=s_arr:
  return
 count=0
 for i in range(n):
  temp=Cloning(arr)
  temp.pop(i)
  d1=len(list(filter(lambda x:x-arr[i]==d,temp)))
  d2=len(list(filter(lambda x:x-arr[i]==2*d,temp)))
  count+=(d1*d2)
 return count



arr=[2,2,3,4,5]
d=1
print(beautifulTriplets(d, arr))
arr=[1,2,4,5,7,8,10]
d=3
print(beautifulTriplets(d, arr))