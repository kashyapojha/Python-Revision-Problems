# Basic:- Class and Object 
# Create a Car class with attributes like brand and model . Then create an instance of this class 

class Car:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")  # Object -1 
print(my_car.brand)
print(my_car.model)


my_new_car = Car("Tata", "Safari")   # Object -2 
print(my_new_car.brand)
print(my_new_car.model)




