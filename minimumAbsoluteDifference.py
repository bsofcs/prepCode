"""
Consider an array of integers, arr=[arr[0],arr[1],...,arr[n-1]]. 
We define the absolute difference between two elements, arr[i] and arr[j] (where i!=j ),
to be the absolute value of arr[i]-arr[j]

Given an array of integers, find and print the minimum absolute difference between any two elements 
in the array. For example, given the array arr=[-2,2,4]
we can create  pairs of numbers: [-2,2],[-2,4] and [2,4]. 
The absolute differences for these pairs are |(-2)-2|=4,|(-2)-4|=6  and |2-4|=2. 
The minimum absolute difference is 2.

Function Description

Complete the minimumAbsoluteDifference function in the editor below. It should return an integer that represents the minimum absolute difference between any pair of elements.

minimumAbsoluteDifference has the following parameter(s):

n: an integer that represents the length of arr
arr: an array of integers
Input Format

The first line contains a single integer n, the size of arr.
The second line contains n space-separated integers arr[i].

Constraints
2<=n<=10**5
-10**9<=arr[i]<=10**9

Output Format

Print the minimum absolute difference between any two elements in the array.

"""
def findPivot(arr,low,high):
 pivot=arr[high]
 i=low-1
 for j in range(low,high):
  if arr[j]<=pivot:
   i+=1
   arr[i],arr[j]=arr[j],arr[i]
 arr[i+1],arr[high]=arr[high],arr[i+1]
 return(i+1)

def quickSort(arr,low,high):
 if arr is None or low>=high:
  return 
 pivot=findPivot(arr,low,high)
 quickSort(arr,low,pivot-1)
 quickSort(arr,pivot+1,high)

def minimumAbsoluteDifference(arr):
 n=len(arr)
 if n not in range(2,10**5+1) or any(x not in range(-1*10**9,10**9+1) for x in arr):
  return None
 quickSort(arr,0,len(arr)-1)
 minVal=float("INF")
 for i in range(n-1):
  tmp=abs(arr[i]-arr[i+1])
  if tmp<minVal:
   minVal=tmp
 return minVal

arr=[3,-7,0]
print(minimumAbsoluteDifference(arr))
arr=[-59,-36,-13,1,-53,-92,-2,-96,-54,75]
print(minimumAbsoluteDifference(arr))