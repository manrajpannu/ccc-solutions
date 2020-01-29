# Which Alien?
# Manraj Pannu
# 593368
# ICS3U0A
# 25 Oct 2018
alien = False
antenna = int(input())
eye = int(input())

if (antenna >= 3 and eye <= 4):
	print('TroyMartian') 
	alien = True

if (antenna <= 6 and eye >= 2):
	print('VladSaturnian')
	alien = True

if (antenna <= 2 and eye <= 3 ):
	print('GraemeMercurian')
	alien = True

