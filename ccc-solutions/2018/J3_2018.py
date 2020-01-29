import time
start = time.time()

splitinput = input().split()
numinput = []

for i in range(len(splitinput)):
  numinput.append(int(splitinput[i]))

length = 5
for i in range(5):
  mystring = ""  
  
  for j in range(5):
    if j == i:
      mystring += str(0)
      
    elif j > i:
      addnum = 0
      for x in numinput[i:j]:
        addnum += x
      mystring += (str(addnum))
    
    elif j < i:
      addnum = 0
      for x in numinput[j:i]:
        addnum += x
      mystring += (str(addnum))
    
    if j < length:
      mystring += " "
  
  print(mystring)

end = time.time()
print(end - start)