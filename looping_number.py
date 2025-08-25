def is_looping(n):
    looping_char = set()

    while n != 1:

        if n in looping_char:
            return True

        looping_char.add(n)
        n = sum(int(x)**2 for x in str(n) )


    return False


n = 4
print(is_looping(n))