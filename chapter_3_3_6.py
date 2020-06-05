# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print statement to the end of your program informing people that you found a bigger dinner table.
#
# • Use insert() to add one new guest to the beginning of your list.
#
# • Use insert() to add one new guest to the middle of your list.
#
# • Use append() to add one new guest to the end of your list.
#
# • Print a new set of invitation messages, one for each person in your list. 

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

# Exercise 3-6
print("GUYS!!!! I found a bigger dinner table!")

strangeperson.insert(0, 'Strange Nº 5')
strangeperson.insert(2, 'Strange Nº 6')
strangeperson.append('Strange Nº 7')

print("Yoooo! " + strangeperson[0] + ", let's dinner!")
print("Yoooo! " + strangeperson[1] + ", let's dinner!")
print("Yoooo! " + strangeperson[2] + ", let's dinner!")
print("Yoooo! " + strangeperson[3] + ", let's dinner!")
print("Yoooo! " + strangeperson[4] + ", let's dinner!")
print("Yoooo! " + strangeperson[5] + ", let's dinner!")