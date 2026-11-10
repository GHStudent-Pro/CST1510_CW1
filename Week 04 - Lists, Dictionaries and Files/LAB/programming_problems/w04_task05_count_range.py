# Task 5: Count Range


def countRange(values, minimum, maximum):
    """Return how many values are >= minimum and < maximum."""
    count = 0
    for value in values:
        if minimum <= value < maximum:
            count += 1
    return count


def main():
    """Demonstrate countRange on integer and float lists."""
    print(countRange([1, 2, 3, 4, 5, 6], 2, 5))            # 3 (2, 3, 4)
    print(countRange([10, 20, 30, 40], 15, 40))            # 2 (20, 30)
    print(countRange([0.5, 1.5, 2.5, 3.5], 1.0, 3.0))      # 2 (1.5, 2.5)
    print(countRange([-2.2, -1.1, 0.0, 1.1], -2.0, 1.1))   # 2 (-1.1, 0.0)
    print(countRange([], 0, 10))                           # 0


main()
