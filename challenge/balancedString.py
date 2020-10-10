"""
balancedString
"""
import sys
def firstNonRepeating(arr,t):
	if t=="0":
		return None
	if not arr:
		arr.append(t)
		return arr[0]
	elif t in arr:
		arr.pop(arr.index(t))
		return -1 if len(arr)==0 else arr[0]
	else:
		arr.append(t)
		return arr[0]

if __name__=="__main__":
	arr=[]
	while True:
		t=input()[0]
		if not t:
			continue
		ans=firstNonRepeating(arr,t)
		if ans:
			print(ans)
		else:
			break
	print("Thanks",arr)