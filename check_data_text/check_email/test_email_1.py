import re


def is_email(text):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    match = re.match(pattern, text)
    if match:
        return True
    else:
        return False


# text = input("Nhập địa chỉ email: ")
# if is_email(text):
#     print("Đây là một địa chỉ email hợp lệ.")
# else:
#     print("Đây không phải là một địa chỉ email hợp lệ.")
