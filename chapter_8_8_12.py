# 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, using a different number of arguments each time.

def sandwich_toppings(*toppings):
    print("Toppings: ", end = '')

    for topping in toppings:
        print(" - " + topping, end ='' )
    print("\n")


sandwich_toppings('pepperoni', 'bacon', 'cheese')

sandwich_toppings('pepperoni', 'bacon', 'eggs', 'cheese')

sandwich_toppings('pepperoni', 'bacon', 'eggs', 'cheese', 'tomato')

