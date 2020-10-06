"""
railwayPlatformNeeded
Given a set of trains' schedule with arrival and departure time.
ind the number of platforms needed for the railway station.
Example: i'th Train will have Arrival[i] and Departure[i]
Arrival:[900,940,950,1100,1500,1800]
Departure:[910,1200,1120,1130,1900,2000]
"""

def railwayPlatformNeeded(arr,dept):
	if arr is None or dept is None:
		return None
	arr.sort()
	dept.sort()
	n=len(arr)
	i=1;j=0
	numOfPlatform=1	#which is bare minimum
	maxPlat=1	#bare maximum at first arrival
	while i<n:
		if arr[i]<dept[j]:
			maxPlat+=1
			numOfPlatform=max(numOfPlatform,maxPlat)
			i+=1
		else:
			maxPlat-=1
			j+=1
	return numOfPlatform

def railwayPlatformNeededBF(arr,dept):
	if arr is None or dept is None:
		return None
	n=len(arr)
	plat=1
	for i in range(n):
		tmp=1
		for j in range(i+1,n):
			if arr[j] in range(arr[i],dept[i]+1) or dept[j] in range(arr[i],dept[i]+1):
				tmp+=1
		plat=max(plat,tmp)
	return plat

arr=[900,940,950,1100,1500,1800]
dept=[910,1200,1120,1130,1900,2000]
print(railwayPlatformNeeded(arr,dept))
print(railwayPlatformNeededBF(arr,dept))