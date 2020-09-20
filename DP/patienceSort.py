"""
patienceSort
The Sorting Technique is inspired by the game of Patience. The technique is used by the analog world for sorting as the most common way.
We create bundles of the elements with the condition that the elements on the top will always will be smaller than the one below.
A new bundle is created if the number next is larger than the number placed at top of the bundles made till that point.
Once all the elements are encountered and placed in the bundles, we fetch the smallest of the all the bundle top's and place them in another array.
"""

class Bundle:
	def __init__(self,arr=None):
		self.n=len(arr)
		self.arr=[] if self.n==0 else [i for i in arr]
	def push(self,val):
		if self.n==0:
			self.arr=[val]
		else:
			self.arr.append(val)
		self.n+=1
	def pop(self):
		if self.n==0:
			return None
		else:
			self.n-=1
			temp=self.arr.pop(self.n)
			return temp
	def peep(self):
		if self.n==0:
			return None
		else:
			return self.arr[self.n-1]
	def print(self):
		for i in range(self.n):
			print(self.arr[i],end=",")

def makeBundle(arr,n):
	if arr is None or n is None:
		return None
	bundle=[]
	for i in range(n):
		insert=0
		for b in range(len(bundle)):
			if bundle[b].peep()>arr[i]:
				bundle[b].push(arr[i])
				insert=1
				break
		if insert==0:
			bundle.append(Bundle([arr[i]]))
	for i in range(len(bundle)):
		bundle[i].print()
		print()
	return bundle

def sortBundle(bundle,n):
	if bundle is None or n is None:
		return None
	tmp=[]
	for i in range(n):
		heads=[float("INF") if i.peep() is None else i.peep() for i in bundle]
		index=heads.index(min(heads))
		tmp.append(bundle[index].pop())
		print(i,heads,index,tmp)
	return tmp

def patienceSort(arr):
	if arr is None:
		return None
	n=len(arr)
	bundle=makeBundle(arr,n)
	return sortBundle(bundle,n)

arr=[4,23,5,7,2,6,9]
print(arr)
arr=patienceSort(arr)
print(arr)