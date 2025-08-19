#Password strength checker 
#Problem: Check the strength of a password based on length and character variety

password = "P@ssw0rd123"

if len(password) < 8:
    strength = "Weak"
elif (any(c.isdigit() for c in password) and
      any(c.isupper() for c in password) and
      any(c.islower() for c in password) and
      any(not c.isalnum() for c in password)):
    strength = "Strong"
else:
    strength = "Moderate"

print("Password strength:", strength)