# Transportation mode selection 
# problem :- choose a mode of transportation based on the distance (e.g:- <3km : Walk , 3-15km: Bike , >15 km car)

distance = 5 

if distance < 3:
    transportation = "Walk"
elif 3 <= distance <= 15:
    transportation = "Bike"
else:
    transportation = "Car"

print("AI recommends:", transportation)