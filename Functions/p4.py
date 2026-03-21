# Function Returning multiple values 
# Create a function that returns both the area and circumference of a circle given its radius.

def circle(radius):
    pi = 3.14
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return area, circumference
print(circle(5))
