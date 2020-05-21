# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#
# • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#
# • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
#
# • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

# Exercise 3-6

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

# Exercise 3-7
print ("Sorry guys, I can only invite 2 persons.")

print(strangeperson.pop() + " left.")
print(strangeperson.pop() + " left.")
print(strangeperson.pop() + " left.")
print(strangeperson.pop() + " left.")

print (strangeperson[0] + " you still in!")
print (strangeperson[1] + " you still in!")

del strangeperson
