min_n = int(input())
max_n = int(input())

cube_list = []
result = 0
for i in range(round(min_n**(1/3)), round(max_n**(1/3)+2)):
	cube_list.append(i**3)

result_list = []
for i in cube_list:
	if (i ** (1/2)) == round(i ** (1/2)):
		result_list.append(i)
		result += 1
print(result_list)
print(result)
