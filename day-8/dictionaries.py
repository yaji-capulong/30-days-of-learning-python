#Day 8: 30 Days of Python Programming

#Create an empty dictionary called dog
dog = {}

#Add name, color, breed, legs, age to the dog dictionary
dog['Name'] = 'Jones'
dog['Color'] = 'Brown'
dog['Breed'] = 'Beagle'
dog['Legs'] = '4'
dog['Age'] = '2'
print(dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'Jesse',
    'last_name':'Diaz',
    'gender':'Male',
    'age':'26',
    'marital status':'Single',
    'skills':['Math','Machining','Fusion','CNC'],
    'country':'Canada',
    'city':'Vancouver',
    'address':'3rd Avenue',
}

#Get the length of the student dictionary
print(len(student))

#Get the value of skills and check the data type, it should be a list
print(type(student['skills']))

#Modify the skills values by adding one or two skills
student['skills'].append('Driving')
print(student['skills'])

#Get the dictionary keys as a list
keys = student.keys()
print('Student Keys: ',keys)

#Get the dictionary values as a list
values = student.values()
print('Student Values: ',values)

#Change the dictionary to a list of tuples using items() method
student.items()

#Delete one of the items in the dictionary
del student['address']

#Delete one of the dictionaries
del dog

