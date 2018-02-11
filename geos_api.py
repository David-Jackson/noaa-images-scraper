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
        file_size = int(r.headers['Content-length'])
        print("SUCCESS: " + url + " | " + str(file_size))
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(path, 'wb') as f:
            chunk_count = 0
            for chunk in r.iter_content(1024):
                chunk_count += 1024
                percentage = int(10000 * chunk_count / file_size) / 100
                print(str(percentage) + "%", end='\r')
                f.write(chunk)
            print("")
        return True
    else:
        print("FAILED: " + url)
        return False