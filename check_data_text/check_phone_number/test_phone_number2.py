import re


def is_valid_phone_number(text):
    """
    Checks if the given text is a valid phone number.

    Args:
      text: The text to check.

    Returns:
      True if the text is a valid phone number, False otherwise.
    """

    # Compile the regular expression pattern for a valid phone number.
    pattern = re.compile(r"^(?:\+84|0)\d{9}$")

    # Check if the text matches the pattern.
    return pattern.match(text) is not None


def get_phone_numbers(text):
    """
    Extracts all valid phone numbers from the given text.

    Args:
      text: The text to extract phone numbers from.

    Returns:
      A list of valid phone numbers.
    """

    # Compile the regular expression pattern for a valid phone number.
    pattern = re.compile(r"^(?:\+84|0)\d{9}$")

    # Find all the phone numbers in the text.
    phone_numbers = re.findall(pattern, text)

    # Check if each phone number is valid.
    valid_phone_numbers = []
    for phone_number in phone_numbers:
        if is_valid_phone_number(phone_number):
            valid_phone_numbers.append(phone_number)

    return valid_phone_numbers


# Test the function with the given phone numbers.
phone_numbers = [
    "+84902 243 822",
    "(+84)902 243 822",
    "(+84) 902 243 822",
    "+84 902 243 822",
    "0902 243 822",
    "0902-243-822",
    "0902.243.822",
    "abc-000-123",
]

for phone_number in phone_numbers:
    print(
        f"{phone_number} is a valid phone number: {is_valid_phone_number(phone_number)}"
    )

# Test the function with a sample text.
# text = """
# My phone number is +84902 243 822.
# You can also reach me at (0902) 243-822.
# My home phone number is 0902.243.822.
# """

# phone_numbers = get_phone_numbers(text)

# print("Valid phone numbers:")
# for phone_number in phone_numbers:
#     print(phone_number)
