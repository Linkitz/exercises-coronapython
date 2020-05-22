# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 60). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
my_pizzas = ["Calabresa","Four Cheese","Atum"]
friend_pizzas = ["chocolate","Banana","Margherita"]
#
# • Add a new pizza to the original list.
my_pizzas.append("Portuguesa")
#
# • Add a different pizza to the list friend_pizzas.
friend_pizzas.append("Chief")
#
# • Prove that you have two separate lists. Print the message, My favorite pizzas are:, and then use a for loop to print the first list. Print the message, My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

for pizza in my_pizzas:
    print("My favorite pizzas are: " + pizza)

for pizza in friend_pizzas:
    print("My friend’s favorite pizzas are: " + pizza)