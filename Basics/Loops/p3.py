# Multiplication table printer 
# print the multiplication table of a given number up to 10 , but skip the fifth iteration 

number = 5 

for i in range(1 , 11):
    if i == 5:
        continue
    print(number, 'x' , i , '=' , number * i)

