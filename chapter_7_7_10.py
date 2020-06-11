# 7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.

places = {}

while True:
    name = input("What is your name?")
    place = input("Where would you like to go?")

    places[name] = place

    message = input("Type \'Y\' to add another person and \'N\' exit.")

    if message == 'N':
        break

for key, values in places.items():
    print(key + " favorites place is " + values + ".")