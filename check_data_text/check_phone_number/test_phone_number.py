import re


def is_valid_phone_number(text):
    pattern = r"^(\+\d{1,3}\s?)?(\(\+\d{1,3}\)\s?)?\d{4}(\s?[-.]?\s?\d{3}){2}$"
    match = re.match(pattern, text)
    return match is not None


# text = input("Nhập vào một đoạn văn bản: ")
# if is_valid_phone_number(text):
#     print("Đây là số điện thoại hợp lệ.")
# else:
#     print("Đây không phải là số điện thoại hợp lệ.")
