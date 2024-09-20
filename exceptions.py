"""Exception handling practice"""

num_loops = input()
for _ in range(int(num_loops)):
    line = input()
    values = line.split(" ")

    try:
        int(values[0] / int(values[1]))

    except ZeroDivisionError as e:
        print("Error Code:", e)
    except Exception as e:
        print("Error Code:", e)

