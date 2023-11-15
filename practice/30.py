movies = ["Avatar", "Titanic", "Avengers"]
len(movies)
print(len(movies))

movie = "Avatar"
print(len(movie))


songs = ["Yesterday", "Hello", "Believer"]
songs.append("Imagine")


movies = ["Avatar", "Titanic", "Avengers"]
movies.append("Alien")
print(movies[3])

items = ["book", "pen", "pencil"]
items.insert(2,"marker")



colors = ["Red", "Blue", "Yellow"]
colors.insert(2, "Green")
colors.append("Black")
print(colors[3])




def greet(name="Guest"):
  print("Welcome", name)
greet()

def greet(name="Guest"):
  print("Welcome", name)
greet("Anna")


word = 'motorbike'
print(word.find('r'))

book = "1984"
print(len(book))


movies=["Avatar","Titanic","Alien"]
movies.append("Avengers")
movies.insert(2, "Terminator")
print(movies[3])