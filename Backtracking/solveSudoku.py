"""
solveSudoku
Given a incomplete Sudoku i.e. a matrix 3X3 where each element is a 3X3 matrix, so basically a 9X9 matrix
Condition of a full Sudoku:
	1. Needs to filled with number 1 to 9
	2. No columns or rows will have any numbers repeating
	3. No smaller box will have any numbers repeating
"""
def solve_sudoku(grid):
	if grid is None:
		return None
	n=len(grid)
	l=[0,0]
	if not find_empty_location(grid,l):
		return True
	row,col=l[0],l[1]
	for num in range(1,10):
		if check_location_is_safe(grid,row,col,num):
			grid[row][col]=num
			if solve_sudoku(grid): return True
			grid[row][col]=0
	return False

def check_location_is_safe(arr,row,col,num):
	return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3, col - col % 3, num)  

def find_empty_location(arr,l):
	for row in range(9):
		for col in range(9):
			if arr[row][col]==0:
				l[0],l[1]=row,col
				return True
	return False

def used_in_row(arr,row,num):
	for i in range(9):
		if arr[row][i]==num:
			return True
	return False

def used_in_col(arr,col,num):
	for i in range(9):
		if arr[i][col]==num:
			return True
	return False

def used_in_box(arr,row,col,num):
	for i in range(3):
		for j in range(3):
			if arr[i+row][j+col]==num:
				return True
	return False

def printGrid(grid):
	print()
	for i in range(9):
		a="-" if i%3 else "="
		print(a*38)
		for j in range(9):
			c=" | " if (j+1)%3 else " || "
			print(grid[i][j],end=c)
		print()
	print("="*38)

grid=[
[3, 0, 6, 5, 0, 8, 4, 0, 0],
[5, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 8, 7, 0, 0, 0, 0, 3, 1],
[0, 0, 3, 0, 1, 0, 0, 8, 0],
[9, 0, 0, 8, 6, 3, 0, 0, 5],
[0, 5, 0, 0, 9, 0, 6, 0, 0],
[1, 3, 0, 0, 0, 0, 2, 5, 0],
[0, 0, 0, 0, 0, 0, 0, 7, 4],
[0, 0, 5, 2, 0, 6, 3, 0, 0]
]
n=len(grid)
printGrid(grid)
print("\nAnswer:")
if solve_sudoku(grid):
	printGrid(grid)
else:
	print("No solution")