"""
RECORD CHECK  -  my version
===========================

Name  :  Mahin Zaeem
Lane  :  AI
Date  :  28/10/2026

Run it:   python template.py

Loads datasets from datasets.txt (one per line: name,rows_loaded,rows_expected),
checks each one, prints a report, and writes the results to dataset_results.txt.
"""

DATA_FILE = "datasets.txt"
RESULTS_FILE = "dataset_results.txt"

# =================================================================== FUNCTIONS

def status_of(percent):
    """Return OVER LIMIT (100%+), WARNING (90%+) or OK for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check_record(rows_loaded, rows_expected):
    """Return the missing rows, the loaded percentage and the status."""
    missing_rows = rows_expected - rows_loaded
    loaded_percent = (rows_loaded / rows_expected) * 100
    return missing_rows, loaded_percent, status_of(loaded_percent)


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


def load_records(path):
    """Read name,rows_loaded,rows_expected lines from a file into a list of dicts."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({"label": label, "value": float(value), "limit": float(limit)})
    return records


# ====================================================================== STORE

try:
    records = load_records(DATA_FILE)
except FileNotFoundError:
    print(f"Could not find {DATA_FILE} - starting with no datasets.")
    records = []


# ============================================================ PROCESS + OUTPUT

over_limit_count = 0

with open(RESULTS_FILE, "w") as results:
    for record in records:
        missing_rows, loaded_percent, status = check_record(record["value"], record["limit"])

        print_report(record["label"], record["value"], record["limit"],
                     missing_rows, loaded_percent, status)

        results.write(f"{record['label']},{status}\n")

        if status == "OVER LIMIT":
            over_limit_count += 1

print(f"\nDatasets over limit: {over_limit_count} of {len(records)}")
print(f"Results written to {RESULTS_FILE}")
