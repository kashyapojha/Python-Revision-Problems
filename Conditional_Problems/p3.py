# Grade Calculator 
# Assign a letter grade based on student's score: A(90-100), B(80-89), C(70-79), D(60-69), F(<60)
score = 101

if score >= 101:
    print("Invalid score")
    exit()

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")
