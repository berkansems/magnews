from datetime import datetime


def timeSet():
    time = datetime.now()
    year = time.year
    month = time.month
    day = time.day
    hour = time.hour
    min = str(time.minute)
    if len(min)==1:
        min=str(f"0{min}")
    timesets= str(f"{year}/{month}/{day} | {hour}:{min}")
    return timesets

