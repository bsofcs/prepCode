def cutTheSticks(arr):
 n=len(arr)
 if n<1 or n>1000 or any(map(lambda x:x<1 or x>1000,arr)):
  return
 arr=sorted(arr)
 result=[]
 while(arr):
  result.append(len(arr))
  arr=list(filter(lambda s:s>0,arr))
  arr=list(filter(lambda s:s-arr[0],arr))
  #print(arr)
 return(result)

arr=[5,4,4,2,2,8]
print(cutTheSticks(arr))
arr=[1,2,3,4,3,3,2,1]
print(cutTheSticks(arr))