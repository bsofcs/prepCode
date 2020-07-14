"""
relativeSorting

Given two arrays A1[] and A2[] of size N and M respectively. The task is to sort A1 in such a way that the relative order among the elements will be same as those in A2. For the elements not present in A2, append them at last in sorted order. It is also given that the number of elements in A2[] are smaller than or equal to number of elements in A1[] and A2[] has all distinct elements.
Note: Expected time complexity is O(N log(N)).

Input:
First line of input contains number of testcases. For each testcase, first line of input contains length of arrays N and M and next two line contains N and M elements respectively.

Output:
Print the relatively sorted array.
"""

if __name__=='__main__':
	for _ in range(int(input())):
		nm=list(map(int,input().rstrip().split()))
		n,m=nm[0],nm[1]
		ln=list(map(int,input().rstrip().split()))
		lm=list(map(int,input().rstrip().split()))
		dic=dict()
		result=[]
		for i in range(n):
			if ln[i] not in dic.keys():
				dic[ln[i]]=1
			else:
				dic[ln[i]]+=1
		for i in range(m):
			temp=[lm[i]]*dic[lm[i]]
			result.extend(temp)
			dic.pop(lm[i])
		print(result)
		print(dic)
		temp=list(dic.keys())
		temp.sort()
		for i in temp:
			result.extend([i]*dic[i])
		print(result)