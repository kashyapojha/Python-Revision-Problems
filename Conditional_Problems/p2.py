#Movie Ticket Pricing
#Problem: Movie tickets are priced on age : $12 for adults (18 and over), $8 for children.Everyone gets $2 discount on wednesday 

age = 26
day = "Wednesday"

price = 12  if age >= 18 else 8

if day == "Wednesday":
    price -= 2

print("Ticket Price: $", price)