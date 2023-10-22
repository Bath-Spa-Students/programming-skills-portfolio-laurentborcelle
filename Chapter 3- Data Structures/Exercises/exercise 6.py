# Exercise 6: Shrinking Guest List

# Answers:

guest_list = ['Olivier Rousteing', 'Donatella Versace', 'Elsa Schiaparelli', 'Vivienne Westwood']

name = guest_list[0].title()
print (name + ", we are pleased to invite you to dinner.")

name = guest_list[1].title()
print (name + ", we are pleased to invite you to dinner.")

name = guest_list[2].title()
print (name + ", we are pleased to invite you to dinner.")

name = guest_list[3].title()
print (name + ", we are pleased to invite you to dinner.")

name = guest_list[-4].title()
print ("\nApologies, " + name + " is unable to make it to dinner.")

del (guest_list[-4])
guest_list.insert (-4, 'Zuhair Murad')


name = guest_list[0].title()
print ("\n" + name + ", we are pleased to invite you to dinner.")

name = guest_list[1].title()
print (name + ", we are pleased to invite you to dinner.")

name = guest_list[2].title()
print (name + ", we are pleased to invite you to dinner.")

name = guest_list[3].title()
print (name + ", we are pleased to invite you to dinner.")

#

print ("\nApologies, we are only able to invite two people to dinner.")

name = guest_list.pop()
print ("Apologies, " + name.title() + " there is no longer any room at the table.")

name = guest_list.pop()
print ("Apologies, " + name.title() + " there is no longer any room at the table.")

name = guest_list[0].title()
print (name + ", we are pleased to invite you to dinner.")

name = guest_list[1].title()
print (name + ", we are pleased to invite you to dinner.")


del (guest_list[0])
del (guest_list[0])

print (guest_list)