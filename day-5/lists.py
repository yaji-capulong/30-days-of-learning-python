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
it_companies.sort()
print('Ascending Order: ', it_companies)

#Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print('Descending Order: ', it_companies)

#Slice out the first 3 companies from the list
print('First three companies: ',it_companies[0:3])

#Slice out the last 3 companies from the list
length = len(it_companies)
print('Last three companies: ', it_companies[(length-3):length])

#Slice out the middle IT company or companies from the list
middlecompany = length // 2
print('Middle IT company: ', it_companies[middlecompany])

#Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

#Remove the middle IT company or companies from the list
it_companies.pop(4)
print(it_companies)

#Remove the last IT company from the list
it_companies.pop()
print(it_companies)

#Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#Destroy the IT companies list
del it_companies
#print(it_companies)

#Join the following lists:
''' front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']'''
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

fullstack = front_end + back_end
print(fullstack)

#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = fullstack.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')

print(full_stack)

#Exercises: Level 2
#The following is a list of 10 students ages:
'''ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]'''

    #Sort the list and find the min and max age
    #Add the min age and the max age again to the list
    #Find the median age (one middle item or two middle items divided by two)
    #Find the average age (sum of all items divided by their number)
    #Find the range of the ages (max minus min)
    #Compare the value of (min - average) and (max - average), use abs() method

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list and find the min and max age
ages.sort()
length = len(ages)
print('Minimum Age: ', ages[0])
print('Maximum Age: ', ages[length-1])

#Add the min age and the max age again to the list
ages.append(ages[0])
ages.append(ages[length-1])
print(ages)

#Find the median age (one middle item or two middle items divided by two)
mid1 = (length - 1)//2
mid2 = (length)//2
median = (ages[mid1] + ages[mid2])/2
print('Median: ', median)

#Find the average age (sum of all items divided by their number)
tempSum = 0
for i in ages:
    tempSum +=i

print('Average Age:',tempSum / 12)

#Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
lengthCountry = len(countries)
if lengthCountry % 2 == 0:
    medianCountry = lengthCountry / 2
    print('Median Country: ', medianCountry)
else:
    medianCountry1 = (lengthCountry - 1) // 2
    print(f'Median Country: {countries[medianCountry1]} & {countries[medianCountry1+1]}' )

#Divide the countries list into two equal lists if it is even if not one more country for the first half.
if lengthCountry % 2 == 0:
    midCountry = lengthCountry / 2
    print('First List: ', countries[0:midCountry])
    print('Second List: ', countries[midCountry:lengthCountry])
else:
    firstListLen = ((lengthCountry - 1) // 2) + 1
    print('First List ', countries[0:firstListLen])
    print('Second List ', countries[firstListLen:lengthCountry])

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countryList = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, rus, us, *scandic = countryList
print(f'Unpacked: {ch} {rus} {us}\nScandic: {scandic}')