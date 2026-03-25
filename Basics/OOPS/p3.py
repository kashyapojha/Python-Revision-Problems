#Inheritance
# Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size
#encapsulation
#Modify the Car class to encapsulate the brand attribute , making it private , and provide  getter method for it 


class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    
    def get_brand(self):
        return self.__brand + "!"
    
    
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    



class ElectricCar(Car):
    def __init__ (self,brand, model , battery_size):
        super().__init__(brand , model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S" , "85kWh")
# print(my_tesla.model)
# print(my_tesla.full_name())

print(my_tesla.get_brand())
# print(my_tesla.__brand)





