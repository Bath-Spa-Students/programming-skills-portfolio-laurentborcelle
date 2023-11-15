# CS : 1
Sales = float (input("Enter sales: "))
bonus = 0
if Sales > 89000:
   bonus = 9500
else:
   bonus = 0
print ("Your bonus: "+str(bonus ) )



# Nested Decision Structure
earning = int(input("Enter your earning per year: "))
work_experience = float (input("Enter your work experience: "))

if earning > 30000:
  if work_experience >=5:
      print ("You are eligible for loan")
  else
     print ("Sorry, your work experience is less than 2 years")
else:
     print ("Your earning is less than 30000") 