age = 16
if age < 18: print("Apply Discount")
print("Proceed to Payment")

age = int(input())
if age < 18: 
  print("Junior discount")
elif age >= 75: 
  print("Senior discount")
else:
  print("No discount")


if age < 18:
  if is_student:
    print("20% discount")
  else:
    print("10% discount")
else:
  print("Regular price")