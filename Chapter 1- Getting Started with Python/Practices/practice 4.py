# Q4: Compute the area of the triangle

# Answers:

import math

def triangle_area (a,b,c):
 
 s = (a + b + c) / 2
 area = math.sqrt(s*(s-a)*(s-b)*(s-c))
 return area

a = float(input("Enter the first side of the triangle:"))
b = float(input("Enter the second side of the triangle:"))
c = float(input("Enter the third side of the triangle:"))

area = triangle_area (a,b,c)
print('The area of the triangle is %0.3f' %area)



