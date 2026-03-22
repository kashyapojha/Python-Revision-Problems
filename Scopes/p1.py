"""
username = "chaiaurcode"

def func1():
    username = "chai"
print(username)  #   chaiaurcode 
func1() # no output because the function does not return anything and the variable username inside the function is local to that function and does not affect the global variable username outside the function.



x = 99
def func2(y):
    z = x + y
    return z

result = func2(1)  # This will print 100
print(result)


def func3():
    global x  # This line tells Python that we want to use the global variable x instead of creating a new local variable with the same name.
    return x
result = func3()
print(result)

def func4():
    global x
    x = 100
    return x
result = func4()
print(result)  # this will print 100 because the global variable x has been modified to 100 inside the function func4() and this change is reflected when we call func3() again which returns the value of x.
result = func3()
print(result)  # this will also print 100 because the global variable x has been modified


def f1():
   x = 88
   def f2():
    print(x)
    return f2
myResult = f1()
print(myResult) 

"""