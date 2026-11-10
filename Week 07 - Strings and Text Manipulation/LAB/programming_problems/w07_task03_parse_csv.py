# Task 3: Parse CSV Data

csv_data = [
    "Alice,25,London,Data Analyst",
    "Bob,30,Paris,Engineer",
    "Charlie,22,Berlin,Student"
]

for row in csv_data:
    name, age, city, job = row.split(",")
    print(f"{name} is a {age} year old {job} based in {city}")
