#Problem J3: Hidden Palindrome

def Palindrome(string):
	stringStrip = string.replace(' ', '').lower() 
	reverse = ''.join(reversed(stringStrip)) 

	if string == reverse:
		return 'yes'
	else:
		return 'no'

string = input()
palidrome_list=[]

for i in range(len(string)):
	for x in range(i+1,len(string)+1):
		if len(string[i:x]) >= 2 and Palindrome(string[i:x]) == "yes":
			palidrome_list.append(string[i:x])


palidrome_len_list = []
for i in range(len(palidrome_list)):
	palidrome_len_list.append(len(palidrome_list[i]))
print(max(palidrome_len_list))

