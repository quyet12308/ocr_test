import re


def validate_phone_number(regex, phone_number):
    match = re.search(regex, phone_number)
    if match:
        return True
    return False


pattern = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")

test_phone_numbers = [
    "+1 (555) 123-4567",
    "555-123-4567",
    "555 123 4567",
    "+44 (0) 20 1234 5678",
    "02012345678",
    "invalid phone number",
    "0395615743",
    "096 320 8338",
    "024 3868 4179",
    "0895 558 468",
]

for number in test_phone_numbers:
    print(f"{number}: {validate_phone_number(pattern, number)}")
