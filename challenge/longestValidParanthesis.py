"""
longestValidParanthesis
"""
class Stack:
	def __init__(self):
		self.stk=[]
		self.n=-1
	def push(self,val):
		self.stk.append(val)
		self.n+=1
	def pop(self):
		if self.stk:
			self.n-=1
			return self.stk.pop()
		else:
			return -1
	def peep(self):
		if self.n>0:
			return self.stk[self.n-1] 

def longestValidParanthesis(str):
	if str is None:
		return None
	n=len(str)
	s=Stack()
	res=0
	s.push(-1)
	for i in range(n):
		print(s.stk,i,res)
		if str[i]=="(":
			s.push(i)
		else:
			s.pop()
			if len(s.stk):
				res=max(res,i-s.stk[len(s.stk)-1])
			else:
				s.push(i)
	return res

arr=["()(())(","()","(",")))(((","(((",")))",")()()(",")"]
for str in arr:
	print(str)
	print(longestValidParanthesis(list(str)))