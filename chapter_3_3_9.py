# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 46), use len() to print a message indicating the number of people you are inviting to dinner.

# Exercise 3-5
strangeperson = ['Strange Nº 1', 'Strange Nº 2', 'Strange Nº 3']

print("Yoooo! " + strangeperson[0] + ", let's dinner!")
print("Yoooo! " + strangeperson[1] + ", let's dinner!")
print("Yoooo! " + strangeperson[2] + ", let's dinner!")

popedperson = strangeperson.pop(1)

print("Unfortunately " + popedperson + " could not join us.")

addguest = 'Strange Nº 4'

strangeperson.insert(1,addguest)

print(addguest + " is the new guest!")

print("Yoooo! " + strangeperson[0] + ", let's dinner!")
print("Yoooo! " + strangeperson[1] + ", let's dinner!")
print("Yoooo! " + strangeperson[2] + ", let's dinner!")

print("There are " + str(len(strangeperson)) + " persons invited to dinner.")