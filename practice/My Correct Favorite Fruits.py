# Exercise 5: Favorite Fruit 

# Answer:

favorite_fruits = ['Strawberry', 'Avocado','Cherry']
favorite_fruits = input("Enter a list of your favorite fruits: ")
fruits_list = favorite_fruits.split()

fruits_list = [str(item) for item in fruits_list]

print ("You entered the list:", fruits_list)



if 'Strawberry' in favorite_fruits:
    print("You really like strawberries!")
if 'Avocado' in favorite_fruits:
    print("You really like avocadoes!")
if 'Peaches' in favorite_fruits:
    print("You really like peaches!")
if 'Apples' in favorite_fruits:
    print("You really like Apples!")
if 'Cherry' in favorite_fruits:
    print("You really like cherries!")
