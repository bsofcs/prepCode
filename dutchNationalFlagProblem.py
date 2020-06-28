#dutchNationalFlagProblem
def segregateEvenOdd(arr):
 if arr is None:
  return
 EvenArr=list(filter(lambda x:x%2==0,arr))
 OddArr=list(filter(lambda x:x%2!=0,arr))
 return EvenArr+OddArr

def sortColors(nums):
        if nums is None:
            return 
        Arr0=list(filter(lambda x:x==0,nums))
        Arr1=list(filter(lambda x:x==1,nums))
        Arr2=list(filter(lambda x:x==2,nums))
        return Arr0+Arr1+Arr2

def dutchNFP(nums):
 if nums is None:
  return 
 low,mid,high=0,0,len(nums)-1
 while mid<=high:
  print(nums,low,mid,high)
  if nums[mid]==0:
   nums[low],nums[mid]=nums[mid],nums[low]
   low+=1
   mid+=1
  elif nums[mid]==2:
   nums[high],nums[mid]=nums[mid],nums[high]
   high-=1
  else:
   mid+=1

arr=[12,16,22,30,35,39,42,45,58,48,50,53,55,56]
print(segregateEvenOdd(arr))
arr= [2,0,2,1,1,0]
print(sortColors(arr))
nums= [0,1,1,2,2,0,1,0]
dutchNFP(nums)
print(nums)