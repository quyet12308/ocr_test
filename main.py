import easyocr
from check_data_text.check_phone_number.test_phone_number import *
from check_data_text.check_email.test_email_1 import *
from check_data_text.check_user_name.check_name_user import *
from check_data_text.check_web.check_website_url import *
from get_time import *
from write_error_log import *

reader = easyocr.Reader(["vi"], gpu=True)
# result = reader.readtext("images/test_hoa_don_2.png")
t1 = gettime3()
for i in range(20):
    t2 = gettime3()
    result = reader.readtext(f"images_2/{i+1}.jpg")
    # result = reader.readtext("images/test_cccd_1.jpg")

    # print(result)
    # print(type(result))
    names = []
    phone_numbers = []
    emails = []
    web_urls = []
    for bbox, text, prob in result:
        # print(f"{bbox},{text},{prob}")
        print(f"{text}")
    t3 = gettime3()
    write_to_file_7(
        filename="text_folders/gpu_check_time2.txt",
        result=f'image {i+1} => {time_difference(start_time=t2,end_time=t3,unit="ms")}',
    )

write_to_file_7(
    filename="text_folders/gpu_check_time2.txt",
    result=f'all image => {time_difference(start_time=t1,end_time=t3,unit="ms")}',
)
#     if is_valid_phone_number(text):
#         phone_numbers.append(text)
#     elif is_email(text):
#         emails.append(text)
#     elif extract_name(text):
#         names.append(text)
#     elif is_website(text):
#         web_urls.append(text)
# print(f"Image : {i+1}.jpg")
# print(f"Tên người dùng : {names}")
# print(f"SDT người dùng : {phone_numbers}")
# print(f"Email người dùng : {emails}")
# print(f"Web người dùng : {web_urls}")
