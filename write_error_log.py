import datetime
import pytz
import json


def gettime2():
    utc_time = datetime.datetime.now(pytz.utc)
    local_time = utc_time.astimezone(pytz.timezone("Asia/Ho_Chi_Minh"))
    t = local_time.strftime("%Y-%m-%d %H:%M:%S")
    return t


def write_to_file(filename, error):
    content = {"time": gettime2(), "error": error}
    content_str = json.dumps(content)
    with open(filename, "a") as file:
        file.write(content_str + "\n")


def write_to_file_4(filename, error):
    content = {"time": gettime2(), "error": error}
    content_str = json.dumps(content)
    with open(filename, "a") as file:
        file.write(content_str + "\n")


def write_to_file2(filename, error, id, predicted_class_index):
    content = {
        "time": gettime2(),
        "error": error,
        "id": f"{id}",
        "predicted_class_index": f"{predicted_class_index}",
    }
    content_str = json.dumps(content)
    with open(filename, "a") as file:
        file.write(content_str + "\n")


def write_to_file3(filename, error, predicted_class_index, url_img):
    content = {
        "time": gettime2(),
        "error": error,
        "predicted_class_index": f"{predicted_class_index}",
        "url_img": url_img,
    }
    content_str = json.dumps(content)
    with open(filename, "a") as file:
        file.write(content_str + "\n")


def write_to_file_4(filename, result, id_phone, url_img):
    content = {
        "time": gettime2(),
        "result": result,
        "id_phone": id_phone,
        "url_img": url_img,
    }
    content_str = json.dumps(content)
    with open(filename, "a") as file:
        file.write(content_str + "\n")


def write_to_file_5(filename, requests):
    content = {"time": gettime2(), "requests": requests}
    content_str = json.dumps(content)
    with open(filename, "a") as file:
        file.write(content_str + "\n")


def write_to_file_6(filename, error, url_img):
    content = {"time": gettime2(), "error": error, "url_img": url_img}
    content_str = json.dumps(content)
    with open(filename, "a") as file:
        file.write(content_str + "\n")


def write_to_file_7(filename, result):
    content = {"time": gettime2(), "result": result}
    content_str = json.dumps(content)
    with open(filename, "a") as file:
        file.write(content_str + "\n")


def write_to_file_8(filename, result, id_phone, url_img, Processing_Time):
    content = {
        "time": gettime2(),
        "result": result,
        "id_phone": id_phone,
        "url_img": url_img,
        "Processing_Time": Processing_Time,
    }
    content_str = json.dumps(content)
    with open(filename, "a") as file:
        file.write(content_str + "\n")


# write_to_file(
#     error="123",
#     filename="test1.txt"
# )
