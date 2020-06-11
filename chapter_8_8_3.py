#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.

#Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size, message):
    print("The size of shirt is " + size + ". The printed will be \'" + message + "\'.")

make_shirt('Large',"a beautiful message")

make_shirt(message = "a beautiful message", size = 'Medium')