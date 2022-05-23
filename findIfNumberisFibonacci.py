#findIfNumberisFibonacci
#Get the nth number in the fibonacci sequence given n
#Alternatively given a number F, print out whether it's a fibonacci number and what the closest index n in the
#fibonacci sequence is.
import math

def printFibonacci(n):
	if n<0:
		return
	if n==1:
		return [0]
	if n==2:
		return [0,1]
	result=[0,1]
	count=2
	for i in range(2,n):
		result.append(result[i-1]+result[i-2])
	return result

def isPerfectSquare(n):
    s=int(math.sqrt(n))
    return s*s==n

def isFibonacci(F):
    return isPerfectSquare(5*F*F + 4) or isPerfectSquare(5*F*F - 4)

def nearestFibonacci(F):
    if isFibonacci(F):
        return F
    c=1
    while True:
        l=F-c
        if isFibonacci(l):
            return l
        h=F+c
        if isFibonacci(h):
            return h
        c+=1

if __name__=="__main__":
	n,F=15,15
	arr=printFibonacci(n)
	print(arr)
	if (isFibonacci(F) == True):
		print(F,"is a Fibonacci Number")
	else:
		print(F,"is a not Fibonacci Number and the nearest Fibonacci number is:",nearestFibonacci(F))