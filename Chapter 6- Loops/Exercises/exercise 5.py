# Exercise 5: No Pastrami

# Answers:

sandwich_orders = ['Pastrami','Turkey Ham', 'Tuna','Pastrami', 'Club', 'Panini','Pastrami','Hamburger','Tonkatsu','Bagel']
finished_sandwiches = []

print ("Apologies, the deli has ran out of pastrami.")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

print ("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print (f"\nWe are working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print ("\n")
for sandwich in finished_sandwiches:
    print (f"\nWe have made your {sandwich} sandwich.")