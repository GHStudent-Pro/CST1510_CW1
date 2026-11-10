# Task 1: Password Strength Checker

password = input("Enter a password: ")

# Check 12 first, otherwise a 12+ character password would stop at "Moderate"
if len(password) >= 12:
    print("Strong")
elif len(password) >= 8:
    print("Moderate")
else:
    print("Weak")
