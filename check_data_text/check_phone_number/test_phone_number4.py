import re


def check_phone_number(string):
    # Kiểm tra độ dài chuỗi
    if len(string) < 10 or len(string) > 18:
        print("độ dài chuỗi ko đúng")
        return False
    # Kiểm tra sự tồn tại của ký tự không phải số
    # if not string.isdigit():
    #     print("ký tự không phải so")
    #     return False

    # Kiểm tra sự tồn tại của ký tự đặc biệt không cho phép
    if re.search(r"[a-zA-Z@]", string):
        print("có chứa các ký tự ko đúng")
        return False

    # Tạo một regex pattern để tìm các chuỗi liên tiếp là số
    pattern = re.compile(r"\d+")

    # Tìm tất cả các chuỗi liên tiếp là số trong chuỗi đầu vào
    matches = pattern.findall(string)

    # Kiểm tra độ dài của chuỗi số tìm được
    for match in matches:

        if len(match) >= 10 and len(match) <= 12:
            print("Độ dài số ko đúng")
            return True
    # print("trường hợp ko biết")
    return True


# check = input("Nhập sdt = ")
# if check_phone_number(check):
#     print(f"sdt {check} là sdt")
# else:
#     print(f"sdt {check} không là sdt")

phone_numbers = [
    "+84902 243 822",
    "(+84)902 243 822",
    "(+84) 902 243 822",
    "+84 902 243 822",
    "0902 243 822",
    "0902-243-822",
    "0902.243.822",
    "abc-000-123",
    "abc-123-4567",
]

for sdt in phone_numbers:
    if check_phone_number(sdt):
        print(f"sdt {sdt} là sdt")
    else:
        print(f"sdt {sdt} không là sdt")
