#Weather Activity Suggestion 
# Suggest an activity based on weather (e.g, Sunny - Go for walk , Rainy- Read a book, Snowy- Build a snowman).

weather =input("Enter weather condition out of sunny , rainy or snowy:")



if weather == "Sunny":
    print("Activity: Go for a walk")
elif weather == "Rainy":
    print("Activity: Read a book")
elif weather == "Snowy":
    print("Activity: Build a snowman")
else:
    print("Activity: Stay indoors")

