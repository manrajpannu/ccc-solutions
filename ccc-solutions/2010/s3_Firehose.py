#j4 fire hose
# houses = []
# for i in range(int(input())):
# 	houses.append(int(input()))

def average(l):
	return round(sum(l)/len(l))

def difference_finder(s):
	difference = []

	for i in range(len(s)-1):
		difference.append(int(s[i+1]) - int(s[i]))
	return difference


def fire_hydrant(houses, hydrants):


	if hydrants == 1:
		return average([houses[0],houses[-1]])


	else: 
		diff = difference_finder(houses)
		print(diff)
		pop = max(difference_finder(houses))
	
		if diff.index(pop) == len(diff)-1:
			houses.pop(diff.index(pop)+1)
		else: houses.pop(diff.index(pop))

		result = fire_hydrant(houses, hydrants-1)

	return max(houses) - result 


print(fire_hydrant([0, 240000, 292000,448000, 500000, 740000],2))







