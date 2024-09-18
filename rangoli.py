""" Create a rangoli from chars of size n """

def print_rangoli(size):
    # your code goes here

    # if size % 3 == 0:
    rangoli_length = (size * 2) -2
    # rangoli_length = (size * 2) - 1
    rangoli = []

    for i in range(size):
        rangoli_str = "-" * (rangoli_length - (i * 2) -1)
        rangoli.append("-")
        rangoli.append(chr(97 + (size -1) - i))

        if i == size -1:
            r_string = "".join(rangoli[1::])
            rev_string = "".join(list(reversed(rangoli))[1:len(rangoli) -1:])
        else:
            r_string = "".join(rangoli)
            rev_string = "".join(list(reversed(rangoli))[1::])
        print(rangoli_str + "".join(r_string) + "".join(rev_string) + rangoli_str)


    for i in range(1, size):
        rangoli_str = "-" * (i * 2)
        # print(i, rangoli_length, rangoli_str)
        rangoli.pop()
        rangoli.pop()
        # print(f"Rangoli: {rangoli}")
        # if i == size -1:
        r_string = "".join(rangoli[1::])
        rev_string = "".join(list(reversed(rangoli))[1:len(rangoli) -1:])
        # else:
        #     r_string = "".join(rangoli)
        #     rev_string = "".join(list(reversed(rangoli))[1::])
        print(rangoli_str + "".join(r_string) + "".join(rev_string) + rangoli_str)


print_rangoli(5)