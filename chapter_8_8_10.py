# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9. Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. Call show_magicians() to see that the list has actually been modified.

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magician, magicians):
    magicians.append(magician)

magicians = ['Ratz', 'Fritz', 'Muk']
make_great('Tiger',magicians)

show_magicians(magicians)