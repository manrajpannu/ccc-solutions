num = int(input())

yesterday = input()
today = input()

counter = 0

for i in range(len(yesterday)):
  if yesterday[i] == 'C':
    if yesterday[i] == today[i]:
      counter += 1
      
print(counter)