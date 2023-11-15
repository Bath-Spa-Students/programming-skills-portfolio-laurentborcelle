password = "SecretWord"
guess = "1234"
print(guess != password)


password = "SecretWord"
guess = input()
while guess != password:  
  guess = input() 
print("Access Granted")



for box in range(50):
    print("Package A")

print("Task complete")


age = 22
if age >= 18:
  print("Regular price")
else:
  print("Discount")