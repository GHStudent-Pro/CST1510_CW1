# Task 1: Quiz - practise +, -, *, /, ** and %
from random import randint


def add(a, b):
    """Return a + b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


def multiply(a, b):
    """Return a * b."""
    return a * b


def divide(a, b):
    """Return a / b rounded to 2 decimal places, or None if b is 0."""
    if b == 0:
        return None
    return round(a / b, 2)


def exponent(a, b):
    """Return a to the power of b."""
    return a ** b


def remainder(a, b):
    """Return a % b, or None if b is 0."""
    if b == 0:
        return None
    return a % b


def show_menu():
    """Print the list of operations."""
    print("\n1) Addition  2) Subtraction  3) Multiplication")
    print("4) Division  5) Exponent     6) Remainder     q) Quit")


def ask_question(symbol, operation):
    """Ask one question and return True if it was answered correctly."""
    number1 = randint(0, 9)
    number2 = randint(0, 9)
    correct = operation(number1, number2)
    if correct is None:
        print(f"{number1} {symbol} {number2}: cannot divide by zero - skipping this one.")
        return False
    try:
        answer = float(input(f"What is {number1} {symbol} {number2}? "))
    except ValueError:
        print("That was not a number.")
        return False
    if abs(answer - correct) < 0.01:
        print("Correct!")
        return True
    print(f"Wrong - the answer is {correct}")
    return False


def main():
    """Run the quiz until the user chooses to quit."""
    operations = {
        "1": ("+", add), "2": ("-", subtract), "3": ("*", multiply),
        "4": ("/", divide), "5": ("**", exponent), "6": ("%", remainder),
    }
    score = 0
    asked = 0
    while True:
        show_menu()
        choice = input("Choose an operation: ").strip().lower()
        if choice == "q":
            break
        if choice not in operations:
            print("Please choose 1-6 or q.")
            continue
        symbol, operation = operations[choice]
        asked += 1
        if ask_question(symbol, operation):
            score += 1
    print(f"\nFinal score: {score} out of {asked}")


if __name__ == "__main__":
    main()
