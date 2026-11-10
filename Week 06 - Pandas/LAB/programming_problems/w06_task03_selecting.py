# Task 3: Selecting Columns and Rows
from pathlib import Path
import pandas as pd

pd.set_option("display.max_columns", None)   # show every column
pd.set_option("display.width", 200)

DATA = Path(__file__).resolve().parents[3] / "Programming Problems-20261110" / "DATA"

df = pd.read_csv(DATA / "students.csv")

grades_df = df[["Name", "Course", "Grade"]]
print(grades_df.head(8))

print("\nRows at positions 5 to 9:")
print(df.iloc[5:10])

print("\nName and City of the student at index 3:")
print(df.loc[3, ["Name", "City"]])
