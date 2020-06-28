def printRepeatingAndMissingNum(arr):
 if arr is None:
  return
 size=len(arr)
 for i in range(size):
  if arr[abs(arr[i])-1]>=0:
   arr[abs(arr[i])-1]=-arr[abs(arr[i])-1]
  else:
   print("The repeating element is:",arr[i])
   break

arr=[0,1,2,3,4,4,5,6]
printRepeatingAndMissingNum(arr)