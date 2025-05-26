from datetime import datetime, time
from zoneinfo import ZoneInfo

def get_time_portland():
    dt = datetime.now(ZoneInfo("America/Los_Angeles"))
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def get_time_nyc():
    dt = datetime.now(ZoneInfo("America/New_York"))
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def get_time_london():
    dt = datetime.now(ZoneInfo("Europe/London"))
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def is_branch_open(tz_name):
    now = datetime.now(ZoneInfo(tz_name)).time()
    open_time = time(9, 0, 0)   # 9:00 AM
    close_time = time(17, 0, 0) # 5:00 PM
    if open_time <= now < close_time:
        return "Open"
    else:
        return "Closed"
