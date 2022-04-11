import random

width = 10
hight = 10
wall = '@'
path = '0'
end = 'u'
maze = [[None] * (hight) for _ in range(width)]

def predefined_maze():
	maze = [[1,2,3,4,5],
			[1,2,3,4,5],
			[1,2,3,4,5],
			[1,2,3,4,5],
			[1,2,3,4,5]]
	return maze

#--------------------------------------------------------------

def create_maze_walls_only(width,hight):
	"""
	create the walls around the maze
	put unvisited 'u' inside the maze
	if the self.width is 10 and the hight is 10

	output example:

	maze = create_maze_walls_only(width,hight)
	@  @  @  @  @  @  @  @  @  @ 
	@  @  @  @  @  @  @  @  @  @ 
	@  @  @  @  @  @  @  @  @  @ 
	@  @  @  @  @  @  @  @  @  @ 
	@  @  @  @  @  @  @  @  @  @ 
	@  @  @  @  @  @  @  @  @  @ 
	@  @  @  @  @  @  @  @  @  @ 
	@  @  @  @  @  @  @  @  @  @ 
	@  @  @  @  @  @  @  @  @  @ 
	@  @  @  @  @  @  @  @  @  @
	      
	"""
	for i in range(width):
		for j in range(hight):
			maze[i][j] = wall
	return maze


maze = create_maze_walls_only(width,hight)

#--------------------------------------------------------------

def random_point(width,hight):
	"""
	this method should return a random starting or ending point
	
	output example:

	position = random_point(width,hight)
	position [2,5]
	"""
	w = width-2
	h = hight-2
	starting_row = random.randint(1,w)
	starting_col = random.randint(1,h)
	position = [starting_row,starting_col]
	return position

#--------------------------------------------------------------

"""
for printing the maze as 2D array.
"""

for i in range(10):
	for j in range(10):
		print(maze[i][j],end="  ")
	print()