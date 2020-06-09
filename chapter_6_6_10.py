# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

favorite_number = {
    'matheus':{
        'n1':10,
        'n2':4,
        'n3':17
    },
    'thales':{
        'n1':24,
        'n2':33,
        'n3':102,
        'n4':111
    }, 
    'andre': {
        'n1':256,
        'n2':1024
    }, 
    'flavio':{
        'n1':21,
        'n2':22
    },
    'pedro':{
        'n1':17,
        'n2':18,
        'n3':19,
        'n4':20,
        'n5':21
    }
}

for key, value in favorite_number.items():
    print(key + "favorite numbers are: ", end ='')
    for numbers in value.values():
        print(str(numbers) + " ", end ='')
    print('.')

