#Day 9: 30 Days of Python Programming

#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
#You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
user = int(input('Enter your age: '))

if user >= 18:
    print('You are old enough to drive.')
elif user < 18:
    missingYrs = 18 - user
    print(f'Wait for {missingYrs} more years.')

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
#Use input(“Enter your age: ”) to get the age as input. You can use a nested condition 
#to print 'year' for 1 year difference in age, 'years' for bigger differences, and a 
#custom text if my_age = your_age. Output:
your_age = int(input('Enter your age: '))
my_age = int(input('Enter your age: '))
difference = your_age - my_age

if your_age > my_age:
    if abs(difference) == 1:
        print(f'You are older than me by {abs(difference)} year.')
    elif abs(difference) > 1:
        print(f'You are older than me by {abs(difference)} years.')
elif your_age < my_age:
    if abs(difference) == 1:
        print(f'I am older than you by {abs(difference)} year.')
    elif abs(difference) > 1:
        print(f'I am older than you by {abs(difference)} years.')
else:
    print('We are the same age. Lock in twin.')

#Get two numbers from the user using input prompt.
#If a is greater than b return a is greater than b, if a is less b return a is smaller than b, 
#else a is equal to b. Output:
a = int(input('Enter a number: '))
b = int(input('Enter a number: '))

if a > b:
    print('A is greater than B.')
elif a < b:
    print('A is smaller than B.')
else:
    print('A is equal to B.')

#Write a code which gives grade to students according to theirs scores:
''' 90-100, A
    70-89, B
    60-69, C
    50-59, D
    0-49, F
'''
grade = int(input('What is your grade: '))

if grade >= 90 and grade <= 100:
    print('Your final grade is A')
elif grade >= 70 and grade <= 89:
    print('Your final grade is B')
elif grade >= 60 and grade <= 69:
    print('Your final grade is C')
elif grade >= 50 and grade <= 59:
    print('Your final grade is D')
elif grade >= 0 and grade <= 49:
    print('Your final grade is F')

#Check if the season is Autumn, Winter, Spring or Summer. If the user input is: 
#September, October or November, the season is Autumn. December, January or February, 
#the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = str(input('Enter a month: '))
autumn = ['September','October','November']
winter = ['December','January','February']
spring = ['March','April','May']
summer = ['June','July','August']

if month in autumn:
    print('The season is Autumn.')
elif month in winter:
    print('The season is Winter.')
elif month in spring:
    print('The season is Spring.')
elif month in summer:
    print('The season is Summer.')
else:
    print('Invalid input.')

#The following list contains some fruits:
#If a fruit doesn't exist in the list add the fruit to the list and 
#print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_input = str(input('Enter a fruit: '))

if fruit_input in fruits:
    print('Fruit already exists in the list.')
else:
    fruits.append(fruit_input)
    print(f'{fruit_input} has been added to the list.\nFruits:{fruits}')

#Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Jesse',
    'last_name': 'Diaz',
    'age': 26,
    'country': 'Canada',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': '3rd Street',
        'zipcode': '12345'
    }
    }

#Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if len(person['skills']) != 0:
    mid_skill = len(person['skills']) // 2
    skills_list = person['skills']
    name = person['first_name']
    print(f'One skill of {name} is {skills_list[mid_skill]}')

#Check if the person dictionary has skills key, if so check if the person has 'Python' skill 
#and print out the result.
if person['skills'] != 0:
    if 'Python' in person['skills']:
        print(f'{name} has the skill Python.')

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person 
# skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, 
# Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - 
# for more accurate results more conditions can be nested!

if 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print('He is a front-end developer')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a backend developer')
elif 'React' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a full stack developer')
else:
    print('Unknown title')

# If the person is married and if he lives in Finland, print the information in the following format
# "Asabeneh Yetayeh lives in Finland. He is married."

first_name = person['first_name']
country = person['country']
if person['is_married'] == True:
    print(f'{first_name} lives in {country}. He is married.')