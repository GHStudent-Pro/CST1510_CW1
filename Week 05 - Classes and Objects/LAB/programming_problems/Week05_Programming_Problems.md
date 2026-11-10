# Week 5 – Classes and Objects – Programming Problems

## Task 1: Student Class

Create a class `Student` with attributes `name` and `age` set in `__init__`. Create two student objects and print their attributes using dot notation.

## Task 2: Dog Class

Create a class `Dog` with `name` and `age`, and two methods:
- `bark()` prints "<name> says Woof!"
- `birthday()` increases the dog's age by 1

Create a dog, call `bark()`, call `birthday()` twice and print the new age.

## Task 3: Rectangle Class

Create a class `Rectangle` with `width` and `height` and methods `area()` and `perimeter()`. Create a list of 4 rectangles and print the area and perimeter of each, then print which rectangle has the largest area.

## Task 4: Bank Account

Create a class `BankAccount` with `owner` and `balance` (default 0) and methods:
- `deposit(amount)`
- `withdraw(amount)` – refuse the withdrawal and print a message if there is not enough money
- `show_balance()`

Test it with several deposits and withdrawals, including one that should fail.

## Task 5: Printing Objects with `__str__`

Add a `__str__` method to the `Student` class from Task 1 (e.g. "Alice (age 19)"). Create a list of 5 students and print them with a loop using `print(student)`.

## Task 6: Library Books

Create a class `Book` with `title`, `author` and `is_available` (default `True`) and methods `borrow()` and `return_book()`. Store 4 books in a list, then:
1. Borrow one book and try to borrow it a second time (print a message).
2. Print all books that are currently available.
3. Ask the user for an author and print all of that author's books.

## Task 7: Shop Inventory

Create a class `Product` with `name`, `price` and `quantity`, and methods `total_value()` and `apply_discount(percent)` (changes the product's own price). Store 5 products in a list and:
1. Print the total value of the whole inventory.
2. Apply a 10% discount to every product and print the new prices.

## Task 8: Cyber: Login Attempt Tracker

Create a class `Account` with `username`, `password` and `failed_attempts`. Add a method `login(password)` that returns `True` for the correct password and resets the failed attempts, otherwise increases `failed_attempts`. After 3 failed attempts the account becomes locked and every later login is refused. Test the class with correct and incorrect passwords.

## Task 9: Gradebook

Create a class `Course` that stores a course name and a list of `Student` objects (each with a name and a list of marks). Add methods `add_student()`, `average_mark(student_name)` and `top_student()`. Create a course with at least 4 students and print each student's average and the top student.
