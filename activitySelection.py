"""
activitySelection
"""
#code



def activitySelection(startTime,endTime):
	path=0
	if startTime is None or endTime is None:

		return None

	activity=list(zip(startTime,endTime))
	activity=sorted(activity,key=lambda x:x[1])
	print(activity)
	pos=activity[0][1]
	path=1
	for i in range(len(activity)):
		if pos<=activity[i][0]:
			path+=1
			pos=activity[i][1]
	return path
			

"""



if __name__=='__main__':

    n=int(input("Number of Test:"))

    for i in range(n):

	m=input()
        sT=input("Start Time:")

        startTime=[int(i) for i in sT.split()]

        eT=input("End Time:")

        endTime=eT.split()

        res=activitySelection(startTime,endTime)

        print(res)

"""
sT="1 3 2 5 8 5"
startTime=[int(i) for i in sT.split()]

eT="2 4 6 7 9 9"
endTime=[int(i) for i in eT.split()]
print(activitySelection(startTime,endTime))

sT="1 3 2 5"
startTime=[int(i) for i in sT.split()]

eT="2 4 3 6"
endTime=[int(i) for i in eT.split()]

print(activitySelection(startTime,endTime))


sT="50 74 59 31 73 45 79 24"
startTime="70 75 65 44 76 73 103 32"
endTime=[int(i) for i in eT.split()]


print(activitySelection(startTime,endTime))