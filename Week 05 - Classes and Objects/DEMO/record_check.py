"""
RECORD CHECK  -  Week 5 version
================================
Run it with:    python record_check.py

    Week 1   input, calculate, print
    Week 2   it can make decisions
    Week 3   it is built from functions
    Week 4   it reads many records from a file
    Week 5   it becomes a reusable component        <- this version
    Week 6   it does the whole job in a few lines

Last week this was four loose functions and a handful of variables sitting
next to each other at the bottom of the file - load_records, check_record,
print_report, a records list, an over_limit_count. Nothing tied them
together except that they happened to run one after another.

This version bundles all of that into ONE thing: a RecordChecker. Its data
(the path, the records, the count) and the actions that belong to that data
(load, check, run) now live together, on the object.

The whole program becomes two lines:

    checker = RecordChecker("records.txt")
    checker.run()

You could make a second RecordChecker, for a different file or a different
warning threshold, and it would keep its own records and its own count -
completely separately from the first one.
"""

class RecordChecker:
    """Loads records from a file and checks each one against its limit."""

    def __init__(self, path, warning_at=90):
        self.path = path
        self.warning_at = warning_at
        self.records = []
        self.over_limit_count = 0

    def load(self):
        """Read label,value,limit lines from self.path into self.records."""
        with open(self.path) as f:
            for line in f:
                label, value, limit = line.strip().split(",")
                self.records.append({
                    "label": label,
                    "value": float(value),
                    "limit": float(limit),
                })

    def check(self, record):
        """Work out the difference, percentage and status for one record."""
        difference = record["value"] - record["limit"]
        percent    = (record["value"] / record["limit"]) * 100

        if percent >= 100:
            status = "OVER LIMIT"
        elif percent >= self.warning_at:
            status = "WARNING"
        else:
            status = "OK"

        return difference, percent, status

    def print_report(self, record, difference, percent, status):
        """Print one bordered report. Nothing is worked out in here - only shown."""
        print()
        print("=" * 34)
        print(f"  RECORD CHECK  -  {record['label']}")
        print("=" * 34)
        print(f"  Value       : {record['value']:>10.2f}")
        print(f"  Limit       : {record['limit']:>10.2f}")
        print(f"  Difference  : {difference:>+10.2f}")
        print(f"  Of limit    : {percent:>9.1f} %")
        print(f"  Status      : {status:>10}")
        print("=" * 34)
        print()

    def run(self):
        """Load, check and report on every record, then print a summary."""
        self.load()
        for record in self.records:
            difference, percent, status = self.check(record)
            self.print_report(record, difference, percent, status)
            if status == "OVER LIMIT":
                self.over_limit_count += 1
        print(f"Checked {len(self.records)} records. {self.over_limit_count} were over limit.")


checker = RecordChecker("records.txt")
checker.run()
