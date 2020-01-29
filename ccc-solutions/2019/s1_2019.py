# Problem J4/S1: Flipper
# Manraj Pannu
# 593368
# ICS4U0
# 6 sep 2018
# Password : Toxsikoz123

def horizontal(grid):
	grid[0], grid[1] = grid[1], grid[0]
	return grid

def vertical(grid):
	grid[0][0], grid[0][1] = grid[0][1], grid[0][0]
	grid[1][0], grid[1][1] = grid[1][1], grid[1][0]
	return grid

grid = [
	[1,2],
	[3,4]
	]

for letter in str(input()):
	if letter == "V":
		grid = vertical(grid)
	if letter == "H":
		grid = horizontal(grid)

for row in grid:
	print(*row, sep =' ')
