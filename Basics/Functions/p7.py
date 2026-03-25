#Function with *args
#Problem: Write a function that takes variable number of arguments and returns their sum. 

def sum_of_numbers(*args): # *chai will also work , * is important for multiple arguments   
    print(args) # this will print the tuple of arguments passed to the function
    return sum(args)

print(sum_of_numbers(1,2,3,))
print(sum_of_numbers(4,5,6,7))
print(sum_of_numbers(10,20))
