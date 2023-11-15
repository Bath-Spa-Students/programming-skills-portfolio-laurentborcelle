# Exercise 5: Cities

# Answers:

def describe_city(city, country = 'france'):
    message = f"{city.title()} is in {country.title()}."
    print(message)

describe_city('paris')
describe_city('doha', 'qatar')
describe_city('cannes')