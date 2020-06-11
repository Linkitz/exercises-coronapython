# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:

#• Use a conditional test in the while statement to stop the loop.

#• Use an active variable to control how long the loop runs.

#• Use a break statement to exit the loop when the user enters a 'quit' value.

loop_count = 0

while True:
    
    message = input("Type your age for ticket price check.")
    if (message == 'quit'):
        break

    message = int(message)    
    if (message < 3):
        print("Your ticket is free!")
    elif (message >= 3) and (message < 12):
        print("Your ticket cost $10!")
    elif (message >= 12):
        print("Your ticket cost $15!")
    loop_count += 1 
    
print("Loop count: " + str(loop_count))