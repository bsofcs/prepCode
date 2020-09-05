"""
petrolPumpTour
"""
class PetrolPump:
	def __init__(self,petrol,distance):
		self.petrol=petrol
		self.distance=distance

def printTour(arr):
	n=len(arr)
	if n==0:
		return
	start,end=0,1
	curr_petrol=arr[start].petrol-arr[start].distance
	while end!=start or curr_petrol<0:
		while curr_petrol<0 and start!=end:
			curr_petrol-=arr[start].petrol-arr[start].distance
			start=(start+1)%n
			if start==0:
				return -1
		curr_petrol+=arr[end].petrol-arr[end].distance
		end=(end+1)%n
	return start

def can_complete_tour(arr):
	minVal=float("INF")
	minPos=-1
	n=len(arr)
	petrolTillNow=0
	for i in range(n):
		petrolTillNow+=arr[i].petrol-arr[i].distance
		if petrolTillNow<minVal:
			minVal=petrolTillNow
			minPos=i
	if petrolTillNow>=0:
		return (minPos+1)%n
	return -1

def circularTour(arr):
	n=len(arr)
	if n==0:
		return None
	start=0
	minVal=float("INF")
	petrolTillNow=0
	for i in range(n):
		petrolTillNow+=arr[i].petrol-arr[i].distance
		if petrolTillNow<0:
			if petrolTillNow<minVal:
				minVal=petrolTillNow
			petrolTillNow=0
			start=i+1
	if start==0:
		return start
	elif petrolTillNow-minVal>=0:
		return start
	else:
		return -1	
petrol=[4,6,7,4]
distance=[6,5,3,5]
city=[]
n=len(petrol)
for i in range(n):
	city.append(PetrolPump(petrol[i],distance[i]))
print(printTour(city))
print(can_complete_tour(city))
print(circularTour(city))