# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

favorite_places ={
    'matheus': {
        'place1': 'japão',
        'place2': 'china',
        'place3': 'marrocos'
        },
    'thales': {
        'place1': 'canadá',
        'place2': 'australia',
        'place3': 'india'
        },
    'andre': {
        'place1': 'alemanha',
        'place2': 'toronto',
        'place3': 'lisboa'
        }

}

for key, value in favorite_places.items():
    print(key + " wanna visit " + value['place1'] + ', ' + value['place2'] + ' and ' + value['place3'])