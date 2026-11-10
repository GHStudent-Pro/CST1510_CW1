"""
RECORD CHECK  -  my version
===========================

Name  :  Mahin Zaeem
Lane  :  AI
Date  :  14/10/2026

Run it:   python template.py

Checks how many rows of a dataset loaded compared with how many were expected.
Type "quit" as the dataset name to stop.
"""

# Counts how many datasets came back OVER LIMIT during this run
over_limit_count = 0

while True:
    # ================================================================ INPUT
    dataset_name = input("\nEnter the dataset name (or quit to stop): ")

    # Check for quit before asking for the numbers
    if dataset_name == "quit":
        break

    rows_loaded = float(input("Enter the rows loaded: "))
    rows_expected = float(input("Enter the rows expected: "))

    # ============================================================== PROCESS
    missing_rows = rows_expected - rows_loaded
    loaded_percent = (rows_loaded / rows_expected) * 100

    # Check 100% first: Python runs the first True branch and skips the rest
    if loaded_percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif loaded_percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    # =============================================================== OUTPUT
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {dataset_name}")
    print("=" * 34)
    print(f"  Rows loaded :  {rows_loaded:>10.2f}")
    print(f"  Expected    :  {rows_expected:>10.2f}")
    print(f"  Missing     :  {missing_rows:>+10.2f}")
    print(f"  Percent     :  {loaded_percent:>10.2f} %")
    print(f"  Status      :  {status:>10}")
    print("=" * 34)

# Printed once, after the loop ends
print(f"\nDatasets over limit this session: {over_limit_count}")
