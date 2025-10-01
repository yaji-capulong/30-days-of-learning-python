#Day 2: 30 Days of Python Programming

import math

first_name = 'mj'
last_name = 'capulong'
full_name = 'Mj Capulong'
country = 'Canada'
age = 24
year = 2001
is_married = 0
is_true = 0
is_light_on = 0
multi_var = 1,2,3,4,5

#print(type(first_name))
#print(type(last_name))
#print(type(full_name))
#print(type(country))
#print(type(age))
#print(type(year))
#print(type(is_married))
#print(type(is_true))
#print(type(is_light_on))
#print(type(multi_var))

print('First Name length:', len(first_name))
print('Last Name length:', len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
variable = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(variable)
print(floor_division)

circleRad = 30
area_of_circle = (math.pi * circleRad) ** 2
print(area_of_circle)

circum_of_circle = 2 * math.pi * circleRad
print(circum_of_circle)

userRad = int(input('Radius: '))
area_of_circle = (math.pi * userRad) ** 2
print(area_of_circle)

firstName = str(input('First Name: '))
lastName = str(input('Last Name: '))
country = str(input('Country of Residence: '))
age = str(input('Age: '))

print(firstName, lastName, country, age)