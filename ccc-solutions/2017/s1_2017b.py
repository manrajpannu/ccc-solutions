# Problem S1: Sum Game
def sumgame(n,team1,team2):
	lol = []
	
	for i in range(n):
		
		if i > 0: 
			team1[i]+=team1[i-1]
			team2[i]+=team2[i-1]
		if team1[i] == team2[i]:
			lol.append(i+1)

	try:	
		return max(lol)
	except:
		return 0

n = int(input())
t1 = input().split()
t2 = input().split()

for i in range(len(t1)):
	t1[i] = int(t1[i])
for i in range(len(t2)):
	t2[i] = int(t2[i])

print(sumgame(n,t1,t2))

