"""
WHAT self ACTUALLY IS
=======================
The thing that confuses everyone first. Run:  python 02_self_explained.py
"""

# --- 1. self is just "this particular object" -------------------------------
# When Python runs r1 = Record("R-001", 87.0, 100.0), it is really doing
# something closer to:   Record.__init__(r1, "R-001", 87.0, 100.0)
# self IS r1. Python passes it for you - you never write it in the call.

class Record:
    def __init__(self, label, value, limit):
        print(f"self is about to become this object, with label={label}")
        self.label = label       # "put label onto THIS object"
        self.value = value
        self.limit = limit

r1 = Record("R-001", 87.0, 100.0)


# --- 2. self must be the first parameter, every time - even though you --
#         never pass it yourself when calling

class Broken:
    def __init__(value):     # missing self - this is a mistake, see below
        pass

# Broken(100)
# TypeError: __init__() takes 1 positional argument but 2 were given
# Python tried to pass the new object AND 100 - but there was only room
# for one parameter.


# --- 3. self.name vs a plain local name are NOT the same --------------------

class Confusing:
    def __init__(self, value):
        value = value * 2      # a LOCAL variable - gone the moment __init__ ends
        self.value = value      # THIS is what actually gets stored on the object

c = Confusing(10)
print(c.value)     # 20 - from the self.value line, not the local one


# --- 4. self is how one object tells its own attributes apart from -----
#         another object's, inside a method

class Record2:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def summary(self):
        return f"{self.label}: {self.value}"    # self - THIS object's own values

r_a = Record2("R-001", 87.0, 100.0)
r_b = Record2("R-002", 120.0, 100.0)

print(r_a.summary())    # R-001: 87.0  - self was r_a here
print(r_b.summary())     # R-002: 120.0 - self was r_b here, same method


# --- TRY IT ------------------------------------------------------------------
# 1. Explain in one sentence why self has to be the first parameter of every
#    method, even though you never type it when calling.
# 2. Predict, then check: what happens if you name the first parameter
#    "this" instead of "self"? (It still works - self is a convention, not
#    a keyword. Do not actually do this in real code.)
