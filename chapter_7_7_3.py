# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

message = input("Write a number multiple of 10.")
message = int(message)

if (message % 10 == 0):
    print("This number is multiple of 10!")
else:
    print("This number is not multiple of 10!!!")
