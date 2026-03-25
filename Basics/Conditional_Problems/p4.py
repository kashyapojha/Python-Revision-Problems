#Fruit Ripeness checker
# determine it a fruit is ripe , or unripe on its color. (e.g., Banana:Green-> Unripe , Yellow-> Ripe , Brown -> Overripe)

fruit = "Banana"
color = "Green"

if color == "Green":
    print("Unripe")
elif color == "Yellow":
    print("Ripe")
elif color == "Brown":
    print("Overripe")
else:
    print("Unknown")