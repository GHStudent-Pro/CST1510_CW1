"""
LOADING OBJECTS FROM A FILE
=============================
Week 4's load_records built a list of dicts. This does the same job, but
builds a list of Record OBJECTS instead - one Record per line.
Run:  python 02_loading_objects_from_a_file.py
(needs sample_records.txt in the same folder)
"""

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


def load_records(path):
    """Read label,value,limit lines from a file and return a list of Records."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))   # <- a Record, not a dict
    return records


# --- 1. Loading builds a list of objects -------------------------------

records = load_records("sample_records.txt")
print(len(records), "records loaded")
print(type(records[0]))     # __main__.Record


# --- 2. Processing each one - the method already knows its own data ---------

for record in records:
    print(record.label, record.status())


# --- 3. A summary, the same running-total pattern as always -----------

over_limit_count = 0
for record in records:
    if record.status() == "OVER LIMIT":
        over_limit_count += 1

print(f"{over_limit_count} of {len(records)} were over limit")


# --- 4. Same idea, three fields ---------------------------------------------
# Same shape - a list built by loading each line as one object.

class Reading:                                        # AI / Data Science
    def __init__(self, value):
        self.value = value

readings = [Reading(21.4), Reading(22.0), Reading(23.7)]
print(len(readings), "Reading objects loaded")

class LogEntry:                                       # Cyber Security
    def __init__(self, ip, result):
        self.ip = ip
        self.result = result

entries = [LogEntry("10.0.0.5", "FAILED"), LogEntry("10.0.0.9", "OK")]
print(len(entries), "LogEntry objects loaded")

class Server:                                         # IT
    def __init__(self, hostname):
        self.hostname = hostname

servers = [Server("srv-01"), Server("srv-02")]
print(len(servers), "Server objects loaded")


# --- TRY IT ------------------------------------------------------------------
# 1. Add a percent(self) method to Record, then print the highest percent
#    value across every loaded record.
# 2. Compare this file to Week 4's load_records - what is the one line that
#    actually changed?
