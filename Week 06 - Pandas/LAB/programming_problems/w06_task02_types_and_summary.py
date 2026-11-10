# Task 2: Data Types and Summary
from pathlib import Path
import pandas as pd

pd.set_option("display.max_columns", None)   # show every column
pd.set_option("display.width", 200)

DATA = Path(__file__).resolve().parents[3] / "Programming Problems-20261110" / "DATA"

df = pd.read_csv(DATA / "students.csv")

print(df.dtypes)
print()
print(df.describe())
print()
print(f"Average grade: {df['Grade'].mean():.2f}")
print(f"Maximum attendance: {df['Attendance'].max()}")
print(f"Youngest student's age: {df['Age'].min()}")
