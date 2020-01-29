# Nikky and Byron
# Manraj Pannu
# 593368
# ICS3U0A
# 21 Jan 2018

def Nikki(a,b,s): # Function for nikki with integer parameters: a,b,s

	total_steps = 0 # records the distance from starting position

	counter = 0 # records the total amount of steps taken
	
	for i in range(s):
		for i in range(a):
			total_steps += 1
			counter += 1
			
			if counter == s:
				return total_steps

		for i in range(b):
			total_steps-=1
			counter += 1	
		
			if counter == s:
				return total_steps

def Byron(c,d,s): # Function for byron with integer parameters: a,b,s

	total_steps = 0 # records the distance from starting position

	counter = 0 # records the total amount of steps taken
	
	for i in range(s): # loops through the amount of steps : s

		for i in range(c): # loops through forward steps
			total_steps += 1 # adds one value to position
			counter += 1 # add value to total steps taken
			
			if counter == s: # if the total steps reaches s: 
				return total_steps # returns the total steps

		for i in range(d): # loops through backward steps
			total_steps-=1
			counter += 1	# add value to total steps taken
			
			if counter == s:
				return total_steps


a = int(input()) # Nikki's forward step
b = int(input()) # Nikki's backward step
c = int(input()) # Byron's forward step 
d = int(input()) # Byron's backward step
s = int(input()) # Total amount of steps to take

if Nikki(a,b,s) > Byron(c,d,s):
	print("Nikki")
elif Nikki(a,b,s) < Byron(c,d,s):
	print("Byron")
else: print("Same")

