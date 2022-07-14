import random

width = 10
hight = 10
wall = '@'
path = 0
start = 'S'
end = 'E'
maze = []

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
	for i in range(hight):
		line = []
		for j in range(width):
			line.append(wall)
		maze.append(line)
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
	starting_row = random.randint(1,hight-2)
	starting_col = random.randint(1,width-2)
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
	maze[starting_position[0]][starting_position[1]] = start
	maze[ending_position[0]][ending_position[1]] = end
	return maze

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

def check_next_step(width, hight, i, j, maze):
	
	if (i == 1 and j != width-1):
		if (maze[i+1][j] == wall):
			if (maze[i][j+1] == wall):
				point = random.randint(1,2)
				if (point == 1):
					maze[i+1][j] = path
				else:
					maze[i][j+1] = path

	if (i == 1 and j == width-1):
		if (maze[i+1][j] == wall):
			if (maze[i][j-1] == wall):
				point = random.randint(1,2)
				if (point == 1):
					maze[i+1][j] = path
				else:
					maze[i][j-1] = path
	
	#            Error
	#            -----
	#
	# if (i >= 2 and j != width-1):
	# 	if (maze[i-1][j] == wall):
	# 		if (maze[i+1][j] == wall):
	# 			if (maze[i][j+1] == wall):
	# 				point = random.randint(1,2)
	# 				if (point == 1):
	# 					maze[i-1][j] = path
	# 				else:
	# 					maze[i][j+1] = path	

	if (i >= 2 and j == width-1):
		if (maze[i-1][j] == wall):
			if (maze[i+1][j] == wall):
				if (maze[i][j-1] == wall):
					point = random.randint(1,2)
					if (point == 1):
						maze[i-1][j] = path
					else:
						maze[i][j-1] = path	

	return maze

#--------------------------------------------------------------

def creating_path(width,hight,maze):
	i = 1
	while (i < hight-1):
		j = 1
		while (j < width-1):
			if (i < hight-2 and j < width-2):
				point = random.randint(1,2)
				if (point == 1):
					maze[i+1][j] = path	
				elif (point == 2):
					maze[i][j+1] = path

			elif(i == hight-1 and j < width-2):
				point = random.randint(1,4)
				if (point == 1):
					maze[i-1][j] = path
				elif (point == 2):
					maze[i][j+1] = path

			elif(i < hight-2 and j == width-1):
				point = random.randint(1,4)
				if (point == 1):
					maze[i+1][j] = path
				elif (point == 2):
					maze[i][j-1] = path

			elif(i == hight-1 and j == width-1):
				point = random.randint(1,3)
				if (point == 1):
					maze[i-1][j] = path
				elif (point == 2):
					maze[i][j-1] = path

			j = j + 1
		i = i + 1

	return maze

maze = creating_path(width,hight,maze)
maze = add_start_end_positions(random_point(width,hight),random_point(width,hight),maze)

#--------------------------------------------------------------


def solve_path_problems(width,hight,maze):
	"""
	"""
	for x in range(hight):
		i = 1
		while (i < hight-1):
			j = 1
			while (j < width-1):
				if (maze[i][j] == path or maze[i][j] == start or maze[i][j] == end):
					maze = check_next_step(width, hight, i, j, maze)
				j = j + 1
			i = i + 1

	return maze

maze = solve_path_problems(width,hight,maze)

#--------------------------------------------------------------
"""
for printing the maze as 2D array.
"""

for i in range(hight):
	for j in range(width):
		print(maze[i][j],end="  ")
	print()

