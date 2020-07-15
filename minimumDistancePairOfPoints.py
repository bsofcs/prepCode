"""
minimumDistancePairOfPoints
The algorithm can be explained in 3 sub-problems:
i.	Sort the points based on x-axis and find the median
ii.	Get the minimum distant pair of points in left and right as dl and dr respectively. Take d as minimum among dl and dr
iii.	Take the strip of length of d on both side of the median. length of strip=2*d. In the strip find the minimum distant paor of points ds.
Return the minimum of d and ds 
"""
import math
class Point:
	def __init__(self,x,y):
		self.x=x
		self.y=y

def dist(p1,p2):
	if p1 is None or p2 is None:
		return
	return(math.sqrt(math.pow((p1.x-p2.x),2)+math.pow((p1.y-p2.y),2)))

def BruteForce(P,n):
	if P is None or n is None:
		return
	min_val=float("INF")
	for i in range(n):
		for j in range(i+1,n):
			if dist(P[i],P[j])<min_val:
				min_val=dist(P[i],P[j])
	return min_val

def stripClosest(strip,n,d):
	if strip is None or n is None or d is None:
		return
	min_val=d
	strip.sort(key=lambda point:point.y)
	for i in range(n):
		j=i+1
		while j<n and (strip[j].y-strip[i].y)<min_val:
			min_val=dist(strip[j],strip[i])
			j+=1
	return min_val

def closestUtil(P,n):
	if P is None or n is None:
		return
	if n<=3:
		return BruteForce(P,n)
	mid=n//2
	midpoint=P[mid]
	dl=closestUtil(P[:mid],mid)
	dr=closestUtil(P[mid:],n-mid)
	d=min(dl,dr)
	strip=[]
	for i in range(n):
		if abs(P[i].x-midpoint.x)<d:
			strip.append(P[i])
	return(min(d,stripClosest(strip,len(strip),d)))

def closest(P):
	if P is None:
		return
	P.sort(key=lambda point: point.x)
	n=len(P)
	return closestUtil(P,n)

P=[Point(2,3),Point(12,30),Point(40,50),Point(5,1),Point(12,10),Point(3,4)]

print(closest(P))