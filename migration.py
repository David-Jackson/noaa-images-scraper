import glob, os, datebuilder


# migrate() moves files from this scheme:
#     [archive (optional)]/images/{image_size}/{all_images_of_that_size}
# to this scheme:
#     [archive (optional)]/images/{image_size}/{date}/{all_images_of_that_size_on_that_date}

def migrate():
    count = 0
    count += move_files_into_date_folders(glob.glob(os.path.join("images", "*", "*.jpg")))
    count += move_files_into_date_folders(glob.glob(os.path.join("archive", "images", "*", "*.jpg")))
    return count

def move_files_into_date_folders(file_list):
    move_count = 0
    for f in file_list:
        filename = os.path.basename(f)
        path_list = os.path.split(f)
        year_day = datebuilder.get_year_day_from_filename(path_list[1])
        new_path = os.path.join(path_list[0], year_day, path_list[1])
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

print(str(migrate()) + " files moved")