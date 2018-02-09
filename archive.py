import glob
import os
import datebuilder

catalog_images = []
saved_images = []

def process(catalog):
    for image_size in catalog["images"]:
        for image in catalog["images"][image_size]:
            catalog_images.append(image)
    saved_images = get_saved_images()
    for new_image in catalog_images:
        if (new_image in saved_images):
            saved_images.remove(new_image)
    move_count = move_to_archive(saved_images)
    return move_count

def get_saved_images():
    images = []
    for f in glob.glob(os.path.join("images", "*", "*.jpg")):
        images.append(os.path.basename(f))
    return images

def move_to_archive(image_list):
    move_count = 0
    for f in glob.glob(os.path.join("images", "*", "*.jpg")):
        filename = os.path.basename(f)
        if filename in image_list:
            path_list = os.path.split(f)
            year_day = datebuilder.get_year_day_from_filename(path_list[1])
            new_path = os.path.join("archive", path_list[0], year_day, path_list[1])
            print(new_path)
            new_file_copy = 1
            directory = os.path.dirname(new_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
            while os.path.isfile(new_path):
                new_path = new_path + "." + str(new_file_copy)
                new_file_copy += 1
            os.rename(f, new_path)
            move_count += 1
    return move_count