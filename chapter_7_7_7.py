# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press CTRL-C or close the window displaying the output.)

while True:
    
    message = input("Type your age for ticket price check.")

    message = int(message)    
    if (message < 3):
        print("Your ticket is free!")
    elif (message >= 3) and (message < 12):
        print("Your ticket cost $10!")
    elif (message >= 12):
        print("Your ticket cost $15!")
