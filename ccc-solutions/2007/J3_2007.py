brief_cases = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
number_of_removed_cases = int(input())
for i in range(number_of_removed_cases):

	case = int(input())

	brief_cases[case - 1] = 0

bankers_offer = int(input())

if (sum(brief_cases) / (10 - number_of_removed_cases)) < bankers_offer: print('deal')
else: print('no deal')