# Task 9: Gradebook


class Student:
    """A student with a name and a list of marks."""

    def __init__(self, name, marks):
        """Store the name and marks on the object."""
        self.name = name
        self.marks = marks

    def average(self):
        """Return the average mark."""
        return sum(self.marks) / len(self.marks)


class Course:
    """A course holding a list of Student objects."""

    def __init__(self, name):
        """Store the course name and start with no students."""
        self.name = name
        self.students = []

    def add_student(self, student):
        """Add a Student to the course."""
        self.students.append(student)

    def average_mark(self, student_name):
        """Return the average for the named student, or None if not found."""
        for student in self.students:
            if student.name == student_name:
                return student.average()
        return None

    def top_student(self):
        """Return the student with the highest average."""
        return max(self.students, key=lambda student: student.average())


course = Course("CST1510")
course.add_student(Student("Alice", [85, 92, 78]))
course.add_student(Student("Bob", [70, 65, 80]))
course.add_student(Student("Chloe", [95, 88, 91]))
course.add_student(Student("Dan", [60, 72, 68]))

print(f"Course: {course.name}")
for student in course.students:
    print(f"  {student.name:<6} average: {course.average_mark(student.name):.2f}")

best = course.top_student()
print(f"Top student: {best.name} ({best.average():.2f})")
