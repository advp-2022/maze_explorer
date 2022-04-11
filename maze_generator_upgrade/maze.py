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

def add_start_end_positions(starting_position,ending_position,maze):
	"""
	The user can manually enter the start and end points by placing
	each of them in a list or by calling the method
	"random_point(width,hight)" to randomly create the points

	output example:

	maze = add_start_end_positions(random_point(width,hight),random_point(width,hight),maze)
	@  @  @  @  @  @  @  @  @  @  
	@  @  @  @  0  @  @  @  @  @  
	@  @  @  @  @  @  @  @  @  @  
	@  @  @  @  @  @  @  @  @  @  
	@  @  @  @  @  @  @  @  @  @  
	@  @  @  @  @  @  @  @  @  @  
	@  @  @  @  @  @  @  @  @  @  
	@  @  @  @  @  @  @  @  @  @  
	@  @  @  @  @  u  @  @  @  @  
	@  @  @  @  @  @  @  @  @  @  

	"""
	maze[starting_position[0]][starting_position[1]] = path
	maze[ending_position[0]][ending_position[1]] = end
	return maze

maze = add_start_end_positions(random_point(width,hight),random_point(width,hight),maze)

#--------------------------------------------------------------

def count_the_surrounding_walls(i,j,maze):
	"""
	this method for counting the surrounding walls around the cell

	output example:

	count = count_the_surrounding_walls(i,j,maze)
	count = 4
	"""
	count = 0
	if (maze[i-1][j]==wall):
		count = count + 1
	if (maze[i+1][j]==wall):
		count = count + 1
	if (maze[i][j+1]==wall):
		count = count + 1
	if (maze[i][j-1]==wall):
		count = count + 1
	return count

#--------------------------------------------------------------

"""
for printing the maze as 2D array.
"""

for i in range(10):
	for j in range(10):
		print(maze[i][j],end="  ")
	print()