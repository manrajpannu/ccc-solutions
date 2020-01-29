# Problem S2: High Tide, Low Tide

def low_high_finder(tides):
	length = len(tides)
	high_tides = []
	low_tides  = []
	while tides:
		print(high)
		if tides:
			low_tides.append(min(tides))
			tides.remove(min(tides))
		if tides:
			high_tides.append(max(tides))
			tides.remove(max(tides))
		if len(tides) == 1:
			low_tides.append(tides.pop())

	return high_tides,low_tides


amount = int(input())
data = list(map(int, input().split()))

grouped_tides = low_high_finder(data)
highest_tides = grouped_tides[0]
lowest_tides = grouped_tides[1]

output = []
for i in range(max(len(highest_tides),len(lowest_tides))):
	if lowest_tides:
		output.append(lowest_tides.pop())
	if highest_tides:
		output.append(highest_tides.pop())
print(*output, sep =' ')



