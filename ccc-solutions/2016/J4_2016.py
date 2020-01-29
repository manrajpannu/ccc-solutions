#Problem J4: Arrival Time

departure_time = input().split(":")
total_commute_time = float(120)



for i in range(2):
	departure_time[i] = int(departure_time[i])

while total_commute_time != 0:

	if 7 <= departure_time[0] <= 9 or 15 >= departure_time[0] >= 18 :
		total_commute_time-=.5
		departure_time[1]+=1
	else:
		total_commute_time-=1
		departure_time[1]+=1

	if departure_time[1] >= 60:
		departure_time[1] = 0
		departure_time[0]+=1

	if departure_time[0] >= 24:
		departure_time[0] = 0	

print(str(format(departure_time[0],"02")+':'+str(format(round(departure_time[1]),"02"))))

