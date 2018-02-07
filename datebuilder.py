from datetime import datetime


def pad_with_zeroes(value_str, desired_length):
    while (len(value_str) < desired_length):
        value_str = "0" + value_str
    return value_str

def get_day_of_year():
    day_of_year = datetime.utcnow().timetuple().tm_yday
    return build_day(day_of_year)

def build_day(day):
    day_str = str(day)
    return pad_with_zeroes(day_str, 3)

def get_year():
    return str(datetime.utcnow().year)

def get_time():
    hour = datetime.utcnow().hour
    hour_str = pad_with_zeroes(str(hour), 2)
    minute = int(datetime.utcnow().minute / 15) * 15
    minute_str = pad_with_zeroes(str(minute), 2)
    return hour_str + minute_str

def build():
    return get_year() + get_day_of_year() + get_time()

def parse_year(date_str):
    return int(date_str[:4])

def parse_day(date_str):
    return int(date_str[4:7])

def parse_time(date_str):
    return int(date_str[-4:-2]), int(date_str[-2:])

def build_next_after(prev_date_str):
    year = parse_year(prev_date_str)
    day = parse_day(prev_date_str)
    hour, minute = parse_time(prev_date_str)
    minute += 15
    if (minute >= 60):
        minute = minute - 60
        hour += 1
        if (hour >= 24):
            hour = hour - 24
            day += 1
            if (day > 365):
                day = day - 365
                year += 1
    
    return pad_with_zeroes(str(year), 4) + pad_with_zeroes(str(day), 3) + pad_with_zeroes(str(hour), 2) + pad_with_zeroes(str(minute), 2)

def build_previous(cur_date_str):
    year = parse_year(cur_date_str)
    day = parse_day(cur_date_str)
    hour, minute = parse_time(cur_date_str)
    minute -= 15
    if (minute < 0):
        minute = minute + 60
        hour -= 1
        if (hour < 0):
            hour = hour + 24
            day -= 1
            if (day <= 0):
                day = day + 365
                year -= 1
    
    return pad_with_zeroes(str(year), 4) + pad_with_zeroes(str(day), 3) + pad_with_zeroes(str(hour), 2) + pad_with_zeroes(str(minute), 2)
    