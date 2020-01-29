# Problem S2: High Tide, Low Tide

amount = int(input())
data = input().split()

def integerlist(lists):
	for i in range(len(lists)):
		lists[i] = int(lists[i])
	return lists

data = sorted(integerlist(data))
data_lower = sorted(data[:int(amount/2)], reverse=True)
data_upper = data[int(amount/2):]

complete_data = []
counter= 0
while len(complete_data) != amount:

	if len(data_lower) != counter:
		complete_data.append(data_lower[counter])
	if len(data_upper) != counter:
		complete_data.append(data_upper[counter])
	counter+=1

print(*complete_data, sep =' ')