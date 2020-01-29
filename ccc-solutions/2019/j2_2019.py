# Problem J2: Time to Decompress
# Manraj Pannu
# 593368
# ICS4U0
# 6 sep 2018

def decode(code): # function to decode the encoded message - where the code is the input
	code = code.split() # takes the string and makes it into a list
	decoded = code[1] * int(code[0]) # multiply the number by the symbol: [9,*] 9 = number, * = symbol
	return decoded	# output the decoded message back 	

num = int(input("Enter amount of encoded messages: "))   # ask for input from user for the amount of messages
code_symbol = [] # create list to input messages into

for i in range(num): # loops the number inputed
	code_symbol.append(input("Enter message: ")) # inputs user's code into a list

for i in range(num): # loops the number inputed
	print(decode(code_symbol[i])) #decodes each code from the list and prints it




	







