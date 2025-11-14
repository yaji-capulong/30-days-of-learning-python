#Day 6: 30 Days of Python Programming

#Create an empty tuple
tpl = ()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Revel', 'MJ', 'Steven')
sisters = ('Claire','Lian')

#Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

#How many siblings do you have?
print('Number of siblings: ', len(siblings))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_memb5ers
family_members = list(siblings)
family_members.append('Grace')
family_members.append('Jay')

print('Family: ',family_members)
#Unpack siblings and parents from family_members
*siblings, gr,j = family_members
rv, mj,st,cl,li,*parents = family_members
print('Siblings: ', siblings)
print('Parents: ', parents)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('orange', 'apple', 'grape', 'mango')
vegetables = ('cabbage', 'carrot', 'cucumber', 'onion')
animal_products = ('beef', 'chicken', 'pork', 'fish')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
mid_food = len(food_stuff_lt) // 2
print('Middle Food:', food_stuff_lt[mid_food])

#Slice out the first three items and the last three items from food_staff_lt list
print('First three items:', food_stuff_lt[0:3])
print('Last three items:', food_stuff_lt[-3:])

#Delete the food_staff_tp tuple completely
del food_stuff_tp

#Check if an item exists in tuple:
# - Check if 'Estonia' is a nordic country
# - Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)