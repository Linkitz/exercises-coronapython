# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

person = {'first_name':'matheus', 'last_name':'dantas', 'age':29, 'city':'salvador'}
person2= {'first_name':'pedro', 'last_name':'pinto', 'age':28, 'city':'salvador'}
person3= {'first_name':'Thais', 'last_name':'dantas', 'age':28, 'city':'salvador'}

people = [person, person2,person3]

for persons in people:    
    print(persons['first_name'])
    print(persons['last_name'])
    print(str(persons['age']))
    print(persons['city'])