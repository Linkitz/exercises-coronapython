# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size = 'large', message = 'I love Python'):
    print("The size of shirt is " + size + ". The printed will be \'" + message + "\'.")

make_shirt(size = 'large')
make_shirt(size = 'medium')

make_shirt(message = "a beautiful message")