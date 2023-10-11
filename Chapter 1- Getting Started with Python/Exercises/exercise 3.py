# Exercise 3: Print date and Time 

# Answers:

from datetime import date
today = (date.today())
d = today.strftime("%B %d, %Y")
print(d)

from datetime import datetime
now = datetime.now()
t = now.strftime("%H:%M:%S")
print(t)
