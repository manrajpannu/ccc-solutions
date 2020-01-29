
string = ''
	
a = int(input())
for i in (a,0,-1):
	print("i=",i)
	string = string.join(' ' * i)	
	for x in (1,(2*a)-1,2):
		print("x=",x)
		string= string.join('*'*x)

	print(string)
	string = ''