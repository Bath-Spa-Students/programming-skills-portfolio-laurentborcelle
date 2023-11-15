# Exercise 1: Pizza Toppings

# Answers:

prompt = "\nWhat topping would you like on your pizza?"

prompt += "\nEnter 'quit' after choosing all your toppings: "

while True:
    
    pztopping = input(prompt)
    if pztopping != 'quit':
        print (" The " + pztopping + " will be added to your pizza.")
    else:
        break
