import datebuilder
import geos_api as api
import archive
import os

# cur = datebuilder.build()
# prev = datebuilder.build_previous(cur)
# nxt = datebuilder.build_next_after(cur)

# print(cur)
# print(prev)
# print(nxt)

# for x in range(10):
#     cur = datebuilder.build_previous(cur)
#     url = api.build_url(cur, 678)
#     print(cur, api.is_file_there(url))

success_count = 0
failed_count = 0

BASE_URL = "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/"
BASE_PATH = "images"

image_sizes = ["339x339", "678x678", "1808x1808", "5424x5424", "10848x10848"]

catalog = api.get_catlog()

move_count = archive.process(catalog)

print(str(move_count) + " files moved to archive")

for image_size in catalog["images"]:
    for f in catalog["images"][image_size]:
        # print(file)
        year_day = datebuilder.get_year_day_from_filename(f)
        saved = api.save_file(BASE_URL + f, os.path.join(BASE_PATH, image_size, year_day, f))
        success_count += 1 if saved else 0
        failed_count += 0 if saved else 1

print("Done: " + str(success_count) + " saved, " + str(failed_count) + " failed.")