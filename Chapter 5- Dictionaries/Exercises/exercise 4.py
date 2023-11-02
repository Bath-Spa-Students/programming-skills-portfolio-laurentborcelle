# Exercise 4: Rivers 

# Answer:

major_rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China',

    }

for river, country in major_rivers.items():
    print ("The " + river.title() + " flows through " + country.title() + ".")

print ("\nThe following rivers are included in this data set:")
for river in major_rivers.keys():
    print ("- " + river.title())

print ("\nThe following countries are included in this data set:")
for country in major_rivers.values():
    print ("- " + country.title())