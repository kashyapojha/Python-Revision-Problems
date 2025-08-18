# Age Group Classification 
# Classify a person's age group : Child(<13),Teenager(13-18),Adult(20-59),Senior(80+)

age=20

if age < 13:
    print("Child")
elif 13 <= age < 18:
    print("Teenager")
elif 18 <= age < 60:
    print("Adult")
else:
    print("Senior")
