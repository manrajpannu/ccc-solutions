# Problem S2: High Tide, Low Tide

def low_high_finder(tides):
	high_tide = []
	low_tide  = []
	while tides:
		if tides:
			low_tide.append(min(tides))
			tides.remove(min(tides))
		
		if tides:
			high_tide.append(max(tides))
			tides.remove(max(tides))
	
		if len(tides) == 1:
			low_tide.append(tides.pop())
		
	return (high_tide),(low_tide)



amount = int(input())
data = low_high_finder(list(map(int, input().split())))

out = []
for i in range(amount):
	if data[1]:
		out.append(data[1][-1])
		data[1].pop()
	if data[0]:
		out.append(data[0][-1])
		data[0].pop()

print(*out, sep =' ')



