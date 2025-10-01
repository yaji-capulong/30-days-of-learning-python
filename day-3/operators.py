#Day 3: 30 Days of Python Programming
#
#import math
##Declare your age as integer variable
#age = 24
#
##Declare your height as a float variable
#height = 141
#
##Declare a variable that store a complex number
#complexNum = 1 + 1j
#
##Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#base = int(input('Enter base: '))
#heightTri = int(input('Enter height: '))
#
#area_of_triangle = 0.5 * base * heightTri
#print('Area of Triangle: ', area_of_triangle)
#
##Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
#side_a = int(input('Side A: '))
#side_b = int(input('Side B: '))
#side_c = int(input('Side C: '))
#
#perimeter = side_a + side_b + side_c
#print('Perimeter of Triangle: ', perimeter)
#
##Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
#length_rec = int(input('Length: '))
#width_rec = int(input('Width: '))
#
#area_of_rectangle = length_rec * width_rec
#print('Area of Rectangle: ', area_of_rectangle)
#
#perimeter_of_rectangle = 2 * (length_rec + width_rec)
#print('Perimeter of Rectangle: ', perimeter_of_rectangle)
#
##Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
#radius = int(input('Radius: '))
#area_of_circle = math.pi * radius * radius
#circumference = 2 * math.pi * radius
#
#print('Area of Circle: ', area_of_circle)
#print('Circumference: ', circumference)
#
##Calculate the slope, x-intercept and y-intercept of y = 2x -2
#
##Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
#
##Compare the slopes in tasks 8 and 9.
#
##Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
#
##Find the length of 'python' and 'dragon' and make a falsy comparison statement.
#print(len('python')) > print(len('dragon'))
#
##Use and operator to check if 'on' is found in both 'python' and 'dragon'
#print('on in Python', 'on' in 'python' and 'on' in 'dragon')
#
##I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
#print('jargon' in 'I hope this course is not full of jargon' )
#
##There is no 'on' in both dragon and python
##????
#
##Find the length of the text python and convert the value to float and convert it to string
#length_python = len('python')
#float_python = float(length_python)
#print(str(float_python))
#
##Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
#user_number = int("Enter a number: ")
#
#if user_number % 2 == 0:
#    print('{1} is an even number.', user_number)
#else:
#    print('{1} is an odd number.', user_number)
#
##Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
#floorDiv = 7 // 3
#
#if floorDiv == int(2.7):
#    print('{1} is equal to 2.7', floorDiv)
#else: 
#    print('{1} is not equal to 2.7', floorDiv)
#
##Check if type of '10' is equal to type of 10
#
#
##Check if int('9.8') is equal to 10
#
#
##Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
#hours_worked = int(input('Enter hours of work today: '))
#rate_per_hour = int(input('Enter rate per hour: '))
#pay = rate_per_hour * hours_worked
#
#print('Your pay today is: ', pay)
#
##Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
#number_of_years = int(input('Enter number of years lived: '))
#year_to_seconds = number_of_years * 31,556,952
#
#print('You have lived {1} seconds', year_to_seconds)
#
##Write a Python script that displays the following table

varA = 1
varB = 2
varC = 3
varD = 4
varE = 5


print(varA,'\n',varB,'\n',varC,'\n',varD,'\n',varE)
'''
1 1 1 1 
2 1 2 4 
3 1 3 9 
4 1 4 16 
5 1 5 25 
'''