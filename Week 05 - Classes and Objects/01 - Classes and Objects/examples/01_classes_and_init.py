"""
CLASSES AND __init__
=====================
A class is a blueprint. An object is one thing built from it.
Run:  python 01_classes_and_init.py
"""

# --- 1. A class defines the shape ---------------------------------------

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit


# --- 2. Creating an object - "instantiating" the class ----------------------

r1 = Record("R-001", 87.0, 100.0)

print(r1.label)     # R-001
print(r1.value)      # 87.0
print(type(r1))       # <class '__main__.Record'>


# --- 3. __init__ runs automatically, the moment you create the object -------
# You never call __init__ yourself. Record("R-001", 87.0, 100.0) calls it for you.


# --- 4. Each object keeps its own separate copy of the attributes -----------

r2 = Record("R-002", 120.0, 100.0)

print(r1.label, r1.value)   # R-001 87.0  - unchanged
print(r2.label, r2.value)    # R-002 120.0 - completely separate

r2.value = 999.0             # changing r2 does not touch r1
print(r1.value)               # still 87.0


# --- 5. Compare to Week 4's dict - same data, different access ----------

record_dict = {"label": "R-001", "value": 87.0, "limit": 100.0}
record_obj  = Record("R-001", 87.0, 100.0)

print(record_dict["label"])   # square brackets, a string key
print(record_obj.label)        # dot, a name - no quotes


# --- 6. Same idea, three fields ---------------------------------------------

class Dataset:                                        # AI / Data Science
    def __init__(self, name, rows, source):
        self.name = name
        self.rows = rows
        self.source = source

class Alert:                                          # Cyber Security
    def __init__(self, ip, severity, timestamp):
        self.ip = ip
        self.severity = severity
        self.timestamp = timestamp

class Server:                                         # IT
    def __init__(self, hostname, used, total):
        self.hostname = hostname
        self.used = used
        self.total = total

d = Dataset("survey_2026", 1200, "moodle")
a = Alert("10.0.0.5", "high", "09:01")
s = Server("srv-01", 87, 120)
print(d.name, d.rows)
print(a.ip, a.severity)
print(s.hostname, s.used, "/", s.total)


# --- TRY IT ------------------------------------------------------------------
# 1. Define a class Server with __init__(self, hostname, used, total). Create
#    one instance and print its hostname.
# 2. Create two Server instances with different data. Change one's `used`
#    value and prove the other is unaffected.
# 3. Predict, then check: what does print(r1) show, without a label or value -
#    just Record("R-001", 87.0, 100.0) printed directly?
