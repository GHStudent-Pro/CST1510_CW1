"""
RECORD CHECK  -  my version
===========================

Name  :  Mahin Zaeem
Lane  :  AI
Date  :  11/11/2026

Run it:   python template.py

Loads datasets.csv (dataset,rows_loaded,rows_expected), works out how much of
each dataset loaded, flags the ones that need attention, and saves a report
CSV and a bar chart of the statuses.
"""

import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "datasets.csv"
REPORT_FILE = "dataset_report.csv"
CHART_FILE = "dataset_status_counts.png"

# ==================================================================== LOAD

df = pd.read_csv(DATA_FILE)


# ================================================================= PROCESS

df["percent"] = ((df["rows_loaded"] / df["rows_expected"]) * 100).round(2)

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK")
)


# ================================================================== OUTPUT

print("All datasets:")
print(df)

print("\nDatasets that need attention:")
print(df[df["status"] != "OK"])

print("\nDatasets per status:")
status_counts = df.groupby("status").size()
print(status_counts)

df.to_csv(REPORT_FILE, index=False)
print(f"\nFull report saved to {REPORT_FILE}")

status_counts.plot(kind="bar")
plt.title("Datasets per status")
plt.xlabel("Status")
plt.ylabel("Number of datasets")
plt.tight_layout()
plt.savefig(CHART_FILE)
print(f"Chart saved to {CHART_FILE}")
