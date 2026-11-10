# Task 4: Lottery Ticket
import random

# random.sample picks 6 DIFFERENT numbers from 1-49
ticket = sorted(random.sample(range(1, 50), 6))
print("Your numbers:", " ".join(str(n) for n in ticket))
