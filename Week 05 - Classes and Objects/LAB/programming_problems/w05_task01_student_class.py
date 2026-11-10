# Task 1: Student Class


class Student:
    """A student with a name and an age."""

    def __init__(self, name, age):
        """Store the name and age on the object."""
        self.name = name
        self.age = age


student1 = Student("Alice", 19)
student2 = Student("Bob", 21)

print(student1.name, student1.age)
print(student2.name, student2.age)
