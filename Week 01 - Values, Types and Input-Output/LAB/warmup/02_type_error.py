# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

value = int(input("Value: "))

print(value + 1)

# To do addition in the print statement, the value variable was not enclosed in parentheses. This means the script thinks of it as interger or float.
# However the variable being saved before was a string. So to fix this i changed the variable type to an interger. 