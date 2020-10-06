"""
JumpingNumbers
https://practice.geeksforgeeks.org/problems/jumping-numbers/0
"""
class Queue:
	def __init__(self):
		self.lst=[]
	def is_empty(self):
		return self.lst==[]
	def enqueue(self,val):
		self.lst.append(val)
	def dequeue(self):
		return self.lst.pop(0)

def isJumping(n):
	while n:
		prev=n%10
		n=n//10
		tmp=n%10
		if tmp==0 and n==0:
			return True
		elif abs(tmp-prev)==1:
			continue
		else:
			return False

def JumpingNumbersTry1(N):
	res=[]

	for i in range(N+1):
		if isJumping(i):

			res.append(i)

	res=" ".join(map(str,res))
	print(res)

def JumpUtil(x,num):
	#uses BFS method i.e. using queue and it can be done in DFS as well
	q=Queue()
	q.enqueue(num)
	res=[]
	while not q.is_empty():
		num=q.dequeue()
		if num<=x:
			res.append(num)
			last_dig=num%10
			if last_dig==0:
				q.enqueue((num*10)+(last_dig+1))
			elif last_dig==9:
				q.enqueue((num*10)+(last_dig-1))
			else:
				q.enqueue((num*10)+(last_dig-1))
				q.enqueue((num*10)+(last_dig+1))
	return res

def JumpingNumbers(N):
	if N is None:
		return None
	res=[0]
	for i in range(1,10):
		res.extend(JumpUtil(N,i))
	print(res)
N=500
print(JumpingNumbersTry1(N))
print(JumpingNumbers(N))