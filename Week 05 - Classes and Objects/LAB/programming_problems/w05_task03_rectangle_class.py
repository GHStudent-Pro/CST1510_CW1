# Task 3: Rectangle Class


class Rectangle:
    """A rectangle with a width and a height."""

    def __init__(self, width, height):
        """Store the width and height on the object."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter."""
        return 2 * (self.width + self.height)


rectangles = [Rectangle(4, 5), Rectangle(2.5, 8), Rectangle(10, 1), Rectangle(6, 6)]

for number, rectangle in enumerate(rectangles, start=1):
    print(f"Rectangle {number} ({rectangle.width} x {rectangle.height}): "
          f"area = {rectangle.area()}, perimeter = {rectangle.perimeter()}")

largest = max(rectangles, key=lambda r: r.area())
print(f"Largest area: {largest.width} x {largest.height} = {largest.area()}")
