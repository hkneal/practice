
arr = []

op = "append(1)"

exec(f"arr.{op}")
print(arr)
arr.append(eval("2+2"))
print(arr)