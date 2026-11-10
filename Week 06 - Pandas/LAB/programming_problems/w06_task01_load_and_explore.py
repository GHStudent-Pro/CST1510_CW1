# Task 1: Load and Explore
from pathlib import Path
import pandas as pd

pd.set_option("display.max_columns", None)   # show every column
pd.set_option("display.width", 200)

DATA = Path(__file__).resolve().parents[3] / "Programming Problems-20261110" / "DATA"

df = pd.read_csv(DATA / "students.csv")

print("First 5 rows:")
print(df.head())
print("\nLast 3 rows:")
print(df.tail(3))
print(f"\nShape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
