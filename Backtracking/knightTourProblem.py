"""
knightTourProblem
"""
def knightTourProblem(n,start_x,start_y):
	if n is None:
		return None
	board=[[-1 for i in range(n)] for i in range(n)]
	move_x=[1,2,2,1,-1,-2,-2,-1]
	move_y=[-2,-1,1,2,2,1,-1,-2]
	board[start_x][start_y]=0
	res=KTUtil(n,board,start_x,start_y,move_x,move_y,1)
	if res:
		for i in range(n):
			print(board[i])
	else:
		print("Tour not possible")

def KTUtil(n,board,start_x,start_y,move_x,move_y,pos):
	#print(start_x,start_y,pos)
	if pos==n**2:
		return True
	for i in range(8):
		xx=start_x+move_x[i]
		yy=start_y+move_y[i]
		if isSafe(n,board,xx,yy):
			board[xx][yy]=pos
			if KTUtil(n,board,xx,yy,move_x,move_y,pos+1):
				return True
			board[xx][yy]=-1
	return False

def isSafe(n,board,x,y):
	if x<0 or y<0 or x>=n or y>=n or board[x][y]!=-1:
		return False
	return True

start_x,start_y=0,0
knightTourProblem(7,start_x,start_y)