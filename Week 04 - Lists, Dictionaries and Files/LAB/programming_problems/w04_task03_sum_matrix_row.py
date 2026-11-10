# Task 3: Sum of a Matrix Row


def sum_row(matrix, rowIndex):
    """Return the sum of the elements in one row of the matrix."""
    return sum(matrix[rowIndex])


matrix = []
print("Enter a 4-by-4 matrix, one row at a time (4 numbers separated by spaces):")
for row in range(4):
    values = input(f"Row {row}: ").split()
    matrix.append([float(value) for value in values])

for row in range(4):
    print(f"Sum of the elements in row {row} is {sum_row(matrix, row)}")
