"""
assisstMiceToHoles
There are N Mice and N holes are placed in a straight line. Each hole can accommodate only 1 mouse. A mouse can stay at his position, move one step right from x to x + 1, or move one step left from x to x -1. Any of these moves consumes 1 minute. Assign mice to holes so that the time when the last mouse gets inside a hole is minimized
https://www.geeksforgeeks.org/assign-mice-holes/
"""

mice=[-10, -79, -79, 67, 93, -85, -28, -94]
holes=[-2, 9, 69, 25, -31, 23, 50, 78]
res=[abs(mice[i]-holes[i]) for i in range(len(mice))]
print(res,max(res))