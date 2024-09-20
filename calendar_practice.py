"""Determine what day the given date is"""

import calendar

line = input()

given_date = line.split(" ")
DAYMAP = {0: "MONDAY", 1:"Tuesday", 2:"WEDNESDAY", 3:"THURSDAY", 4:"FRIDAY", 5:"SATURDAY", 6:"SUNDAY"}
weekday = [calendar.weekday(int(given_date[2]), int(given_date[0]), int(given_date[1]))]

print(DAYMAP[weekday[0]])