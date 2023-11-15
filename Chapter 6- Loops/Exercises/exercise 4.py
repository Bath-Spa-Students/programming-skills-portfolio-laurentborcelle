# Exercise 4: Deli

# Answers:

sandwich_orders = ['\nTurkey Ham', '\nTuna', '\nClub', '\nPanini','\nHamburger','\nTonkatsu','\nBagel']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print (f"\nWe are working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

    
print ("\n")
print ("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print (sandwich)


print ("\n")
for sandwich in finished_sandwiches:
    print (f"\nWe have made your {sandwich} sandwich.")