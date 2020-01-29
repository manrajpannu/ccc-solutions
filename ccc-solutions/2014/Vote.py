# Vote
# Manraj Pannu
# 593368
# ICS3U0A
# 20 Nov 2018
amount = int(input())
vote = input().upper()
Count = 0  
votes = 0	

if amount != len(vote):
	quit()
for i in vote: 

	if (i == 'A'): 
		Count+=1 
	if (i == 'B'):
		Count-=1
	votes+=1 

if (1<votes<15): 
	if (Count>0): 
		print('A') 
	elif (Count<0): 
		print('B') 
	else:
		print('Tie') 
