import requests, json
import functools

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

# print(local)
# print(group)
# print(both)

time_url = "http://worldtimeapi.org/api/timezone/America/Los_Angeles"

def get_time():
    resp = requests.get(time_url)

    print(json.loads(resp.content))
    data = json.loads(resp.content)
    print(data["datetime"])
    print(f'Data Type using Loads: {type(data)}')


    resp_json = resp.json()
    print(type(resp_json))

    data_d = json.dumps(resp_json, sort_keys=True, indent=4)
    print(f'Data Type using Dumps: {type(data_d)}')

    with open("temp.json", 'w', encoding='utf-8') as f:
        f.write(json.dumps(resp_json))


    print(resp_json["datetime"])
    resp = resp.content
    parse_json = json.loads(resp)

    return parse_json["datetime"]

print(get_time())

range_lst = range(110)

print(range_lst)

print(dict(red="red", blue="blue", green=3))


def add_them(*args, **kwargs):
    print(args, kwargs)
    print(type(args), type(kwargs))
    sum = 0

    sum = functools.reduce(lambda sum, a: sum + a, list(args) )

    for x in args:
        sum = sum + x
    for v in kwargs.values():
        sum = sum + v

    return sum

print(add_them(2,34,567, a=7))

