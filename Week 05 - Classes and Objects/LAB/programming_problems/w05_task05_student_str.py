# Task 5: Printing Objects with __str__


class Student:
    """A student with a name and an age."""

    def __init__(self, name, age):
        """Store the name and age on the object."""
        self.name = name
        self.age = age

    def __str__(self):
        """Return a readable description used by print()."""
        return f"{self.name} (age {self.age})"


students = [Student("Alice", 19), Student("Bob", 21), Student("Chloe", 20),
            Student("Dan", 22), Student("Eve", 18)]

for student in students:
    print(student)
