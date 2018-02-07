import requests
import os

CATALOG_URL = "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/catalog.json"

def get_catlog():
    r = requests.get(CATALOG_URL)
    return r.json()

def build_url(date_str, size):
    size = str(size)
    return "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/" + date_str + "_GOES16-ABI-FD-GEOCOLOR-" + size + "x" + size + ".jpg"

def is_file_there(url):
    r = requests.head(url)
    return r.ok

def save_file(url, path):
    if (os.path.isfile(path)):
        return True
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        print("SUCCESS: " + url)
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(path, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
        return True
    else:
        print("FAILED: " + url)
        return False