# Function with **kwargs
# Create a function that accepts any nuber of keyword arguments and prints them in the format key : value.


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")



print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer", enemy = "Dr. Jackaal") # this will give an error because the function is defined to take only 2 arguments