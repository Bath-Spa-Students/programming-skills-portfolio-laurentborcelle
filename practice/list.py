# Homogenous List
designers = ["CHANEL", "DIOR", "YSL" ]
print(designers)

# Heterogenous List
mylist = ["34","5353.4","Pasta"]
print (mylist)

# Repetition Operator * To repeat data
numbers = [3,4,5,6]
new_numbers = numbers * 2
print (new_numbers)


numbers = [3,4,5,6]
new_numbers = numbers * 5
print (new_numbers)


# Positive Indexing

numbers =[5,6,3,7,9]
print (numbers[3])


# Negative Indexing starts from -1, because 0 is a non-negative integer
numbers =[5,6,3,7,9]
print (numbers[-3])


# lens function
numbers =[5,6,3,7,9]
print ("number of elements in a list :" ,len(numbers))


# Mutability (Changeable)

numbers =[5,6,7,8,3,4]
numbers[-3]=1
numbers[-1]=9
print(numbers)


# Concatenation
List_1 = [3,4,5,6,7]
List_2 = [12,11,10,9,8]

List_3=List_1+List_2
print(List_3)


# List_slicing * To use one part of the list
new_list = [1,2,3,8,6,23]
result=new_list [-5:6]
print(result)

# Find elements in list * if operator
new_list1 =[1,2,3,4,5,6,7,8,9]
if 10 in new_list1:
    print("found")
else:
    print ("Not found")

# (Not in) operator

new_list2 =[1,2,3,4,5,6,7,8,9]
if 20 not in new_list2:
    print("yes")
else:
    print("no")




