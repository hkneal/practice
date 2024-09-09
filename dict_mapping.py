users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "lkpassword"),
    (3, "Username", "1234"),
]

user_mapping = {user[1]: user for user in users}

print(user_mapping)
print(user_mapping["Bob"])

my_dict = dict(name="Jose", school="Computing", grades=(66,77,88))
print(my_dict)