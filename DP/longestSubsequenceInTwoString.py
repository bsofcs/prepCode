"""
longestSubsequenceInTwoString
"""
def longestSubsequenceInTwoString(arr1,arr2):
	if arr1 is None or arr2 is None:
		return None
	Table=[[0 for _ in range(len(arr2)+1)] for _ in range(len(arr1)+1)]
	for i,x in enumerate(arr1):
		for j,y in enumerate(arr2):
			if x==y:
				Table[i+1][j+1]=Table[i][j]+1
			else:
				Table[i+1][j+1]=max(Table[i+1][j],Table[i][j+1])
	result=""
	x=len(arr1);y=len(arr2)
	while x!=0 and y!=0:
		if Table[x][y]==Table[x-1][y]:
			print("from (",x,",",y,") to (",x-1,",",y,")")
			x-=1
		elif Table[x][y]==Table[x][y-1]:
			print("from (",x,",",y,") to (",x,",",y-1,")")
			y-=1
		else:
			print("from (",x,",",y,") to (",x-1,",",y-1,")")
			assert arr1[x-1]==arr2[y-1]
			result=arr1[x-1]+result
			x-=1;y-=1
	for i in range(len(Table)):
		print(Table[i])
	return result

if __name__=='__main__':
	arr1=input("The first string=>")
	arr2=input("The second string=>")
	print(longestSubsequenceInTwoString(arr1,arr2))