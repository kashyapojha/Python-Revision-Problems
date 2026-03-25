# Property Decorators 
# use a property decorator in the Car class to make the model attribute read-only 


class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "A car is a mean of transportation"

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


# Objects
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
my_car = Car("Tata", "Safari")
Car("Tata", "Nexon")   # just to increase total_car count

# Outputs
print(my_car.model)                     # Read-only property
print(Car.general_description())        # Static method
print(my_tesla.fuel_type())             # Method overriding
safari = Car("Tata", "Safari")
print(safari.fuel_type())               # Parent class method
print(Car.total_car)                    # Class variable