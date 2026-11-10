# Task 2: Dice Throws
import random

throws = []
for _ in range(7):
    throws.append(random.randint(1, 6))

random.shuffle(throws)
print("Shuffled:", throws)

throws.sort(reverse=True)
print("Descending:", throws)

print("Occurrences:")
for face in range(1, 7):
    print(f"  {face}: {throws.count(face)}")
