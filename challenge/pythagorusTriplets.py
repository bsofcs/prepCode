"""
pythagorusTriplets

Check if there is any pythagorus Triplet in an array.
"""
def pythagorusTriplets(arr):
	if arr is None:
		return None
	arr.sort()
	n=len(arr)
	arr1=[arr[i]**2 for i in range(n)]
	for i in range(n-1,1,-1):
		j=0
		k=i-1
		while j<k:
			if arr1[i]==(arr1[j]+arr1[k]):
				print(f"{arr[i]},{arr[j]},{arr[k]}")
				return True
			elif arr1[i]>(arr1[j]+arr1[k]):
				j+=1
			else:
				k-=1
	return False

arr=[1,4,2,5,3]
print(pythagorusTriplets(arr))