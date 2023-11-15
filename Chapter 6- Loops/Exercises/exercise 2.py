# Exercise 2: Movie Tickets

# Answers:

prompt = "\nEnter your age."

prompt += "\nEnter 'quit' when you are finished: "

while True:
    
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print ("Your ticket is free.")
    elif age < 13:
        print ("The ticket costs $10.")
    else:
        print ("The ticket costs $15.")