# Task 2: Multiplication Quiz
from random import randint

number1 = randint(0, 9)
number2 = randint(0, 9)

answer = int(input(f"What is {number1} * {number2}? "))

if answer == number1 * number2:
    print("True - well done!")
else:
    print(f"False - {number1} * {number2} is {number1 * number2}")
