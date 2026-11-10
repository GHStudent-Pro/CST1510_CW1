"""
RECORD CHECK  -  my version
===========================

Name  :  Mahin Zaeem
Lane  :  AI
Date  :  11/11/2026

Run it:   python template.py

Reads messy survey responses from survey_lines.txt, cleans each one into a
dict, and flags responses whose rating or age is not a valid value.
"""

DATA_FILE = "survey_lines.txt"

# =================================================================== FUNCTIONS

def parse_line(raw_line):
    """Clean one 'survey, rating=.., age=..' line and return it as a dict."""
    line = raw_line.strip().lower()
    survey_part, rest = line.split(",", 1)
    record = {"survey": survey_part.strip()}
    for piece in rest.split(","):
        key, value = piece.split("=")
        record[key.strip()] = int(value.strip())
    return record


def status_of(record):
    """Return FLAGGED if the rating is not 1-5 or the age is not 18-99, else OK."""
    # Ratings must be on the 1-5 scale and respondents must be adults with a
    # realistic age, otherwise the response should not be used for analysis.
    if not (1 <= record["rating"] <= 5) or not (18 <= record["age"] <= 99):
        return "FLAGGED"
    return "OK"


def load_lines(path):
    """Return the non-blank lines of a file."""
    with open(path) as f:
        return [line for line in f if line.strip()]


# ====================================================================== INPUT

raw_records = load_lines(DATA_FILE)


# =============================================================== PROCESS + OUTPUT

flagged_count = 0

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)

    if status == "FLAGGED":
        flagged_count += 1

    print(f"{status:<8} {record}")

print(f"\n{len(raw_records)} records checked, {flagged_count} flagged.")
