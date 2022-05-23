#python3SumToZero
#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#Notice that the solution set must not contain duplicate triplets.
class Solution:
    def threeSum(self, nums): #List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        nums.sort()
        print(nums)
        result=[]
        n=len(nums)
        for i in range(1,n-1):
            j,k=0,n-1
            while j!=i and k!=i:
                #print(i,j,k)
                if nums[i]+nums[j]+nums[k]<0:
                    j+=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    temp=[nums[j],nums[i],nums[k]]
                    if temp not in result:
                        result.append(temp)
                    j+=1
                    k-=1
        return(result)
            
if __name__=="__main__":
    nums = [-1,0,1,2,-1,-4]
    s=Solution()
    print(s.threeSum(nums))
    nums = []
    s=Solution()
    print(s.threeSum(nums))
    nums = [0]
    s=Solution()
    print(s.threeSum(nums))
    
    
#better be done where low and high have an index running between them
# check low+high+i==0 or not and then move the low and high accordingly
