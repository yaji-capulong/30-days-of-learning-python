#Day 4: 30 Days of Python Programming

#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'

sentence = str1 + str2 + str3 + str4
print(sentence)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
first_word = 'Coding'
second_word = 'For'
third_word = 'All'

sentence = str1 + str2 + str3
print(sentence)

#Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

#Print the variable company using print().
print(company)

#Print the length of the company string using len() method and print().
print(len(company))

#Change all the characters to uppercase letters using upper() method.
print(company.upper())

#Change all the characters to lowercase letters using lower() method.
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of Coding For All string.
coding = company[0:6]
print(coding)

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
print(company.find('Coding'))

#Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('coding', 'python'))

#Change Python for Everyone to Python for All using the replace method or other methods.
phrase =  'Python for Everyone'
print(phrase.replace('Python', 'Coding'))

#Split the string 'Coding For All' using space as the separator (split()) .
company= 'Coding For All'
print(company.split(' '))

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
socmed = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(socmed.split(', '))

#What is the character at index 0 in the string Coding For All.
index = 0
print(company[index])

#What is the last index of the string Coding For All.
lastletter = 'l'
print(company.rindex(lastletter))

#What character is at index 10 in "Coding For All" string.
print('Character: ',company[10])

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
python_phrase = 'Python For Everyone'
split_phrase = python_phrase.split()
first_word = split_phrase[0]
second_word = split_phrase[1]
third_word= split_phrase[2]
print(first_word[0] + second_word[0] + third_word[0])

#Create an acronym or an abbreviation for the name 'Coding For All'.
coding_phrase = 'Coding For All'
splitc_phrase = coding_phrase.split()
firstc_word = splitc_phrase[0]
secondc_word = splitc_phrase[1]
thirdc_word= splitc_phrase[2]
print(firstc_word[0] + secondc_word[0] + thirdc_word[0])

#Use index to determine the position of the first occurrence of C in Coding For All.
print('Index: ',coding_phrase.index('C'))

#Use index to determine the position of the first occurrence of F in Coding For All.
print('Index: ',coding_phrase.index('F'))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(coding_phrase.rfind('l'))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence_one = 'You cannot end a sentence with because because because is a conjunction'
print(sentence_one.index('because'))

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence_one.rindex('because'))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence_one[31:54])

#Does ''Coding For All' start with a substring Coding?
print(coding_phrase.startswith('Coding'))

#Does 'Coding For All' end with a substring coding?
print(coding_phrase.endswith('Coding'))

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
phraseCoding = '   Coding For All      '
print(phraseCoding.strip('   '))

#Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
challenge = '30DaysOfPython'
print(challenge.isidentifier())

#thirty_days_of_python
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.


#Use the new line escape sequence to separate the following sentences.
