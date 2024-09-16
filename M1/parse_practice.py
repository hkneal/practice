"""
Parse a log file 
"""
from datetime import datetime
import re


infile = "log.txt"
timestamp_profile = re.compile(r'\d\d/\d\d \d\d:\d\d:\d\d')



with open(infile, "r") as f:
    for line in f:
        datetime_match = timestamp_profile.search(line)
        line_lst = line.split(" ")
        
        if datetime_match:
            print(datetime_match.group())
            dt = datetime.strptime(datetime_match.group(), "%m/%d %H:%M:%S")
            print(datetime.strftime(dt, "%m/%d %H:%M:%S"))

        # print(line_lst)
        if len(line_lst) >= 3:
            # print(line_lst[2])
            pass

