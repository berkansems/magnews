from datetime import datetime
import random

from news.models import News


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

def timeRand():

    time = datetime.now()
    year = time.year
    month = time.month
    day = time.day
    hour = time.hour
    min = str(time.minute)
    ran=random.randint(10000,99999)
    trand=str(f"{year}{month}{day}{hour}{min}{ran}")
    while len(News.objects.filter(rand=trand)) != 0:
        ran = random.randint(10000, 99999)
        trand = str(f"{year}{month}{day}{hour}{min}{ran}")

    return trand

