 # Validate input 
# keep asking the user for input until they enter a number between 1 and 10 

number = int(input("Enter a value between 1 and 10"))
if 1 <= number <= 10:
    print("Thanks")
else:
    print("Invalid input")
