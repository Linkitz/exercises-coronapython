# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {
    'macaé': {
        'country': 'brasil',
        'population': 300000,
        'info': 'small city'
    },
    'rio de janeiro': {
        'country': 'brasil',
        'population': 16460000,
        'info': 'tour city'  
    },
    'são paulo': {
        'country': 'brasil',
        'population': 44040000,
        'info': 'big city'  
    }   
}

for city,value in cities.items():
    print(city.title() + ' is located in ' + value['country'] + '. It\'s population is around ' + str(value['population']) + '. It\'s a ' + value['info'])