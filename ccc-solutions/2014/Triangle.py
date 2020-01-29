# Triangle
# Manraj Pannu
# 593368
# ICS3U0A
# 23 Oct 2018

firstAngle = int(input()) # input: the first angle of the triangle
secondAngle = int(input())  # input: the second angle of the triangle
thirdAngle = int(input())  # input: the third angle of the triangle

totalAngle = (firstAngle + secondAngle + thirdAngle) # calculates the total angle of the triangle

if (firstAngle == 60 and secondAngle == 60 and thirdAngle == 60) : # checks if all the angles have 60 degree angles
	print('Equilateral') # output: that the triangle is equilateral

elif (totalAngle == 180 and (firstAngle == secondAngle or secondAngle == thirdAngle or firstAngle == thirdAngle) ):  # checks if all the angles equal to 180 and that atleast two of the angles are the same
	print('Isosceles') # output: that the triangle is equilateral

elif (totalAngle == 180 and (firstAngle != secondAngle and secondAngle != thirdAngle and firstAngle != thirdAngle) ):  # checks if all the angles equal to 180 and that all of the angles arent the same
	print('Scalene') # output: that the triangle is equilateral

else :  # works if all other conditional statements are false
	print('Error') #output : that there is no proper inputs for it to be a triangle
