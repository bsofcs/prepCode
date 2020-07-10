"""
meetingRoomSelection
"""
def meetingRoomSelection(schedules):
	print(schedules)
	schedules=sorted(schedules,key=lambda x:x[1])
	result=[schedules[0][2]]
	pos=schedules[0][1]
	for i in range(len(schedules)):
		if pos<=schedules[i][0]:
			result.append(schedules[i][2])
			pos=schedules[i][1]
	return result

if __name__=='__main__':
	n=int(input())
	for i in range(n):
		noOfMeetings=int(input())
		st=input()
		startTime=[int(i) for i in st.split()]
		et=input()
		endTime=[int(i) for i in et.split()]
		code=[i+1 for i in range(noOfMeetings)]
		schedules=list(zip(startTime,endTime,code))
		result=meetingRoomSelection(schedules)
		for i in result:
			print(i,end=" ")
		print()