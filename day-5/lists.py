##Day 5: 30 Days of Python Programming

#Declare an empty list
empty_list = list()

#Declare a list with more than 5 items
listOfFive = ['jesse', 'is', 'a', 'handsome', 'cutie', 'baby']

#Find the length of your list
print(len(listOfFive))

#Get the first item, the middle item and the last item of the list
first_item = listOfFive[0]
middle_item = listOfFive[3]
last_item = listOfFive[5]

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Jesse','26','154','single','Vancouver']

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook','Google','Microsoft','Apple','IBM', 'Oracle', 'Amazon']

#Print the list using print()
print(it_companies)

#Print the number of companies in the list
print(len(it_companies))

#Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])

#Print the list after modifying one of the companies
it_companies[4] = 'Electronic Arts'
print(it_companies)

#Add an IT company to it_companies
it_companies.append('Bad Dragon')
print(it_companies)

#Insert an IT company in the middle of the companies list
it_companies.insert(3, 'Acer')
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[1].upper())

#Join the it_companies with a string '#;  '
it_companies.append('#; ')
print(it_companies)

#Check if a certain company exists in the it_companies list.
does_exist = 'Amazon' in it_companies
print(does_exist)

#Sort the list using sort() method
print('Ascending Order: ')
print(it_companies.sort())

#Reverse the list in descending order using reverse() method
print('Descending Order: ',it_companies.sort(reverse=True))

#Slice out the first 3 companies from the list
print(it_companies)
print('First three companies: ',it_companies[0:3])

#Slice out the last 3 companies from the list
length = len(it_companies)
print('Last three companies: ', it_companies[(length-3):length])

#Slice out the middle IT company or companies from the list


#Remove the first IT company from the list


#Remove the middle IT company or companies from the list


#Remove the last IT company from the list


#Remove all IT companies from the list


#Destroy the IT companies list


#Join the following lists:
''' front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']'''

#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

#Exercises: Level 2
#The following is a list of 10 students ages:
'''ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]'''

    #Sort the list and find the min and max age
    #Add the min age and the max age again to the list
    #Find the median age (one middle item or two middle items divided by two)
    #Find the average age (sum of all items divided by their number )
    #Find the range of the ages (max minus min)
    #Compare the value of (min - average) and (max - average), use abs() method


#Find the middle country(ies) in the countries list


#Divide the countries list into two equal lists if it is even if not one more country for the first half.


#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.