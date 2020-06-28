def timeCompare(time1,time2):
 hour1,min1=time1.split(":")
 hour2,min2=time2.split(":")
 t1=hour1*60+min1
 t2=hour2*60+min2
 if t1>t2:
  return 1
 if t1<t2:
  return -1
 if t1==t2:
  return 0

def timeBetween(time1,time2):
 hour1,min1=time1.split(":")
 hour2,min2=time2.split(":")
 t1= int(hour1) *60 + int(min1)
 t2= int(hour2) *60 + int(min2)
 result=abs(t2-t1)
 return(result)  

def timeAvail(time1,time2):
 start1=time1[0]
 end1=time1[1]
 start2=time2[0]
 end2=time2[1]
 if timeCompare(start1,start2)==-1 and timeCompare(start2,end1)==-1 and timeCompare(end1,end2)==-1:
  return [start2,end1]
 if timeCompare(start1,start2)==1 and timeCompare(start1,end2)==-1 and timeCompare(end1,end2)==1:
  return [start1,end2]
 if timeCompare(start1,start2)==-1 and timeCompare(end1,end2)==1:
  return time2
 if timeCompare(start1,start2)==1 and timeCompare(end1,end2)==-1:
  return time1
 if timeCompare(start1,start2)==0 and timeCompare(end1,end2)!=0:
  return([start1,end1] if timeCompare(end1,end2)==-1 else [start1,end2])
 if timeCompare(start1,start2)!=0 and timeCompare(end1,end2)==0:
  return([start1,end1] if timeCompare(start1,start2)==1 else [start2,end1])
 if timeCompare(start1,start2)==0 and timeCompare(end1,end2)==0:
  return time1
 return None

def timeBetweenSlot(time1,time2):
 start1=time1[0]
 end1=time1[1]
 start2=time2[0]
 end2=time2[1]
 if (timeCompare(end1,start2)==-1):
   return([end1,start2])
 return None
   

def freeTimeLeft(cal,bound,duration):
 start='00:00' if bound[0] is None else bound[0]
 end='24:00' if bound[1] is None else bound[1]
 result=[]
 if timeCompare(start,cal[0][0])==-1:
  result=result.append([start,cal[0][0]])
 for i in range(len(cal)-1):
  timeBW=timeBetweenSlot(cal[i],cal[i+1])
  timeBW=timeBetween(timeBW[0],timeBW[1]) if timeBW else 0
  if timeBW>=duration:
   result.append([cal[i][1],cal[i+1][0]])
 if timeCompare(cal[-1][1],end)==-1:
  result.append([cal[-1][1],end])
 return result

def calendarBooking(cal1,bound1,cal2,bound2,duration):
 freeCal1=freeTimeLeft(cal1,bound1,duration)
 freeCal2=freeTimeLeft(cal2,bound2,duration)
 result=[]
 for time1 in freeCal1:
  for time2 in freeCal2:
   temp=timeAvail(time1,time2)
   if temp:
    if timeBetween(temp[0],temp[1])>=duration:
     result.append(temp)
 return(result)

cal1=[["09:00","10:30"],["12:00","13:00"],["16:00","18:00"]]
bound1=["09:00","20:00"]
cal2=[["10:00","11:30"],["12:30","14:30"],["14:30","15:00"],["16:00","17:00"]]
bound2=["10:00","18:30"]
duration=30
print(calendarBooking(cal1,bound1,cal2,bound2,duration))