#Coffee Customization 

# Customize a coffee order. "Small","Medium","Large" with an option for "extra shots" of expressp

order_size = "Medium"
extra_shots = True

if extra_shots:
    coffee = order_size + " with extra shots"

else: 
    coffee= order_size + "coffee"

print("Order:",  coffee)
