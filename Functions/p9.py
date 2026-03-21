#Generator function with yield

# write a function that yields even numbers up to a specified limit 

def even_generator(limit):
    for i in range(2, limit + 1,2):
        yield i # use of yield allows the function to return a generator object that can be iterated over to get the even numbers one by one , it maintains the state of the function in memory 

for num in even_generator(10):
    print(num)