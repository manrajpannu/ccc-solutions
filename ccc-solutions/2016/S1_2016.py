# Problem S1: Ragaman


def remove_occurence(list1,list2):
	new = []
	for elem in list1:
		if elem in list2:
			new.append(elem)
			list2.remove(elem)

	if new == list1:
		return True
	else: return False

			

string_1 = sorted(list(input()))
string_2 = sorted(list(input()))

while "*" in string_2:
	string_2.remove('*')

if string_1 == string_2:
	print("N")
	quit()

if remove_occurence(string_2,string_1) == True:
	print('A')
else: print('N')

