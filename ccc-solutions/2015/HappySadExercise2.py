# Happy Sad
# Manraj Pannu
# 593368
# ICS3U0A
# 10 Oct 2018

feeling = input()
feelinghappy = 0
feelingsad = 0

pos = 0
pos2 = 0

while pos != -1 :
	pos = feeling.find(':-)', pos)
	if(pos != -1):
		feelinghappy+=1
		pos+=1
	else:
		break

while pos2 != -1 :
	pos2 = feeling.find(':-(', pos2)
	if(pos2 != -1):
		feelingsad+=1
		pos2+=1
	else:
		break



feelingNum = feelinghappy - feelingsad

if feelingNum == 0 :
	print('none')
elif feelingNum > 0  : 
	print('happy')
elif feelingNum < 0: 
	print('sad')