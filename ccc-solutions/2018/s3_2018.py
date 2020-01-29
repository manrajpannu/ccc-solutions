# CCC '18 S3 - RoboThieves by Manraj Pannu



grid  = [['W', 'W', 'W', 'W', 'W'],
		 ['W', '.', 'W', '.', 'W'],
		 ['W', 'W', 'S', '.', 'W'],
		 ['W', 'W', '.', 'W', 'W']]


def find_start(matrix):
	for sublist in matrix:
		if 'S' in sublist:
			return [matrix.index(sublist),sublist.index('S')]

def find_neighbours(matrix, start): 
	result_value = []
	result_index = []
	# Creates a list of all the neighbour's indexes
	result_index.append([start[0]-1,start[1]])
	result_index.append([start[0],start[1]+1])
	result_index.append([start[0]+1,start[1]])
	result_index.append([start[0],start[1]-1])

	# Creates a list of the neighbour's elements
	result_value.append(matrix[start[0]-1][start[1]])
	result_value.append(matrix[start[0]][start[1]+1])
	result_value.append(matrix[start[0]+1][start[1]])
	result_value.append(matrix[start[0]][start[1]-1])
	return [result_value,result_index]


def find_routes(matrix, start, visited):
	neighbours = find_neighbours(matrix,start)
	neighbours_index = neighbours[1]
	neighbours_value = neighbours[0]
	#print(find_neighbours(matrix, start))
	#print(neighbours_value,start)
	for cell in neighbours_value:
		if start not in visited and cell == '.':
			print(visited)
			visited.append(start)
			find_routes(matrix, neighbours_index[neighbours_value.index(cell)], visited)
	return visited

	
	

visited = []
print(find_routes(grid, find_start(grid), visited))

