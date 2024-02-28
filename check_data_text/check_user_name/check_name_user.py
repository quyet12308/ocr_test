import re


def extract_name(text):
    pattern = r"\b[A-Z][a-zA-Z]*(?:\s[A-Z][a-zA-Z]*)+\b"
    matches = re.findall(pattern, text)
    return matches

def is_username(text):
    words = text.split()
    if len(words) >= 2 and len(words) <= 4:
        for word in words:
            if not word.isalpha():
                return False
        return True
    return False


# text = "Nguyen Van A is a software engineer at ABC Company."
# names = extract_name(text)
# if names:
#     print("Tên người: ", names)
# else:
#     print("Không tìm thấy tên người trong đoạn văn bản.")
