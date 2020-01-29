# Problem J4/S1: Flipper
# Manraj Pannu
# 593368
# ICS4U0
# 6 sep 2018

import math
def test_prime(n):
    if n == 2: 
        return True 
    if n % 2 == 0:
        return False
    upper_lim = int(math.sqrt(n)) + 1
    # check odd numbers from 3 to sqrt(n)
    return len([i for i in range(3, n, 2) if n % i == 0]) == 0


def primefinder(num):

	if test_prime(num) == True:
		return (num, num)
	else:
		for i in range(3,num+1,2):
			if test_prime(i) == True and test_prime((num*2)-i) == True:
				return (i,(num*2)-i)

integers = []
for i in range(int(input())):
	integers.append(int(input()))

for i in integers:
	print(*primefinder(i), sep =' ')

