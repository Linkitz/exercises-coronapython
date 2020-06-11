# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.

def make_album(name, title, ntrack = ''):
    info = {'name':name, 'title':title}
    if ntrack:
        info['ntrack'] = ntrack
    return info



while True:
    name = input("Please, write an album's artist.")
    title = input("Please, write title album.")
    
    print(make_album(name, title))
    
    message = input("Type \'Y\' to enter another album\'s artist and title. For exit type \'N\'.")

    if message == 'N':
        break

