#Day 9: 30 Days of Python Programming

#Iterate 0 to 10 using for loop, do the same using while loop.

#for number in range(11):
#    print(number)
#    number +=1

#count = 0
#while count < 11:
#    print(count)
#    count +=1

#Iterate 10 to 0 using for loop, do the same using while loop.

#for number in range(10, -1, -1):
#    print(number)
#
#count = 10
#while count > -1:
#    print(count)
#    count -=1


#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
'''
  #
  ##
  ###
  ####
  #####
  ######
  #######
'''

#pound = '#'
#for i in range(7):
#    print(pound)
#    pound = pound + '#'

#Use nested loops to create the following:
'''
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
'''
pound = '#'

for i in range(8):          # rows
    for j in range(8):      # columns
        print(pound, end=" ")
    print()


#Print the following pattern:
'''
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
'''
count = 0
for i in range(11): #rows
    for j in range(1): #column, in this case, one because we only need one instance of each line
        count2 = count * count #where we multiply our numbers
    print(count,end=' x ' + str(count) + ' = ' +  str(count2)+ '\n')
    count += 1

#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in lst:
    print(i)

#Use for loop to iterate from 0 to 100 and print only even numbers
print("\nEven numbers from 0-100")
for i in range(51):
    i *= 2
    print(i)

#Use for loop to iterate from 0 to 100 and print only odd numbers
print("\nOdd numbers from 0-100")
for i in range(50):
    i = (i * 2) + 1
    print(i)

#Use for loop to iterate from 0 to 100 and print the sum of all numbers.

total = 0
print('Sum of 0-100')
for i in range(101):
    total += i
print(total)

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

totalEven = 0
print('\nSum of even numbers from 0-100')
for i in range(51):
    i *= 2
    totalEven += i
print(totalEven)

totalOdd = 0
print('\nSum of odd numbers from 0-100')
for i in range(50):
    i = (i * 2) + 1
    totalOdd += i
print(totalOdd)

#Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
#Go to the data folder and use the countries_data.py file.
#What are the total number of languages in the data
#Find the ten most spoken languages from the data
#Find the 10 most populated countries in the world