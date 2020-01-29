#Problem J4: Favourite Times
def sequence_finder(s):
	dif = []
	for i in range(len(s)-1):
		dif.append(int(s[i+1]) - int(s[i]))

	return dif

def checkEqual(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)

start = [12,00]
time = []
new = []
lit = []
counter = 0
string_of_numbers = ''
for i in range(int(input())):
	start[1]+=1

	if start[1] > 59:
		start[1]=0
		start[0]+=1

	if start[0] > 12:
		start[0] = 1	
	
	lit.append(str(start[0]))
	lit.append(str(format(round(start[1]),"02")))

	string_of_numbers = "".join(lit)

	if checkEqual(sequence_finder(string_of_numbers)) == True:
		counter +=1

	lit = []

print(counter)