"""
printPrime
Given three numbers sum S, prime P and N, find all N prime numbers after prime P such that their sum is equal to S
"""
import math
def isPrime(x):
	if x is None:
		return
	n=math.sqrt(x)
	for i in range(2,int(n)):
		if x%i==0:
			return False
	return True

prime,se=[],[]
def primeSum(total,N,S,index):
	global prime,se
	if None in (total,N,S,index):
		return
	if total==S and len(se)==N:
		display()
		return
	if total>S or index==len(prime):
		return
	se.append(prime[index])
	primeSum(total+prime[index],N,S,index+1)
	se.pop()
	primeSum(total,N,S,index+1)

def display():
	global prime,se
	length=len(se)
	for i in range(length):
		print(se[i],end=" ")
	print()

def primeAll(S,P,N):
	global prime,se
	if None in (S,P,N):
		return
	for i in range(P+1,S+1):
		if isPrime(i):
			prime.append(i)
	if len(prime)<N:
		return
	primeSum(0,N,S,0)

S,N,P=54,2,3
primeAll(S,P,N)