"""
RECORD CHECK  -  my version
===========================

Name  :  Mahin Zaeem
Lane  :  AI
Date  :  04/11/2026

Run it:   python template.py

Loads datasets from datasets.txt (one per line: name,rows_loaded,rows_expected)
as Record objects and prints a report for each one.
"""

DATA_FILE = "datasets.txt"

# ====================================================================== CLASS

class Record:
    """One dataset: its name, rows loaded and rows expected."""

    over_limit_count = 0   # class-level: shared running total across every Record

    def __init__(self, label, value, limit):
        """Store the dataset name, rows loaded and rows expected on the object."""
        self.label = label
        self.value = value
        self.limit = limit

    def missing(self):
        """Return how many rows are missing (negative if there are extra)."""
        return self.limit - self.value

    def percent(self):
        """Return the rows loaded as a percentage of the rows expected."""
        return (self.value / self.limit) * 100

    def status(self):
        """Return OVER LIMIT (100%+), WARNING (90%+) or OK."""
        percent = self.percent()
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS

def load_records(path):
    """Read name,rows_loaded,rows_expected lines from a file into a list of Records."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records


records = load_records(DATA_FILE)


# ==================================================================== OUTPUT

for record in records:
    status = record.status()   # call once, then reuse the variable

    if status == "OVER LIMIT":
        Record.over_limit_count += 1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Rows loaded :  {record.value:>10.2f}")
    print(f"  Expected    :  {record.limit:>10.2f}")
    print(f"  Missing     :  {record.missing():>+10.2f}")
    print(f"  Percent     :  {record.percent():>10.2f} %")
    print(f"  Status      :  {status:>10}")
    print("=" * 34)

print(f"\nDatasets over limit: {Record.over_limit_count} of {len(records)}")
