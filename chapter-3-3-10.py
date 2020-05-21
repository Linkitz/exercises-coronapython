# 3-10. Every Function: Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

list = ['Pokemón', 'Digimon', 'Ragnarok']

print(list)

print("I like " + list[0] + ", " + list[1] + " and " + list[2] + ".")

#Append
list.append('World of Warcraft')
print(list)

#Insert
list.insert(2,'Rocket League')
print(list)

#Remove
list.remove('Digimon')
print(list)

#POP
print("I removed " + list.pop(1) + ".")
print(list)

#Reverse
print(sorted(list,reverse=True))
print(list)

#Reverse Sort
list.sort(reverse=True)
print(list)