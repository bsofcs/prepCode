#minimumJumpsToReachHomeByBug
#A certain bug's home is on the x-axis at position x. Help them get there from position 0.
#
#The bug jumps according to the following rules:
#
#It can jump exactly a positions forward (to the right).
#It can jump exactly b positions backward (to the left).
#It cannot jump backward twice in a row.
#It cannot jump to any forbidden positions.
#The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.
#
#Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i], and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home. If there is no possible sequence of jumps that lands the bug on position x, return -1.

#class Solution:
#    def __init__(self):
#        self.seen=[[]]
#    def minimumJumps(self, forbidden, a, b, x):
#        self.seen=[[]]
#        if forbidden is None or a is None or b is None or x is None:
#            return None
#        print("List:",forbidden," a:",a," b:",b," x:",x," seen:",self.seen)
#        f=self.jumps(forbidden,a,b,x,"Forward",0,0)
#        b=self.jumps(forbidden,a,b,x,"Back",0,0)
#        if (f==float("INF") and b==float("INF")):
#            return -1
#        return(b if f>b else f)
#        
#    def jumps(self,forbidden,a,b,x,step,start,jump):
#        if start==x:
#            return jump
#        if step=="Back" and (start-b<0 or (start-b) in forbidden):
#            return float("INF")
#        elif step=="Back" and start-b==x:
#            return jump+1
#        elif (step=="Forward" or step=="Back1") and (start+a<0 or (start+a) in forbidden):
#            return float("INF")
#        elif (step=="Forward" or step=="Back1") and start+a==x:
#            return jump+1
#        forward,back=float("INF"),float("INF")
#        if [start+a,"Forward"] not in self.seen and start<2000:
#            self.seen.append([start+a,"Forward"])
#            forward=self.jumps(forbidden,a,b,x,"Forward",start+a,jump+1)
#        if step=="Back" and [start-b,"Back"] not in self.seen:
#            self.seen.append([start-b,"Back"])
#            back=self.jumps(forbidden,a,b,x,"Back1",start-b,jump+1) #can go back
#        if step=="Forward" and [start-b,"Back"] not in self.seen:
#            self.seen.append([start-b,"Back"])
#            back=self.jumps(forbidden,a,b,x,"Back",start-b,jump+1) #can go back
#        return(back if forward>back else forward)



#DFS fails
# so try BFS


forbidden = [14,4,18,1,15]
a = 3
b = 15
x = 9
s=Solution()
print(s.minimumJumps(forbidden,a,b,x))
forbidden = [8,3,16,6,12,20]
a = 15
b = 13
x = 11
print(s.minimumJumps(forbidden,a,b,x))
forbidden = [1,6,2,14,5,17,4]
a = 16
b = 9
x = 7
print(s.minimumJumps(forbidden,a,b,x))
forbidden =[14,4,18,1,15]
a=3
b=15
x=9
print(s.minimumJumps(forbidden,a,b,x))
forbidden=[128,178,147,165,63,11,150,20,158,144,136]
a=61
b=170
x=135
print(s.minimumJumps(forbidden,a,b,x))