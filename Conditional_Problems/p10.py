#Pet food recommendation system
#Problem: Suggest pet food based on pet type and size

pet_type = "Dog"
pet_size = "Large"

if pet_type == "Dog":
    if pet_size == "Small":
        food = "Small Dog Food"
    elif pet_size == "Medium":
        food = "Medium Dog Food"
    else:
        food = "Large Dog Food"
else:
    food = "Cat Food"

print("Recommended food:", food)
