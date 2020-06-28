def findPivot(arr,low,high):
 pivot=ord(arr[high])
 i=low-1
 for j in range(low,high):
  if ord(arr[j])<=pivot:
   i+=1
   arr[i],arr[j]=arr[j],arr[i]
 arr[i+1],arr[high]=arr[high],arr[i+1]
 return(i+1)

def QuickSort(arr,low,high):
 if low>=high:
  return
 pivot=findPivot(arr,low,high)
 QuickSort(arr,low,pivot-1)
 QuickSort(arr,pivot+1,high)


def gridChallenge(grid):
 n=len(grid)
 m=len(grid[0])
 if n not in range(1,101):
  return None
 for i in range(n):
  QuickSort(grid[i],0,m-1)
 print(grid)
 for i in range(n):
  for j in range(m):
   if i-1>=0 and grid[i][j]<grid[i-1][j]:
    print("1",grid[i][j],grid[i-1][j],i,j)
    return "NO"
   if j-1>=0 and grid[i][j]<grid[i][j-1]:
    print("2",grid[i][j],grid[i][j-1],i,j)
    return "NO"
 return "YES"


grid=[['e','a','b','c','d'],
['f','g','h','i','j'],
['o','l','k','m','n'],
['t','r','p','q','s'],
['x','y','w','u','v']]
#print(gridChallenge(grid))

grid=[
['m','p','x','z'],
['a','b','c','d'],
['w','l','m','f']
]
print(gridChallenge(grid))