# Task 2: Dog Class


class Dog:
    """A dog with a name and an age."""

    def __init__(self, name, age):
        """Store the name and age on the object."""
        self.name = name
        self.age = age

    def bark(self):
        """Print the dog's bark."""
        print(f"{self.name} says Woof!")

    def birthday(self):
        """Add one year to the dog's age."""
        self.age += 1


dog = Dog("Rex", 3)
dog.bark()
dog.birthday()
dog.birthday()
print(f"{dog.name} is now {dog.age}")
