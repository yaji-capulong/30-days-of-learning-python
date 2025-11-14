#Day 7: 30 Days of Python Programming

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print('IT Companies Set length: ', len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies.update(['Instagram', 'TikTok', 'Vine'])
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove('Vine')
print(it_companies)

#What is the difference between remove and discard
#it_companies.remove('Vine') #causes an error
it_companies.discard('Vine') #does not cause error

#Join A and B
C = A.union(B)
print(C)

#Find A intersection B
print('A Intersection of B:',A.intersection(B))

#Is A subset of B
print('Is A subset of B:',A.issubset(B))

#Are A and B disjoint sets
print('Are A and B disjoint sets:',A.isdisjoint(B))

#Join A with B and B with A
C = A.union(B)
D = B.union(A)

#What is the symmetric difference between A and B
print('Symmetric Difference between A and B:',A.symmetric_difference(B))

#Delete the sets completely
del A
del B

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_set = set(age)
print('Set length:',len(ages_set))
print('List length:',len(age))

#Explain the difference between the following data types: string, list, tuple and set
    #String - any data type written as text
    #List - collection of ordered and mutable data types
    #Tuple - collection of immutable ordered data types 
    #Set - store unique items

#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
sentence_list = sentence.split()
sentence_set = set(sentence_list)
print('List length:',len(sentence_list))
print('Set length:',len(sentence_set))