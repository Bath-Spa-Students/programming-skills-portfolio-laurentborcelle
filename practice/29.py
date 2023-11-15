# Create a list of dictionaries to store pet information
pets = []

# Function to add a pet to the list
def add_pet(animal_type, name, owner, weight, eats):
    pet = {
        'animal type': animal_type,
        'name': name,
        'owner': owner,
        'weight': weight,
        'eats': eats,
    }
    pets.append(pet)

# Add individual pets to the list
add_pet('python', 'john', 'guido', 43, 'bugs')
add_pet('chicken', 'clarence', 'tiffany', 2, 'seeds')
add_pet('dog', 'peso', 'eric', 37, 'shoes')

# Display information about each pet
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
