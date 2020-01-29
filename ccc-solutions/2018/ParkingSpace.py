# Parking Spaces
# Manraj Pannu
# 593368
# ICS3U0A
# 6 Dec 2018

number_of_parking_spaces = int(input()) # prompts user for the number of parking spaces

yesterday_parking = input() # prompts user for recorded information about yesterday’s parking spaces

today_parking = input() # prompts user for recorded information about today's parking spaces

count_parking = 0 # counter: the number of parking spaces which were occupied yesterday and today.

yesterday_parking_list = [] # empty list for yesterday's parking information
today_parking_list = [] # empty list for today's parking information


for char in yesterday_parking: # loops through each indivdual character in the string for yesterday's parking spaces
	yesterday_parking_list.append(char) # takes each indivdual character and puts it into a list

for char in today_parking: # loops through each indivdual character in the string for today's parking spaces
	today_parking_list.append(char) # takes each indivdual character and puts it into a list


if len(yesterday_parking_list) == number_of_parking_spaces and len(today_parking_list) == number_of_parking_spaces: # Checks if the number of parking spaces is equal to the recorded information for both days

	for i in range(number_of_parking_spaces): # loops from zero to the number of parking spaces 

		if yesterday_parking_list[i] == 'C' and today_parking_list[i] == 'C': # checks if each character in parking info for yesterday and today is 'C' or not
			count_parking+=1 # if the parking data is equal to 'C' for each parking space then count it
	print('\nOccupied Parking: '+str(count_parking)) # output the total number of parking spaces which were occupied yesterday and today.
else: # if parking data doesnt correlate with number of parking spaces
	quit() #quits the program