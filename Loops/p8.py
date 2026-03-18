#Prime number 
# check if a number is prime or not 

num = int(input("Enter a number: "))

is_prime = True
if num > 1:
    for i in range(2 , num):
        if (num % i) == 0:
            is_prime = False 
print(is_prime)