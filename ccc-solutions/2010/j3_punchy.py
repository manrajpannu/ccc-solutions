A = 0
B = 0
stop = 0

while stop != 7:
	input_command = input().split(' ')

	if int(input_command[0]) == 1:
		if input_command[1] == 'A': A = int(input_command[2])

		if input_command[1] == 'B': B = int(input_command[2])

	if int(input_command[0]) == 2:
                                                                                             
		if input_command[1] == 'A': print(A)

		if input_command[1] == 'B': print(B)

	if int(input_command[0]) == 3: A = eval(input_command[1]) + eval(input_command[2])

	if int(input_command[0]) == 4: A = eval(input_command[1]) + eval(input_command[2])

	if int(input_command[0]) == 5: A = eval(input_command[1]) - eval(input_command[2])
	
	if int(input_command[0]) == 6: A = eval(input_command[1]) // eval(input_command[2])

	if int(input_command[0]) == 7: stop = 7 


	input_command = 0

