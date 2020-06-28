"""
Marc loves cupcakes, but he also likes to stay fit. Each cupcake has a calorie count, and Marc can walk a distance to expend those calories. 
If Marc has eaten j cupcakes so far, after eating a cupcake with c calories he must walk at least 2**jXc miles to maintain his weight.
"""
def findPivot(arr,low,high):
 pivot=arr[high]
 i=low-1
 for j in range(low,high):
  if arr[j]>=pivot:
   i+=1
   arr[i],arr[j]=arr[j],arr[i]
 arr[i+1],arr[high]=arr[high],arr[i+1]
 return(i+1)

def QuickSortDesc(arr,low,high):
 if low>=high:
  return
 pivot=findPivot(arr,low,high)
 QuickSortDesc(arr,low,pivot-1)
 QuickSortDesc(arr,pivot+1,high)

def marcsCakewalk(calorie):
 n=len(calorie)
 if n not in range(1,41) or any(x not in range(1,1001) for x in calorie):
  return None
 QuickSortDesc(calorie,0,n-1)
 sumTotal=0
 for i in range(n):
  sumTotal+=calorie[i]*(2**i)
 return sumTotal

calorie=[1,3,2]
print(marcsCakewalk(calorie))
calorie=[7,4,9,6]
print(marcsCakewalk(calorie))
