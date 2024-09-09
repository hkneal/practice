import requests
import json

num1 = num2 = 12
num1 = 17

print(num1, num2)

# Works with sets not lists
friends = {"bob", "rolf", "anne"}
abroad = {"bob", "anne", "tommy"}

local = friends.difference(abroad)

# Combines the sets of unique
group = friends.union(abroad)

# Gives those in both
both = friends.intersection(abroad)

print(local)
print(group)
print(both)

time_url = "http://worldtimeapi.org/api/timezone/America/Los_Angeles"

def get_time():
    resp = requests.get(time_url)
    resp_json = resp.json()
    print(resp_json["datetime"])
    resp = resp.content
    parse_json = json.loads(resp)
    return parse_json["datetime"]

print(get_time())

range_lst = range(110)

print(range_lst)


print("Palindrome"[::-2])
