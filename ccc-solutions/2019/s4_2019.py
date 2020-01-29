# CCC '19 S4 - Tourism
# Manraj Pannu
# 593368
# ICS4U0
# 6 sep 2018


# input1 = input().split()
# input2= input().split()
# n = int(input1[1])
attractions = [2, 5, 7, 1, 4]
attractions_v3 = [1000000000, 1000000000, 1, 1, 1]
n = 33333
def list_into_int(list_of_strings):
    new = []
    for i in list_of_strings:
        if i != 'X':
            new.append(int(i))
        else: new.append(i)
    return new

def max_sum_of_list(attractions,n):
	attractions_list = []
	for i in range(int(len(attractions)/n)):
		attractions_list.append(max(attractions[i*n:(i+1)*n]))
	return sum(attractions_list)	

def min_tourist(attractions,n):
	result = []
	if n == 1:
		return sum(attractions)
	elif n >= len(attractions):
		return max(attractions)
	elif len(attractions) % n == 0:
		return max_sum_of_list(attractions,n)

	else:
		
		remainders_orders = int(((len(attractions)/n)+1)) # finds number of ordering of remainder
		len_remainder = round(len(attractions)%n)

		for i in range(remainders_orders):
			iteration = i*n
			remaining_attractions = attractions[iteration:(iteration+(len_remainder))]
			outstanding_attractions = attractions.copy()
			del outstanding_attractions[iteration:(iteration+(len_remainder))]
			result.append(max(remaining_attractions)+max_sum_of_list(outstanding_attractions,n))
			
	return max(result)
	


# print(min_tourist(list_into_int(input2),n))
# print(attractions_v2)
print(min_tourist(attractions_v2,n))







# def create_sublists(attractions, n):
# 	my_sublists = []
# 	for i in range(len(attractions)%n):
# 		my_sublists.append(attractions[i*3:(i+1)*3])

# 	return my_sublists




# def permutation(list):
# 	if len(list)==0:
# 		return []
# 	elif len(list)==1:
# 		return [list]
# 	else:
# 		new_list = []
# 		for i in range(len(list)):
# 			x = list[i]
# 			xs = list[:i]+list[i+1:]
# 			for p in permutation(xs):
# 				new_list.append([x]+p)
# 		return new_list

# s = list("aabbcc")
# new = []
# for a in permutation(s):
# 	if a not in new:
# 		new.append(a)
# 		print (a)