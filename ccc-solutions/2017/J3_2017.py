#Problem J3: Exactly Electrical

start = input().split()
end = input().split()
energy = int(input())
distance = []
for i in range(2):
	distance.append(abs(int(start[i]) - int(end[i])))

distance = distance[0] + distance[1]
if distance <= energy and (energy - distance) % 2 == 0: print("Y")
else: print("N")