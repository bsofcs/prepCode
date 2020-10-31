"""
boxStacking
Assume that we are given a set of N types 3D boxes; the dimensions are defined for i'th box as:
	h[i]= height of the i'th box
	w[i]= width of the i'th box
	d[i]= depth of the i'th box
We need to stack them one above the other and print the tallest height that can be achieved. One type of box can be used multiple times.
Condition of the stacking is:
	1. The box can be placed on top of another box, iff the lower box's top surface area is strictly larger than the upper box's base area
	2. Strictly larger area is where the both length and width are higher

n = 4
height[] = {4,1,4,10}
width[] = {6,2,5,12}
length[] = {7,3,6,32}
Output: 60
Explanation: One way of placing the boxes is
as follows in the bottom to top manner:
(Denoting the boxes in (l, w, h) manner)
{ 2 , 1 , 3 }
{ 3 , 2 , 1 }
{ 5 , 4 , 6 }
{ 6 , 5 , 4 }
{ 7 , 6 , 4 }
{ 12 , 10 , 32 }
{ 32 , 12 , 10 }
Hence, the total height of this stack is
10 + 32 + 4 + 4 + 6 + 1 + 3 = 60.
No other combination of boxes produces a height
greater than this.
"""

class Box:
	def __init__(self,length,width,height):
		self.length=length
		self.width=width
		self.height=height
		self.area=length*width
	def printbox(self):
		print("{",self.length,",",self.width,",",self.height,"}")

def allBoxesWithDimensions(box):
	if box is None:
		return None
	return [Box(max(box.length,box.width),min(box.length,box.width),box.height),Box(max(box.length,box.height),min(box.length,box.height),box.width),Box(max(box.width,box.height),min(box.width,box.height),box.length)]


def stackBoxes(length,width,height):
	if length is None or width is None or height is None or len(length)!=len(width) or len(length)!=len(height):
		return None
	n=len(height)
	boxes=[]
	for i in range(n):
		boxes.append(Box(length[i],width[i],height[i]))
	boxAllType=[]
	for i in range(n):
		boxAllType.extend(allBoxesWithDimensions(boxes[i]))
	boxAllType=sorted(boxAllType,key=lambda x:x.area)[::-1]
	#for i in boxAllType:
	#	i.printbox()
	m=len(boxAllType)
	maxTillNow=[i.height for i in boxAllType]
	result=[i for i in range(m)]

	for i in range(1,m):
		for j in range(i):
			if boxAllType[i].length<boxAllType[j].length and boxAllType[i].width<boxAllType[j].width:
				maxTillNow[i]=maxTillNow[j]+boxAllType[i].height
				result[i]=j

	maxVal=max(maxTillNow)
	print("Max Value:",maxVal)
	maxIndex=maxTillNow.index(maxVal)
	i=maxIndex
	su=0
	while i!=result[i]:
		boxAllType[i].printbox()
		su+=boxAllType[i].height
		i=result[i]
	boxAllType[i].printbox()



height = [4,1,4,10]
width = [6,2,5,12]
length = [7,3,6,32]

stackBoxes(length,width,height)

height=[4,5]
width=[2,2]
length=[1,3]

stackBoxes(length,width,height)