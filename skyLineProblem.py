"""
skyLineProblem

Given n rectangles in a 2D city, computes the skyline of these buildings, eliminating hidden lines. The main task is to view buildings from a side and remove all sections that are not visible.
All buildings share common bottom and every building is represented by triplet (left,ht and right).
1. left: is the x coordinate of the left side
2. right: is the x coordinate of the right side
3. ht: is the height of the building

A skyline is a collection of rectangular strips. A rectangular strip is represented as a pair of (left,ht).

Input: array of (left,right,height)
Output: array of (left,height)
For example: In case there is only one building
Input: [(1,5,11)]
Output: [(1,11),(5,0)]

Thus, in a multiple building city:
Input: [(1,5,11),(2,7,6),(3,9,13),(12,16,7),(14,25,3),(19,22,18),(23,29,13),(24,28,4)]

Algorithm:
1. Convert all the buildings as a pair of start and end line.
	for ex- for building[(1,5,11)] it will be [(1,11,'s'),(5,11,'e')]
2. Sort these lines based on their x-axis values but with following consideration:
	i.	two starts are compared then higher height building should be picked first
	ii.	two ends are compared then lower height building should be picked first
	iii.	one start and one end is compared then start should appear before end

Considering

class Building:
	def __init__(self,left=0,ht=0,right=0):
		self.left=left
		self.ht=ht
		self.right=right

class Line:
	def __init__(self,left=0,ht=0,mark=''):
		self.left=0
		self.ht=0
		self.mark=mark

"""
import heapq
def MergeSort(arr):
	n=len(arr)
	if n<=1:
		return
	mid=n//2
	L,R=arr[:mid],arr[mid:]
	MergeSort(L)
	MergeSort(R)
	i=j=k=0
	while i<len(L) and j<len(R):
		if L[i][0]<=R[j][0]:
			if L[i][0]<R[j][0]:
				arr[k]=L[i]
				i+=1
			elif L[i][0]==R[j][0] and L[i][2]==R[j][2] and L[i][2]=="s":
			#two starts are compared then higher height building should be picked first
				if L[i][1]>=R[j][1]:
					arr[k]=L[i]
					i+=1
				else:
					arr[k]=R[j]
					j+=1
			elif L[i][0]==R[j][0] and L[i][2]==R[j][2] and L[i][2]=="e":
			#two ends are compared then lower height building should be picked first
				if L[i][1]<=R[j][1]:
					arr[k]=L[i]
					i+=1
				else:
					arr[k]=R[j]
					j+=1
			else:
			#one start and one end is compared then start should appear before end
				if L[i][2]=="s":
					arr[k]=L[i]
					i+=1
				else:
					arr[k]=R[j]
					j+=1
		else:
			arr[k]=R[j]
			j+=1
		k+=1
	while i<len(L):
		arr[k]=L[i]
		i+=1;k+=1
	while j<len(R):
		arr[k]=R[j]
		j+=1;k+=1

# Input a Building array and returns Line array
def convertBuildingsToLines(building):
	n=len(building)
	if n==0:
		return None
	result=[]
	for i in range(n):
		start=(building[i][0],building[i][2],"s")
		result.append(start)
		end=(building[i][1],building[i][2],"e")
		result.append(end)
	MergeSort(result)
	return result

class Solution:
	def getSkyline(self, buildings):
		n=len(buildings)
		if n<1:
			return None
		lines=convertBuildingsToLines(buildings)
		ln=len(lines)
		h=[0]
		result=[]
		max_till_now=0
		heapq.heapify(h)
		for i in range(ln):
			temp=lines[i]
			if temp[2]=="s" and temp[1] not in h:
				heapq.heappush(h,(temp[1]*(-1)))
			if temp[2]=="e":
				h.pop(h.index((-1)*temp[1]))
				heapq.heapify(h)
			if max_till_now!=h[0]*(-1):
				max_till_now=h[0]*-1
				result.append([temp[0],max_till_now])
		return result
				
		
        
building=[[1,5,11],[2,7,6],[3,9,13],[12,16,7],[14,25,3],[19,22,18],[23,29,13],[24,28,4]]
result=convertBuildingsToLines(building)
print("\n")
print(building)
print("\n")
print(result)

x=Solution()
result=x.getSkyline(building)
print("\n")
print(result)

building=[[0,1,3]]
result=x.getSkyline(building)
print("\n")
print(result)