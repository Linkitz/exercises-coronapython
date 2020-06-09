# 6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program or improving the formatting of the output.

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
        'n5':21,
        'n6':33
    }
}

for key, value in favorite_number.items():
    print(key + "favorite numbers are: ", end ='')
    for numbers in value.values():
        print(str(numbers) + " ", end ='')
    print('.')