# Task 1: Reverse Input

numbers = []
while True:
    number = int(input("Enter an integer (0 to finish): "))
    if number == 0:
        break
    numbers.append(number)

for number in reversed(numbers):
    print(number)
