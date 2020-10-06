"""
rainWaterTapping
1. Try1 and Try2 are both the same algo	: T=O(n**2) S=O(n)
2. OS: using optimal way than that of Try1 and Try2: T=O(n) S=O(1)
"""
def rainWaterTappingTry1(arr):
	if arr is None:
		return
	n=len(arr)
	if n<3:
		return 0
	l2r=[i for i in arr]
	r2l=[i for i in arr]
	res=[0]*n
	for i in range(1,n-1):
		l2r[i]=max(arr[i+1:])
		if arr[i]>l2r[i]:
			l2r[i]=arr[i]
	for i in range(n-2,0,-1):
		r2l[i]=max(arr[:i])
		if arr[i]>r2l[i]:
			r2l[i]=arr[i]
		tmp=min(l2r[i],r2l[i])-arr[i]
		res[i]=tmp if tmp>0 else 0
	#print(l2r,"\n",r2l,"\n",res)
	return sum(res)

def rainWaterTappingTry2(arr):
	if arr is None:
		return
	n=len(arr)
	if n<3:
		return 0	
	left=[0]*n
	right=[0]*n
	left[0]=arr[0]
	for i in range(1,n):
		left[i]=max(left[i-1],arr[i])
	right[n-1]=arr[n-1]
	for i in range(n-2,-1,-1):
		right[i]=max(right[i+1],arr[i])
	water=0
	#print(left,"\n",right)
	for i in range(n):
		water+=min(left[i],right[i])-arr[i]
	return water

def rainWaterTappingOS(arr):
	if arr is None:
		return
	n=len(arr)
	if n<3:
		return 0
	result=0
	left_max=0
	right_max=0
	lo=0
	hi=n-1
	while lo<=hi:
		#print(arr[lo],arr[hi],left_max,right_max)
		if arr[lo]<arr[hi]:
			if arr[lo]>left_max:
				left_max=arr[lo]
			else:
				result+=left_max-arr[lo]
			lo+=1
		else:
			if arr[hi]>right_max:
				right_max=arr[hi]
			else:
				result+=right_max-arr[hi]
			hi-=1
		#print(arr[lo],arr[hi],left_max,right_max,result)
	return result
arr=[3,0,0,2,0,4]
print(rainWaterTappingTry1(arr))
print(rainWaterTappingTry2(arr))
print(rainWaterTappingOS(arr))
arr=[6,9,6]
print(rainWaterTappingTry1(arr))
print(rainWaterTappingTry2(arr))
print(rainWaterTappingOS(arr))
arr=[7,4,0,9]
print(rainWaterTappingTry1(arr))
print(rainWaterTappingTry2(arr))
print(rainWaterTappingOS(arr))
arr=[2,5,0,9,6,3,3,5]
print(rainWaterTappingTry1(arr))
print(rainWaterTappingTry2(arr))
print(rainWaterTappingOS(arr))