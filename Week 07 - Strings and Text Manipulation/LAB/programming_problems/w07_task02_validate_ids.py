# Task 2: Validate Student IDs


def is_valid_id(student_id):
    """Return True if the ID is M00 followed by 6 digits (9 characters)."""
    return (student_id.startswith("M00")
            and len(student_id) == 9
            and student_id[3:].isdigit())


student_ids = ["M00123456", "M0012345", "X00123456", "M00ABCDEF", "M00987654"]

for student_id in student_ids:
    print(f"{student_id}: {is_valid_id(student_id)}")
