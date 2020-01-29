#row = int(input())
#col = int(input())

#array = [[0] * col for i in range(row)]



matrix = [
    [0,1,2,3,4],
    [5,6,6,8,9],
    [1,1,2,3,4],
    [5,6,7,8,9],
    [2,2,2,3,4]
]

def rotate(matrix):
    size = len(matrix)
    layer_count = size // 2

    for layer in range(0, layer_count):
        first = layer
        last = size - first - 1

        for element in range(first, last):
            offset = element - first

            top = matrix[first][element]
            right_side = matrix[element][last]
            bottom = matrix[last][last-offset]
            left_side = matrix[last-offset][first]

            matrix[first][element] = left_side
            matrix[element][last] = top
            matrix[last][last-offset] = right_side
            matrix[last-offset][first] = bottom

def print_matrix(matrix):
	for row in matrix:
		print(row)


for i in range(4):
	print_matrix(matrix)
	print("\n")
	rotate(matrix)
