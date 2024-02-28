import os
from PIL import Image


def count_images_in_directory(directory):
    count = 0
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            try:
                image = Image.open(filepath)
                image.close()
                count += 1
            except (IOError, SyntaxError):
                pass
    return count


def rename_images_in_directory(directory):
    count = 1
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            try:
                image = Image.open(filepath)
                image.close()
                new_filename = str(count) + ".jpg"
                new_filepath = os.path.join(directory, new_filename)
                os.rename(filepath, new_filepath)
                count += 1
            except (IOError, SyntaxError):
                pass


directory = "images_2"
# image_count = count_images_in_directory(directory)
# print("Số lượng ảnh trong thư mục:", image_count)

rename_images_in_directory(directory=directory)
