# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the name of a pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do print everything you know about each pet.

pet1 = {'pet_name':'godofredo', 'breed':'Cat', 'owner':'Luiza'}
pet2 = {'pet_name':'Au Au', 'breed':'Dog', 'owner':'Carol'}
pet3 = {'pet_name':'Flash', 'breed':'Snail', 'owner':'João'}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(pet['pet_name'])
    print(pet['breed'])
    print(pet['owner'])

    