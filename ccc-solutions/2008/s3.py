# Problem S3: Maze Game
def print_(grid):
	for x in grid:
		print(x)
	print()

def pint(dungeon, t):
	for i in t:
		dungeon[i[0]][i[1]] = 999
	print_(dungeon)


def construct_maze():
	r = int(input())
	c = int(input())
	maze = []

	for i in range(r):
		maze.append(list(input()))
	return maze

def paths(matrix, start): 
	neighbours = {'+' : [True, True, True, True], 
				  '|' : [True, False, True, False],
				  '-' : [False, True, False, True],
				  '*' : [False, False, False, False]  }


	result_value = []
	result_index = []

	ways_to_travel = neighbours[matrix[start[0]][start[1]]]

	
	if  start[0] - 1 >= 0 and ways_to_travel[0] == True:	# checks top element
		if matrix[start[0] - 1][start[1]] != '*':
			result_index.append([start[0]-1,start[1]])
			result_value.append(matrix[start[0]-1][start[1]])

	if start[1] + 1 <= len(matrix[0])-1 and ways_to_travel[1] == True:	# checks right element
		if  matrix[start[0]][start[1]+1] != '*':
			result_index.append([start[0],start[1]+1])
			result_value.append(matrix[start[0]][start[1]+1])

	if start[0] + 1 <= len(matrix)-1 and ways_to_travel[2] == True:	# checks bottom element
		if  matrix[start[0] + 1][start[1]] != '*':
			result_index.append([start[0]+1,start[1]])
			result_value.append(matrix[start[0]+1][start[1]])

	if start[1] - 1 >= 0 and ways_to_travel[3] == True:	# checks left element and if it can travel there
		if matrix[start[0]][start[1]-1] != '*':
			result_index.append([start[0],start[1]-1])
			result_value.append(matrix[start[0]][start[1]-1])

	return result_index

def print_maze(maze,point):
	maze[point[0]][point[1]] = '0'
	for i in maze:
		print(i)


def BFS(graph):
	start = [0,0]
	end = [len(graph)-1,len(graph[0])-1]
	
	# lists
	queue   = []
	visited = []

	# track moves taken
	move_count = 0
	nodes_left_in_layer = 1
	nodes_in_next_layer = 0



	queue.append(start)
	visited.append(start)

	while queue:
		v = queue.pop(0)

		
		possible_paths = paths(graph, v)
		for i in range(len(possible_paths)):
			if possible_paths[i] not in visited:
				nodes_in_next_layer+=1
				queue.append(possible_paths[i])
				visited.append(possible_paths[i])
		nodes_left_in_layer-=1
		if nodes_left_in_layer==0:
			move_count+=1
			nodes_left_in_layer = nodes_in_next_layer
			nodes_in_next_layer = 0		

		if end ==v:
				return move_count
	
	
	return -1



output = []
for i in range(int(input())):
	output.append(BFS(construct_maze()))

for i in output:
	print(i)



