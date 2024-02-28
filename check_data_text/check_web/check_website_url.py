import re


def is_website(text):
    pattern = (
        r"^(https?:\/\/)?([\w\-]+\.)*[\w\-]+(\.[a-zA-Z]{2,}){1,2}([\/\w\.-]*)*\/?$"
    )
    match = re.match(pattern, text)
    if match:
        return True
    else:
        return False


# text = input("Nhập địa chỉ website: ")
# if is_website(text):
#     print("Đây là một địa chỉ website hợp lệ.")
# else:
#     print("Đây không phải là một địa chỉ website hợp lệ.")
