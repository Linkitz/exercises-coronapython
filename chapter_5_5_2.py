
#5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:

#Tests for equality and inequality with strings

name = 'Pedro'

print("Is name == 'Pedro'?")
print(name == 'Pedro')

print("Is name != 'Pedro'?")
print(name != 'Pedro')


#• Tests using the lower() function

print("Is name == 'Pedro'.lower()?")
print(name == 'Pedro'.lower())

print("Is name != 'Pedro'.lower()?")
print(name != 'Pedro'.lower())

#• Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to

print("50 > 20?")
print(50 > 20)

print("50 > 50?")
print(50 > 50)

print("50 >= 50?")
print(50 >= 50)

print("50 <= 50?")
print(50 <= 50)

print("50 == 50?")
print(50 == 50)

#• Tests using the and keyword and the or keyword

print("Is (20 > 10) and (53 < 70)?")
print((20 > 10) and (53 < 70))

print("Is (20 > 10) and (53 < 14)?")
print((20 > 10) and (53 < 14))

print("Is (20 > 10) or (53 < 14)?")
print((20 > 10) or (53 < 14))

#• Test whether an item is in a list

names = ['João', 'Pedro', 'Thales', 'Matheus', 'André']

print("Is André in names?")
print('André' in names)

#• Test whether an item is not in a list

print("Is Thais in names?")
print('Thais' in names)




