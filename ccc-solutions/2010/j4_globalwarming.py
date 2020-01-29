#Problem J4: Global Warming
temperature_data = input().split()

def difference_finder(s):
	difference = []
	for i in range(len(s)-1):
		difference.append(int(s[i+1]) - int(s[i]))

	return difference

def sequence_finder(list_seq):
	sequence = []
	for i in range(len(list_seq)):
		for x in range(i+1, len(list_seq) + 1):
			sequence.append(list_seq[i])
			for i in range(len(sequence)):
				if sequence[i] != list_seq[x]:
					sequence.append(list_seq[x])


print(difference_finder(input().split()))
# print(sequence_finder(difference_finder(temperature_data)))