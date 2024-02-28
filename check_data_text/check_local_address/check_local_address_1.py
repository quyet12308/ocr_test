import re


def is_local_address(text):
    pattern = r"^[\w\s\-\,\.]+$"
    match = re.match(pattern, text)
    if match:
        return True
    else:
        return False
    


text = input("Nhập địa chỉ: ")
if is_local_address(text):
    print("Đây là một địa chỉ local hợp lệ.")
else:
    print("Đây không phải là một địa chỉ local hợp lệ.")
