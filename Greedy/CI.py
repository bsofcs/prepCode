arr=[3, 1, 41, 52, 15, 4, 1, 63, 12]
arr.sort()
r=-20
s=0
n=len(arr)
for i in range(n-1,-1,-1):
	t=n-1-i
	d=(1+r/100)**t
	s+=arr[i]*d
print(s)