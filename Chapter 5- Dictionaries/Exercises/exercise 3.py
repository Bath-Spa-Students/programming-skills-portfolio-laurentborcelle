# Exercise 3: Glossary 2

# Answer: 

# words: elif, iterable, append, nested, sequence, selection, repetition

glossary = {
    'Elif': ' is short for "else if" and is used when the first if statement is not true, but you want to check for another condition',
    'Iterable': ' is any Python object capable of returning its members one at a time, permitting it to be iterated over in a for-loop.',
    'Append': 'attaches an element to the end of the list.',
    'Nested': 'provides encapsulation and hide functions from external access.',
    'Sequence': 'is an ordered list of instructions.',
    'Selection': 'is used to select part of a program to be executed based on condition.',
    'Repetition': 'are used to repeat the same code multiple times in succession.'

}

for word, meaning in glossary.items():
    print (f"{word}:\n{meaning}\n")