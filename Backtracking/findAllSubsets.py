"""
findAllSubsets
Give a array that may contain the 
"""
def findAllSubsets(arr):
	if arr is None:
		return
	n=len(arr)
	for i in range(1<<n):
		tmp=list(bin(i).replace("0b",""))[::-1]
		print("(",end=" ")
		for j in range(len(tmp)):
			if tmp[j]=="1":
				print(arr[j],end=" ")
		print(")")
	print()

arr=[1,2,2,4,5]
findAllSubsets(arr)