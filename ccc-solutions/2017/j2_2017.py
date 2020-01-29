# Shifty Sum
# Manraj Pannu
# 593368
# ICS3U0A
# 10 Oct 2018

N = int(input())
k = int(input())

limit = k + 1
count = 0
answer = 0

while(count != limit):

	answer+=(N*(10**count))
	
	count+=1 

print(answer)