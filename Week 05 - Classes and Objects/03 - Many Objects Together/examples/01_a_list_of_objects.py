"""
A LIST OF OBJECTS
==================
Week 4: a list of dicts. This week: a list of objects - same shape, and now
each item can also DO something, not just hold data.
Run:  python 01_a_list_of_objects.py
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


# --- 1. Build a list of objects, the same way you built a list of dicts -----

records = [
    Record("R-001", 87.0, 100.0),
    Record("R-002", 120.0, 100.0),
    Record("R-003", 45.0, 100.0),
]

print(type(records))          # list
print(type(records[0]))        # __main__.Record - each ITEM is a Record


# --- 2. Looping over it - one object per pass, same as before -----------

for record in records:
    print(record.label, record.status())


# --- 3. The difference from a list of dicts -----------------------------
# Compare this to Week 4:
#     record["label"]           dict - needs a status() FUNCTION written
#                                 separately, passed the dict's fields
#     record.label               object - status() is record.status(),
#                                 already knows its own value and limit

for record in records:
    if record.status() == "OVER LIMIT":
        print(f"{record.label} needs attention")


# --- TRY IT ------------------------------------------------------------------
# 1. Build a list of 3 Record objects by hand. Loop over it and print only
#    the labels of the ones that are OK.
# 2. Count how many records in your list are OVER LIMIT, using a running
#    total updated inside the loop.
