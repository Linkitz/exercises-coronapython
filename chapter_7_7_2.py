# 7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.

message = input("How many people are in your dinner group?")
message = int(message)

if (message > 8):
    print("You\'ll have to wait.")
else:
    print("Your table is ready!")
