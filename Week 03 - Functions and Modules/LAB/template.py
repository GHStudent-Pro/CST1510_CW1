"""
RECORD CHECK  -  my version
===========================

Name  :  Mahin Zaeem
Lane  :  AI
Date  :  21/10/2026

Run it:   python template.py

Checks how many rows of a dataset loaded compared with how many were expected.
Type "quit" as the dataset name to stop.
"""

# =================================================================== FUNCTIONS

def status_of(percent):
    """Return OVER LIMIT (100%+), WARNING (90%+) or OK for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(rows_loaded, rows_expected):
    """Return the missing rows and the loaded percentage."""
    missing_rows = rows_expected - rows_loaded
    loaded_percent = (rows_loaded / rows_expected) * 100
    return missing_rows, loaded_percent


def print_report(dataset_name, rows_loaded, rows_expected, missing_rows, loaded_percent, status):
    """Print the bordered report for one dataset."""
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


# ===================================================================== MAIN

over_limit_count = 0

while True:
    # ---------------------------------------------------------------- INPUT
    dataset_name = input("\nEnter the dataset name (or quit to stop): ")
    if dataset_name == "quit":
        break

    rows_loaded = float(input("Enter the rows loaded: "))
    rows_expected = float(input("Enter the rows expected: "))

    # -------------------------------------------------------------- PROCESS
    missing_rows, loaded_percent = check(rows_loaded, rows_expected)
    status = status_of(loaded_percent)

    if status == "OVER LIMIT":
        over_limit_count += 1

    # --------------------------------------------------------------- OUTPUT
    print_report(dataset_name, rows_loaded, rows_expected, missing_rows, loaded_percent, status)

print(f"\nDatasets over limit this session: {over_limit_count}")
