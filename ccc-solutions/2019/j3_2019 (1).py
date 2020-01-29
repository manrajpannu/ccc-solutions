# Problem J3: Cold Compress
# Manraj Pannu
# 593368
# ICS4U0
# 6 sep 2018

def compress(decode): # function to encode the message: **** -> 4 *

	message = [] #create a list to input the encoded message
	counter = 1 #create a counter at 1
	decode = decode + " " #add a space at the end of the message to fix an error 

	for i in range(len(decode)):  #loop over the length of the message

		try: # try to run this code (to error check with except function)
			if decode[i] == decode[i+1]: #if the current character in this list is the same as the next one then:
				counter+=1 #increment counter by 1 

			else: #if the next character isnt the same as the current one then:
				message.append(counter)	#add the counter to the list
				message.append(decode[i]) #add the character to the list 
				
				counter = 1 # reset counter back to 1

		except: return message # if error occurs then automatically output the list (with except function)

num = int(input()) # ask for input for amount of messages to encode
sequence_of_symbols = [] #create a list for the sequence of symbols

for i in range(num): #loop for the amount of messages to encode
	sequence_of_symbols.append(str(input())) #ask for input for the messages
	
for i in range(num): #loop for the amount of messages to encode
	codes = compress(sequence_of_symbols[i]) #run the function over each message
	print(*codes, sep =' ') #output each compressed message - use sep function to print the messages without the brackets
	codes = '' #reset variable





